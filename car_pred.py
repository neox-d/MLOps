import pandas as pd
import yfinance as yf
import streamlit as st
import datetime

import pickle

# import sklearn

st.header("Cars 24 Price Prediction App")

df = pd.read_csv("Cars-24-price-prediction.csv")
# st.dataframe(df)

fuel_type = st.selectbox(
    "Select Fuel type",
    ("Diesel", "Petrol", "CNG", "Electric" "LPG"))

engine = st.slider("Engine", 500, 5000, step=100)

col1, col2 = st.columns(2)

with col1:

    transmission = st.selectbox(
        "Select transmission Type",
        ("Manual", "Automatic"))
with col2:

    seats = st.selectbox(
        "No. of seats",
        [4, 5, 6, 7, 8])
    
encode_dict = {
    "fuel_type": {"Diesel": 1, "Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
    "transmission": {"Manual": 1, "Automatic": 2}
}

def model_pred(fuel_encoded, transmission_enc, seats, engine):
    with open('car_pred', "rb") as file:
        reg_model = pickle.load(file)

        input_features = [[2010, 1, 72000, fuel_encoded, transmission_enc, 26.6, engine, 58.16, seats]]

        return reg_model.predict(input_features)

if st.button("Predict"):
    fuel_encoded = encode_dict['fuel_type'][fuel_type]
    transmission_enc = encode_dict['transmission'][transmission]

    price = model_pred(fuel_encoded, transmission_enc, seats, engine)
    st.text("Predicted Price is: " + str(price[0]))