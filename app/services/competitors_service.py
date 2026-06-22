from app.repositories.competitors_repository import fetch_competitor_posts

def get_top_posts():
    posts = fetch_competitor_posts()
    return sorted(posts, key=lambda p: p.likes, reverse=True)