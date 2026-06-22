from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/health")
def healthcheck():
    return {
        "status": "ok",
        "version": settings.version,
        "environment": settings.environment
    }
