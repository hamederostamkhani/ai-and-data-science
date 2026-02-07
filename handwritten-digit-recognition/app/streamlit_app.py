import streamlit as st
import numpy as np
from PIL import Image
import sys

from streamlit_drawable_canvas import st_canvas

sys.path.append("src")
from predict import predict


st.set_page_config(
    page_title="Handwritten Digit Recognition",
    layout="centered"
)

st.title("✍️ Handwritten Digit Recognition")
st.write("Draw a digit (0–9) and let the CNN model predict it.")

# -----------------------------
# Layout: Two Columns
# -----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Draw Here")
    canvas_result = st_canvas(
        fill_color="white",
        stroke_width=15,
        stroke_color="black",
        background_color="white",
        width=280,
        height=280,
        drawing_mode="freedraw",
        key="canvas",
    )

with col2:
    st.subheader("Prediction")

    if canvas_result.image_data is not None:
        img = canvas_result.image_data

        # Convert to grayscale
        img = Image.fromarray(img.astype("uint8")).convert("L")
        img = img.resize((28, 28))

        st.image(img, caption="Processed Input", width=120)

        if st.button("Predict"):
            prediction = predict(img)
            st.success(f"Predicted Digit: {prediction}")
    else:
        st.info("Draw a digit to enable prediction.")