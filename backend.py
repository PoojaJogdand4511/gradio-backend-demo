# backend.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    name: str

@app.post("/process")
def process_data(data: InputData):
    response = f"Hello {data.name}, this is your backend speaking 👋"
    return {"message": response}
