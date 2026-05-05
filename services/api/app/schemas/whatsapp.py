from pydantic import BaseModel

class WhatsappIncoming(BaseModel):
    from_phone: str
    message: str

class WhatsappMessage(BaseModel):
    to_phone: str
    message: str
