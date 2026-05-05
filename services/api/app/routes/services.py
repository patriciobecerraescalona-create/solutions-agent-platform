from fastapi import APIRouter
from app.schemas.service import ServiceCreate, ServiceResponse
from app.services.service_service import register_service

router = APIRouter(prefix="/services", tags=["Services"])

@router.post("/register", response_model=ServiceResponse)
def register_service_route(service: ServiceCreate):
    return register_service(service)
