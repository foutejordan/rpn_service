from fastapi import FastAPI, HTTPException
from .operations import rpn_cal
from .schemas import OperationRequest, OperationResponse
import time

app = FastAPI()


@app.post("/evaluate/", response_model=OperationResponse)
def evaluate(operation: OperationRequest):
    try:
        if operation.expression is not None:
            start_time = time.time()
            result = rpn_cal(operation.expression)
            end_time = time.time()
            execution_time = end_time - start_time
            return {"result": result, "execution_time": execution_time}
        else:
            return {"Error": "Veullez entrer une expression Npi"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
