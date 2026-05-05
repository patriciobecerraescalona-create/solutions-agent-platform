from pydantic import BaseModel

class ServiceCreate(BaseModel):
    user_id: int
    name: str
    due_day: int

class ServiceResponse(BaseModel):
    id: int
    user_id: int
    name: str
    due_day: int
