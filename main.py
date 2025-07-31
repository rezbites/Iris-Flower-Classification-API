from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pickle
import numpy as np
import os 
app = FastAPI()
import sklearn
print(sklearn.__version__)
# Mount static files (for images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict origins!
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model


with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)


label_map = {
    'Iris-setosa': {"name": "Iris Setosa", "img": "Iris Setosa.jpg"},
    'Iris-versicolor': {"name": "Iris Versicolor", "img": "Iris Versicolor.jpg"},
    'Iris-virginica': {"name": "Iris Virginica", "img": "Iris Virginica.jpg"}
}

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/predict")
def predict_species(data: IrisInput):
    input_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    prediction = model.predict(input_data)[0]
    pred_class = label_map[str(prediction)]
    return {
        "species": pred_class["name"],
        "image": pred_class["img"]
    }
