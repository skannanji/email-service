from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Hospital Appointment Email Service"
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    TEMPLATE_FOLDER: str = "app/templates"

    class Config:
        env_file = ".env"

settings = Settings()
