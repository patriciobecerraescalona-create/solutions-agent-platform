from typing import Any, Dict, List
from pydantic import BaseModel

class ExecuteResponse(BaseModel):
    response: str
    actions: List[Any]
    trace: Dict[str, Any]
