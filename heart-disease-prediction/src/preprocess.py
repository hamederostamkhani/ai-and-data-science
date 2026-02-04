"""
Preprocessing functions to convert user input into model-ready format
"""

import pandas as pd
from config import *

def preprocess_user_input(inputs: dict) -> pd.DataFrame:
    """
    Converts user input dictionary into DataFrame with same order as model expects.
    Args:
        inputs (dict): user input from Streamlit sidebar
    Returns:
        pd.DataFrame: single-row DataFrame ready for prediction
    """
    # Map categorical inputs to numeric
    processed = {
        "age": inputs["age"],
        "sex": sex_mapping[inputs["sex"]],
        "cp": cp_mapping[inputs["cp"]],
        "trestbps": inputs["trestbps"],
        "chol": inputs["chol"],
        "fbs": fbs_mapping[inputs["fbs"]],
        "restecg": restecg_mapping[inputs["restecg"]],
        "thalach": inputs["thalach"],
        "exang": exang_mapping[inputs["exang"]],
        "oldpeak": inputs["oldpeak"],
        "slope": slope_mapping[inputs["slope"]],
        "ca": ca_mapping[inputs["ca"]],
        "thal": thal_mapping[inputs["thal"]]
    }

    # Convert to DataFrame
    df = pd.DataFrame([processed], columns=feature_order)
    return df