from fastapi import APIRouter
from app.schemas.payment import PaymentSchedule, PaymentResponse
from app.services.payment_service import schedule_payment

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/schedule", response_model=PaymentResponse)
def schedule_payment_route(payment: PaymentSchedule):
    return schedule_payment(payment)
