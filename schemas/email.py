from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict

class EmailSchema(BaseModel):
    recipients: List[EmailStr]
    subject: str
    template_name: str
    template_data: Dict

class AppointmentEmail(BaseModel):
    patient_email: EmailStr
    patient_name: str
    doctor_name: str
    appointment_date: str
    appointment_time: str
    hospital_name: str
    department: str
    booking_reference: str
