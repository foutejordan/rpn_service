import csv
from io import StringIO
from fastapi import HTTPException

def export_operations_to_csv(redis_client):
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["npi_expression", "result"])

    keys = redis_client.keys()

    if not keys:
        raise HTTPException(status_code=404, detail="No operations found")

    for key in keys:
        expression = redis_client.hget(key, "npi_expression")
        result = redis_client.hget(key, "result")
        writer.writerow([expression, result])

    output.seek(0)
    return output
