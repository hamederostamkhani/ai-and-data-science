"""
Configuration file for constants, feature mappings, and default values
"""

# Feature mappings for categorical inputs
cp_mapping = {
    "Typical Angina": 1,
    "Atypical Angina": 2,
    "Non-Anginal Pain": 3,
    "Asymptomatic": 4
}

restecg_mapping = {
    "Normal": 0,
    "ST-T wave abnormality": 1,
    "Left ventricular hypertrophy": 2
}

slope_mapping = {
    "Upsloping": 1,
    "Flat": 2,
    "Downsloping": 3
}

thal_mapping = {
    "Normal": 3,
    "Fixed Defect": 6,
    "Reversable Defect": 7
}

ca_mapping = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3
}

sex_mapping = {
    "Male": 1,
    "Female": 0
}

fbs_mapping = {
    "True (> 120 mg/dl)": 1,
    "False (<= 120 mg/dl)": 0
}

exang_mapping = {
    "Yes": 1,
    "No": 0
}

# List of features in order expected by the model
feature_order = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]