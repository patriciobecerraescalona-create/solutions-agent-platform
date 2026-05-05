from app.db.memory_db import users, services, payments
from app.services.whatsapp_service import send_whatsapp_message
from datetime import datetime, timedelta

def trigger_reminders() -> dict:
    # Simula evaluar si vence manana
    tomorrow_str = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    sent_count = 0
    for payment in payments:
        if payment["status"] == "pending" and payment["due_date"] == tomorrow_str:
            svc = next((s for s in services if s["id"] == payment["service_id"]), None)
            if svc:
                user = next((u for u in users if u["id"] == svc["user_id"]), None)
                if user:
                    amt_str = f"${int(payment['amount']):,}".replace(",", ".")
                    msg = f"Oye {user['name']}, mañana vence tu {svc['name']} por {amt_str}\n\n[ YA PAGUÉ ]\n[ RECORDAR DESPUÉS ]"
                    send_whatsapp_message(user["phone"], msg)
                    sent_count += 1
                    
    return {"status": "reminders_triggered", "sent_count": sent_count, "evaluated_date": tomorrow_str}
