
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

# Load model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🚗 AutoPricer AI – Predict Used Car Prices")
st.write("Enter vehicle details below to get an estimated market price.")

# User inputs
year = st.slider("Manufacturing Year", 2000, 2025, 2020)
mileage = st.number_input("Mileage (in miles)", value=30000)
cylinders = st.selectbox("Engine Cylinders", [4, 6, 8])
is_luxury = st.selectbox("Is it a luxury brand?", ["No", "Yes"])
fuel_gasoline = st.selectbox("Fuel Type is Gasoline?", ["Yes", "No"])
model_freq = st.slider("Model Popularity (0 = rare, 200+ = very common)", 0, 250, 100)
price_per_mile = st.number_input("Estimated Price Per Mile", value=0.5)

# Feature Engineering
car_age = 2025 - year
is_luxury = 1 if is_luxury == "Yes" else 0
fuel_gasoline = 1 if fuel_gasoline == "Yes" else 0

# Arrange features as per training order
input_data = pd.DataFrame([{
    'cylinders': cylinders,
    'mileage': mileage,
    'car_age': car_age,
    'price_per_mile': price_per_mile,
    'is_luxury': is_luxury,
    'fuel_Gasoline': fuel_gasoline,
    'model_freq': model_freq
}])

# Align with trained model features (scaling etc.)
input_scaled = scaler.transform(input_data)
predicted_price = model.predict(input_scaled)[0]

st.success(f"💰 Estimated Vehicle Price: ${predicted_price:,.2f}")


sample_car = {
    'cylinders': 6,
    'mileage': 30000,
    'year': 2021,
    'price_per_mile': 1.5,  # Approx, or you can leave as NaN and fill with median
    'is_luxury': 0,
    'fuel_Gasoline': 1,
    'model_freq': 100
}
import pandas as pd

car_age = 2025 - sample_car['year']

# Create dataframe with same order as training features
input_df = pd.DataFrame([{
    'cylinders': sample_car['cylinders'],
    'mileage': sample_car['mileage'],
    'car_age': car_age,
    'price_per_mile': sample_car['price_per_mile'],
    'is_luxury': sample_car['is_luxury'],
    'fuel_Gasoline': sample_car['fuel_Gasoline'],
    'model_freq': sample_car['model_freq']
}])

input_scaled = scaler.transform(input_df)
predicted_price = forest.predict(input_scaled)[0]
print(f"💰 Predicted Price: ${predicted_price:,.2f}")








