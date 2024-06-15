from fastapi import FastAPI, HTTPException
from .operations import rpn_cal
import time


app = FastAPI()

@app.get("/", response_model=dict[str, int])
def get():
    return {"resul": 2}

@app.post("/evaluate/", response_model=dict[str, int])
def evaluate(operation: str):
    try:
        if operation is not None:
            start_time = time.time()
            result = rpn_cal(operation)
            end_time = time.time()
            execution_time = end_time - start_time
            return {"result": result, "execution_time": execution_time}
        else:
            return {"Error": "Veullez entrer une expression Npi"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

