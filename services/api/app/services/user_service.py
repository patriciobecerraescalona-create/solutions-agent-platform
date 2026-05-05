from app.db.memory_db import users, get_next_id
from app.schemas.user import UserCreate

def create_user(user_data: UserCreate) -> dict:
    user = {
        "id": get_next_id(users),
        "name": user_data.name,
        "phone": user_data.phone
    }
    users.append(user)
    return user
