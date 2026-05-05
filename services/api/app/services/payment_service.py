from app.db.memory_db import payments, get_next_id
from app.schemas.payment import PaymentSchedule

def schedule_payment(payment_data: PaymentSchedule) -> dict:
    payment = {
        "id": get_next_id(payments),
        "service_id": payment_data.service_id,
        "due_date": payment_data.due_date,
        "amount": payment_data.amount,
        "status": payment_data.status
    }
    payments.append(payment)
    return payment

def get_pending_payments_by_user(user_id: int) -> list:
    from app.db.memory_db import services
    user_service_ids = [s["id"] for s in services if s["user_id"] == user_id]
    user_payments = [p for p in payments if p["service_id"] in user_service_ids and p["status"] == "pending"]
    return user_payments
