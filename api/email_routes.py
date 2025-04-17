from fastapi import APIRouter, BackgroundTasks
from app.schemas.email import EmailSchema, AppointmentEmail
from app.services.email_service import EmailService

router = APIRouter()
email_service = EmailService()


@router.post("/send-appointment-confirmation")
async def send_appointment_confirmation(
        appointment: AppointmentEmail,
        background_tasks: BackgroundTasks
):
    email_data = EmailSchema(
        recipients=[appointment.patient_email],
        subject=f"Appointment Confirmation - {appointment.booking_reference}",
        template_name="appointment_confirmation.html",
        template_data={
            "patient_name": appointment.patient_name,
            "doctor_name": appointment.doctor_name,
            "appointment_date": appointment.appointment_date,
            "appointment_time": appointment.appointment_time,
            "hospital_name": appointment.hospital_name,
            "department": appointment.department,
            "booking_reference": appointment.booking_reference
        }
    )

    background_tasks.add_task(email_service.send_email, email_data)
    return {"message": "Appointment confirmation email queued"}


@router.post("/send-welcome-email")
async def send_welcome_email(email: str, name: str, background_tasks: BackgroundTasks):
    email_data = EmailSchema(
        recipients=[email],
        subject="Welcome to Our Hospital Portal",
        template_name="welcome_email.html",
        template_data={"name": name}
    )

    background_tasks.add_task(email_service.send_email, email_data)
    return {"message": "Welcome email queued"}
