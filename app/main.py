from fastapi import FastAPI
from app.api.v1.routes_health import router as health_router
from app.api.v1.routes_competitors import router as competitors_router
from app.core.logging import setup_logging
from app.core.config import settings
from app.core.db import init_db

def create_app() -> FastAPI:
    setup_logging()
    init_db()
    app = FastAPI(title=settings.app_name, version=settings.version)

    app.include_router(health_router, prefix="/api/v1")
    app.include_router(competitors_router, prefix="/api/v1")
    return app

app = create_app()

