import logging
from typing import Dict, List

import services.user
from database.database import get_session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from models.user import User
from utils.utils import make_password_hash

logger = logging.getLogger(__name__)
user_route = APIRouter()


@user_route.post(
    "/signup",
    response_model=Dict[str, str],
    status_code=status.HTTP_201_CREATED,
    summary="User Registration",
    description="Register a new user with email and password",
)
async def signup(data: User, session=Depends(get_session)) -> JSONResponse:
    try:
        if services.user.get_user_by_email(data.email, session):
            logger.warning(f"Signup attempt with existing email: {data.email}")
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists",
            )

        user = User(email=data.email, name=data.name, password=data.password)
        services.user.create_user(user, session)
        logger.info(f"New user registered: name:{data.name}, email:{data.email}")
        return {"message": "User successfully registered"}

    except Exception as e:
        logger.error(f"Error during signup: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating user",
        )


@user_route.post("/signin")
async def signin(data: User, session=Depends(get_session)) -> JSONResponse:
    user = services.user.get_user_by_email(data.email, session)
    if user is None:
        logger.warning(f"Login attempt with non-existent email: {data.email}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist"
        )

    if user.password_hash != make_password_hash(data.password):
        logger.warning(f"Failed login attempt for user: {data.email}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials passed"
        )

    return {"message": "User signed in successfully"}


@user_route.get(
    "/get_all_users",
    response_model=List[User],
    summary="Get all users",
    response_description="List of all users",
)
async def get_all_users(session=Depends(get_session)) -> List[User]:
    try:
        users = services.user.get_all_users(session)
        logger.info(f"Retrieved {len(users)} users")
        return users
    except Exception as e:
        logger.error(f"Error retrieving users: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving users",
        )
