import joblib
import pandas as pd
from fastapi import FastAPI,Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = 'Housing API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/data')
def data():
    df = joblib.load(r"C:\Users\pc\PycharmProjects\WelcomeScreen\Mini Projects\Housing_Project\models\data_frame.pkl")
    return Response(df.to_json(orient='records'),media_type='application/json')


model = joblib.load(r"C:\Users\pc\PycharmProjects\WelcomeScreen\Mini Projects\Housing_Project\data\house_model.pkl")
model_columns = joblib.load(r"C:\Users\pc\PycharmProjects\WelcomeScreen\Mini Projects\Housing_Project\models\model_columns.pkl")

class HouseInput(BaseModel):
    longitude:float|int
    latitude:float|int
    housing_median_age:int
    total_rooms:int
    total_bedrooms:int
    population:int
    households:int
    median_income:float|int
    ocean_proximity_1H_OCEAN:int
    ocean_proximity_INLAND:int
    ocean_proximity_ISLAND:int
    ocean_proximity_NEAR_BAY:int
    ocean_proximity_NEAR_OCEAN:int

@app.post('/predict')
def Price_Prediction(data: HouseInput):
    df = pd.DataFrame([data.model_dump()])
    df = df.reindex(columns = model_columns , fill_value = 0)

    prediction = int(model.predict(df)[0])

    return {'Prediction': prediction}