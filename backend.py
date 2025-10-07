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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="0.0.0.0", port=10000, reload=True)
