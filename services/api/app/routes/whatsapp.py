from fastapi import APIRouter
from app.schemas.whatsapp import WhatsappIncoming
from app.services.whatsapp_service import handle_incoming_message
from app.db.memory_db import whatsapp_outbox

router = APIRouter(prefix="/whatsapp", tags=["WhatsApp"])

@router.post("/incoming")
def incoming_message(payload: WhatsappIncoming):
    return handle_incoming_message(payload)

@router.get("/outbox")
def get_outbox():
    return {"outbox": whatsapp_outbox}
