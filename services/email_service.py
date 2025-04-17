from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import Environment, FileSystemLoader
from app.core.config import settings
from app.schemas.email import EmailSchema
import logging

mail_config = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    TEMPLATE_FOLDER=settings.TEMPLATE_FOLDER
)

class EmailService:
    def __init__(self):
        self.fastmail = FastMail(mail_config)
        self.jinja_env = Environment(
            loader=FileSystemLoader(settings.TEMPLATE_FOLDER)
        )

    async def send_email(self, email_data: EmailSchema):
        try:
            template = self.jinja_env.get_template(email_data.template_name)
            html_content = template.render(**email_data.template_data)

            message = MessageSchema(
                subject=email_data.subject,
                recipients=email_data.recipients,
                body=html_content,
                subtype="html"
            )

            await self.fastmail.send_message(message)
            return True
        except Exception as e:
            logging.error(f"Email sending failed: {str(e)}")
            return False
