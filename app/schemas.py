from pydantic import BaseModel, Field


class OperationRequest(BaseModel):
    npi_expression: str = Field(..., description="L'expression en notation polonaise inverse (NPI) à évaluer.")


class OperationResponse(BaseModel):
    result: float = Field(..., description="Le résultat de l'évaluation de l'expression NPI.")
    execution_time: float = Field(..., description="Le temps d'exécution de l'évaluation en secondes.")
