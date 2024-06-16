from pydantic import BaseModel


class OperationRequest(BaseModel):
    npi_expression: str


class OperationResponse(BaseModel):
    result: float
    execution_time: float
