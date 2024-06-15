from fastapi import FastAPI, HTTPException
from .operations import rpn_cal

app = FastAPI()

@app.get("/", response_model=dict[str, int])
def get():
    return {"resul": 2}

@app.post("/evaluate/", response_model=dict[str, int])
def evaluate(operation: str):
    print(operation)
    try:
        if operation is not None:
            result = rpn_cal(operation)
            return {"result": result}
        else:
            return {"Error": "Veullez entrer une expression Npi"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

