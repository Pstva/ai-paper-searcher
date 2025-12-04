from typing import List, Optional

from models.user import User
from schemas.user import UserUpdate
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select
from utils.utils import make_password_hash


def get_all_users(session: Session) -> List[User]:
    try:
        statement = select(User).options(
            selectinload(User.transactions),
            selectinload(User.chat_requests),
        )
        users = session.exec(statement).all()
        return users
    except Exception:
        raise


def get_user_by_id(user_id: int, session: Session) -> Optional[User]:
    try:
        statement = (
            select(User)
            .where(User.id == user_id)
            .options(
                selectinload(User.transactions),
                selectinload(User.chat_requests),
            )
        )
        user = session.exec(statement).first()
        return user
    except Exception:
        raise


def get_user_by_email(email: str, session: Session) -> Optional[User]:
    try:
        statement = (
            select(User)
            .where(User.email == email)
            .options(
                selectinload(User.transactions),
                selectinload(User.chat_requests),
            )
        )
        user = session.exec(statement).first()
        return user
    except Exception:
        raise


def create_user(user: User, session: Session) -> User:
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception:
        session.rollback()
        raise


def delete_user(user_id: int, session: Session) -> bool:
    try:
        user = get_user_by_id(user_id, session)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False
    except Exception:
        session.rollback()
        raise


def update_user(user: User, session: Session, user_update: UserUpdate) -> bool:
    try:
        user.user_type = (
            user_update.user_type if user_update.user_type else user.user_type
        )
        user.name = user_update.name if user_update.name else user.name
        user.password_hash = (
            make_password_hash(user_update.password)
            if user_update.password_hash
            else user.password_hash
        )
        user.balance = user_update.balance if user_update.balance else user.balance
        session.commit()
        session.refresh(user)
        return True
    except Exception:
        session.rollback()
        raise
