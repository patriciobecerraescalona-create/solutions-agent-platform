from fastapi import APIRouter
from app.services.reminder_service import trigger_reminders

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/trigger-reminders")
def trigger_reminders_route():
    return trigger_reminders()
