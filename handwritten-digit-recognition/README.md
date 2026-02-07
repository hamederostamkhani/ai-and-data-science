# Handwritten Digit Recognition with CNN

A complete pipeline for **handwritten digit recognition** using PyTorch,  
with preprocessing, CNN model training, evaluation, and a Streamlit demo application.  

The project is **structured professionally** for academic and industrial presentations.

---

## 🗂 Project Structure

```mermaid
flowchart LR
    A[notebooks] --> B[01_data_exploration.ipynb]
    A --> C[02_preprocessing.ipynb]
    A --> D[03_model_training.ipynb]
    A --> E[04_evaluation.ipynb]

    F[src] --> G[model.py]
    F --> H[preprocessing.py]
    F --> I[predict.py]
    F --> J[train.py]

    K[app] --> L[streamlit_app.py]

    M[images] --> N[mnist_samples.png]
    M --> O[class_distribution.png]
    M --> P[preprocessing_comparison.png]
    M --> Q[training_curves.png]
    M --> R[confusion_matrix.png]
    M --> S[misclassified_samples.png]
    M --> T[streamlit_ui_prediction.png]

    A & F & K & M --> U[Project Root]
```

---

## 📝 Project Overview

This project demonstrates the full machine learning pipeline:

1. **Data Exploration**
   - Visualize MNIST dataset
   - Check class distribution  
   ![MNIST Samples](images/mnist_samples.png)  
   ![Class Distribution](images/class_distribution.png)

2. **Data Preprocessing**
   - Convert images to tensors
   - Normalize with MNIST mean & std
   - Ensures training stability  
   ![Preprocessing Comparison](images/preprocessing_comparison.png)

3. **Model Training**
   - CNN architecture with 2 Conv layers + 2 FC layers
   - Trained on MNIST dataset
   - Achieves ~98–99% training accuracy  
   ![Training Curves](images/training_curves.png)

4. **Model Evaluation**
   - Evaluate on MNIST test set
   - Confusion matrix and misclassified examples  
   ![Confusion Matrix](images/confusion_matrix.png)  
   ![Misclassified Samples](images/misclassified_samples.png)

5. **Streamlit Demo**
   - Draw a digit on the canvas
   - Predict using the trained CNN
   - UI shows canvas and prediction side by side  
   ![Streamlit Demo](images/streamlit_ui_prediction.png)

---

## 🏗️ Architecture Overview

- **src/**: core ML logic (model, preprocessing, inference, training)
- **notebooks/**: exploration, preprocessing, training, evaluation
- **app/**: Streamlit UI
- **images/**: figures for documentation and README

---

## ⚙️ How to Run

1️⃣ Install Dependencies

Install dependencies using the provided `requirements.txt`.
```bash
pip install -r requirements.txt
```

2️⃣ Train the Model (optional)

Train the model (optional, pre-trained weights are saved in `models/`).
```bash
python src/train.py
```

3️⃣ Run Streamlit App

Run the Streamlit app to test digit predictions.
```bash
streamlit run app/streamlit_app.py
```
---

## 📊 Future Improvements

- Add **data augmentation** to improve generalization
- Experiment with **more complex CNN architectures**
- Add **real-time webcam input** for digit prediction
- Convert to a **full web app with FastAPI + Streamlit frontend**

---

## 📦 requirements.txt

```text
torch==2.7.0
torchvision==0.22.0
numpy>=1.27.0
Pillow>=10.0.0
matplotlib>=3.8.0
scikit-learn>=1.3.0
streamlit>=1.25.0
streamlit-drawable-canvas==0.9.0
pandas>=2.1.0
```
> **Notes**:
> - Version numbers are approximate, compatible with latest stable releases.
> - `streamlit` is needed for the interactive web app.

---

## 🎓 References

- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
- PyTorch documentation: https://pytorch.org/
- Streamlit documentation: https://docs.streamlit.io/