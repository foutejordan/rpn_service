from fastapi import FastAPI, HTTPException
from .operations import rpn_cal
from .schemas import OperationRequest, OperationResponse
from .utils import format_expression
from .export_csv import export_operations_to_csv
import time
import hashlib
import redis
import os
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse

load_dotenv()

app = FastAPI()

redis_host = os.environ.get("REDIS_HOST")
redis_port = os.environ.get("REDIS_PORT")

redis_instance = redis.Redis(host=redis_host, port=int(redis_port), decode_responses=True)


@app.get("/export-csv/", tags=["Export Database"])
def export_csv():
    csv_data = export_operations_to_csv(redis_instance)
    response = StreamingResponse(iter([csv_data.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=operations.csv"
    return response


@app.post("/evaluate/", response_model=OperationResponse, tags=["RPN Calculator"], summary="Evaluate an RPN expression", description="This endpoint evaluates an expression in Reverse Polish Notation (RPN) and returns the result.")
def evaluate(operation: OperationRequest):
    try:
        if operation.npi_expression is not None:
            start_time = time.time()

            expression = operation.npi_expression

            expression_key = hashlib.sha256(expression.encode("utf-8")).hexdigest()
            result_from_db = redis_instance.hgetall(expression_key) if redis_instance.type(
                expression_key) == 'hash' else None
            print(result_from_db)
            if result_from_db is not None:
                result = float(result_from_db["result"])
            else:
                result = rpn_cal(expression)

                redis_instance.hset(expression_key, mapping={
                    "npi_expression": expression,
                    "result": result,
                })
            end_time = time.time()
            execution_time = end_time - start_time

            return {"result": result, "execution_time": execution_time}
        else:
            return {"Error": "Veullez entrer une expression Npi"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
