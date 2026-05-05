from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/create", response_model=UserResponse)
def create_user_route(user: UserCreate):
    return create_user(user)
