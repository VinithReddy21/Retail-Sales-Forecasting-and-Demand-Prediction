import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("models/sales_forecast_model.pkl")

# Load Label Encoder
label_encoder = joblib.load("models/label_encoder.pkl")

# Page Config
st.set_page_config(
    page_title="Retail Sales Forecasting",
    page_icon="📈",
    layout="wide"
)

# Title
st.title("📈 Retail Sales Forecasting and Demand Prediction System")

st.markdown(
    "Predict future product sales using Machine Learning."
)

# Store Number
store_nbr = st.number_input(
    "Store Number",
    min_value=1,
    max_value=54,
    value=1
)

# Product Family
family = st.selectbox(
    "Product Family",
    list(label_encoder.classes_)
)

# Encode Family
family_encoded = label_encoder.transform(
    [family]
)[0]

# Promotion Count
onpromotion = st.number_input(
    "Items on Promotion",
    min_value=0,
    value=0
)

# Year
year = st.selectbox(
    "Year",
    [2017, 2018, 2019]
)

# Month
month = st.slider(
    "Month",
    min_value=1,
    max_value=12,
    value=1
)

# Day
day = st.slider(
    "Day",
    min_value=1,
    max_value=31,
    value=1
)

# Day of Week
day_of_week = st.slider(
    "Day Of Week",
    min_value=0,
    max_value=6,
    value=0
)

# Input Data
input_data = pd.DataFrame({
    "store_nbr": [store_nbr],
    "family": [family_encoded],
    "onpromotion": [onpromotion],
    "year": [year],
    "month": [month],
    "day": [day],
    "day_of_week": [day_of_week]
})

# Prediction
if st.button("Predict Sales"):

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Sales: {prediction[0]:.2f}"
    )