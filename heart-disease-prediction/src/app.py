"""
Streamlit app for Heart Disease Prediction
"""

import streamlit as st
import joblib
from preprocess import preprocess_user_input

# Load trained model
model = joblib.load("../models/best_model.pkl")

# App Title
st.title("Heart Disease Prediction")
st.markdown("""
This application predicts the likelihood of heart disease using a machine learning model
trained on the UCI Heart Disease (Cleveland) dataset.
""")

# Sidebar for user input
st.sidebar.header("Patient Information")

# Age
age = st.sidebar.slider("Age", 20, 100, 50)

# Sex
sex = st.sidebar.radio("Sex", ["Male", "Female"])

# Chest Pain
cp = st.sidebar.selectbox(
    "Chest Pain Type",
    ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"]
)

# Resting Blood Pressure
trestbps = st.sidebar.number_input("Resting Blood Pressure", 80, 200, 120)

# Cholesterol
chol = st.sidebar.number_input("Serum Cholesterol", 100, 600, 200)

# Fasting Blood Sugar
fbs = st.sidebar.radio("Fasting Blood Sugar > 120 mg/dl", ["True (> 120 mg/dl)", "False (<= 120 mg/dl)"])

# Resting ECG
restecg = st.sidebar.selectbox(
    "Resting ECG",
    ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"]
)

# Max Heart Rate
thalach = st.sidebar.number_input("Maximum Heart Rate Achieved", 60, 250, 150)

# Exercise Induced Angina
exang = st.sidebar.radio("Exercise Induced Angina", ["Yes", "No"])

# ST Depression
oldpeak = st.sidebar.slider("ST Depression Induced by Exercise", 0.0, 10.0, 1.0, 0.1)

# ST Slope
slope = st.sidebar.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])

# Number of Major Vessels
ca = st.sidebar.selectbox("Number of Major Vessels Colored by Fluoroscopy", ["0", "1", "2", "3"])

# Thalassemia
thal = st.sidebar.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversable Defect"])

# Collect inputs
user_input = {
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}

# Predict Button
if st.button("Predict"):
    # Preprocess input
    input_df = preprocess_user_input(user_input)

    # Make prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # Display result
    if prediction == 1:
        st.error(f"⚠️ Heart Disease Detected! Probability: {probability*100:.2f}%")
    else:
        st.success(f"🟢 No Heart Disease Predicted. Probability: {probability*100:.2f}%")

# Model Info & Disclaimer
st.markdown("---")
st.markdown("""
**Model:** Random Forest Classifier  
**Dataset:** UCI Heart Disease (Cleveland)  
**Disclaimer:** This application is for educational purposes only and should not be used for medical diagnosis.
""")