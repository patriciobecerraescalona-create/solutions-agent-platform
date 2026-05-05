from fastapi import APIRouter
from app.schemas.execute import ExecuteResponse
from app.services.executor import process_execution

router = APIRouter()

@router.post("/api/v1/execute", response_model=ExecuteResponse)
def execute(payload: dict):
    return process_execution(payload)
