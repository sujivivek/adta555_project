# -*- coding: utf-8 -*-
# pip install streamlit

import streamlit as st

st.title("Model Evaluation Dashboard")

metric_to_files = {
    "Loss Curves": ("images/LSTM_Loss.jpg"),
    "Confusion Matrix": ("images/LSTM_CM.jpg"),
    "Accuracy": ("images/LSTM_Accuracy.png"),
    "Word Count Distribution": ("images/WordCount.jpg"),
    "Same vs Real": ("images/SameReal.jpg")
}

metric = st.selectbox("Select Metric to Compare", list(metric_to_files.keys()))

# Load and Display Images
model_a_path = metric_to_files[metric]

# Check if files exist
if not (os.path.exists(model_a_path) and os.path.exists(model_b_path)):
    st.error("One or more image files are missing.")
else:
    col1 = st.columns(1)

    with col1:
        st.subheader("📌 Model A")
        img_a = Image.open(model_a_path)
        st.image(img_a, use_column_width=True)
