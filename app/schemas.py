from pydantic import BaseModel


class OperationRequest(BaseModel):
    expression: str


class OperationResponse(BaseModel):
    result: float
    execution_time: float
