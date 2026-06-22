from sqlmodel import select
from app.models.post import Post
from app.core.db import get_session

def fetch_competitor_posts():
    with next(get_session()) as session:
        statement = select(Post)
        return session.exec(statement).all()