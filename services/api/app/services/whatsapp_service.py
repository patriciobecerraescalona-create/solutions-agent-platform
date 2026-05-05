from app.db.memory_db import users, services, whatsapp_outbox
from app.schemas.whatsapp import WhatsappIncoming
from app.services.payment_service import get_pending_payments_by_user

def send_whatsapp_message(to_phone: str, message: str) -> None:
    whatsapp_outbox.append({
        "to_phone": to_phone,
        "message": message
    })
    print(f"[WHATSAPP MOCK OUTBOX] To: {to_phone} | Message: {message}")

def handle_incoming_message(payload: WhatsappIncoming) -> dict:
    # Find user by phone
    user = next((u for u in users if u["phone"] == payload.from_phone), None)
    if not user:
        send_whatsapp_message(payload.from_phone, "No te encuentro en nuestros registros.")
        return {"status": "user_not_found"}

    msg_lower = payload.message.lower()
    
    def format_amount(amt):
        return f"${int(amt):,}".replace(",", ".")

    # Simple rule based engine for the MVP
    if "ya pagué" in msg_lower or "ya pague" in msg_lower:
        pending = get_pending_payments_by_user(user["id"])
        if pending:
            pending[0]["status"] = "paid"
            send_whatsapp_message(user["phone"], "Perfecto, ya registré tu pago 👍")
        else:
            send_whatsapp_message(user["phone"], f"¡Genial {user['name']}! Aunque revisando mis registros, no tenías pagos pendientes. ¡Todo al día!")
    elif "pagar" in msg_lower or "qué tengo que pagar" in msg_lower or "que tengo que pagar" in msg_lower:
        pending = get_pending_payments_by_user(user["id"])
        if not pending:
            send_whatsapp_message(user["phone"], f"Oye {user['name']}, no tienes pagos pendientes. ¡Todo al día!")
        else:
            response_lines = [f"Hola {user['name']}, tienes los siguientes pagos pendientes:"]
            for p in pending:
                svc = next((s for s in services if s["id"] == p["service_id"]), None)
                svc_name = svc["name"] if svc else "Servicio"
                amt_str = format_amount(p["amount"])
                response_lines.append(f"- {svc_name}: {amt_str} vence el {p['due_date']}")
            send_whatsapp_message(user["phone"], "\n".join(response_lines))
    else:
        send_whatsapp_message(user["phone"], "No entendí tu mensaje. Puedes decirme 'ya pagué' o preguntar 'qué tengo que pagar'.")
        
    return {"status": "message_processed"}
