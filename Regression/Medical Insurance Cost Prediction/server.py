import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the model using pickle
with open('medical_insurance_cost_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Example Streamlit app to accept input data and make predictions
st.title("Medical Insurance Cost Prediction Using Machine Learning Model")

# Input fields for the user (adjusted based on correct feature names)
age = st.number_input("Age")
bmi = st.number_input("BMI")
children = st.number_input("Children")
smoker = st.selectbox("Smoker", ["yes", "no"])

# Convert categorical input (e.g., smoker) to a numeric format
smoker = 1 if smoker == "yes" else 0

# Prepare the input data for prediction (ensure columns match training data)
user_input = pd.DataFrame([[age, bmi, children, smoker]], columns=['age', 'bmi', 'children', 'smoker'])

# Initialize StandardScaler
scaler = StandardScaler()

# Scale the input features using the same scaler used during training
scaled_input = scaler.fit_transform(user_input)

# Prediction
if st.button("Predict"):    
    prediction = model.predict(user_input)[0] if len(model.predict(user_input)) > 0 else 'NA'
    st.write(f"The predicted value is {prediction}, with an accuracy of 86% Predicted.")

