from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def get():
    return {"Hello": "World"}
