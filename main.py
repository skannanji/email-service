from fastapi import FastAPI
from app.api.email_routes import router as email_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(email_router, prefix="/email", tags=["email"])
