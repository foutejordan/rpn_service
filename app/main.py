from fastapi import FastAPI, HTTPException
from .operations import rpn_cal
from .schemas import OperationRequest, OperationResponse
from .utils import format_expression
import time
import hashlib
import redis
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

redis_host = os.environ.get("REDIS_HOST")
redis_port = os.environ.get("REDIS_PORT")


redis_instance = redis.Redis(host=redis_host,  port=int(redis_port), decode_responses=True)


@app.post("/evaluate/", response_model=OperationResponse)
def evaluate(operation: OperationRequest):
    try:
        if operation.expression is not None:
            start_time = time.time()

            expression = format_expression(operation.expression)

            expression_key = hashlib.sha256(("".join(expression)).encode("utf-8")).hexdigest()
            result_from_db = redis_instance.hgetall(expression_key)
            print(result_from_db)

            if "result" in result_from_db.keys():
                result = result_from_db["result"]
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
