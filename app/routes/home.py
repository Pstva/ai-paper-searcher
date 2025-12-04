from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

root_route = APIRouter()


@root_route.get(
    "/",
    response_model=JSONResponse,
)
async def read_root():
    try:
        return {"message": "Welcome to AI PaperSearcher API!"}
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@root_route.get(
    "/health",
    response_model=JSONResponse,
)
async def health_check():
    try:
        return {"status": "healthy"}
    except Exception:
        raise HTTPException(status_code=503, detail="Service unavailable")
