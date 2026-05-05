from app.db.memory_db import services, get_next_id
from app.schemas.service import ServiceCreate

def register_service(service_data: ServiceCreate) -> dict:
    service = {
        "id": get_next_id(services),
        "user_id": service_data.user_id,
        "name": service_data.name,
        "due_day": service_data.due_day
    }
    services.append(service)
    return service
