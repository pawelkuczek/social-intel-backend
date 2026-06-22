from fastapi import APIRouter
from app.services.competitors_service import get_top_posts

router = APIRouter()

@router.get("/competitors/top")
def top_competitors():
    return get_top_posts()
