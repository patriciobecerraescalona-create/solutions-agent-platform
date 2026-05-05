from pydantic import BaseModel

class PaymentSchedule(BaseModel):
    service_id: int
    due_date: str
    amount: float
    status: str = "pending"

class PaymentResponse(BaseModel):
    id: int
    service_id: int
    due_date: str
    amount: float
    status: str
