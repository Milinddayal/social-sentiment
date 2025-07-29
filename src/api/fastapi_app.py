from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(item: InputText):
    return {"sentiment": "positive", "confidence": 0.95}
