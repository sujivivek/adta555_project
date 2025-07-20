# -*- coding: utf-8 -*-
# pip install streamlit

import streamlit as st
from PIL import Image
import os

metric_to_image = {
    "Loss Curves": ("images/LSTM_Loss.png"),
    "Confusion Matrix": ("images/LSTM_CM.png"),
    "Accuracy": ("images/LSTM_Accuracy.png"),
    "Word Count Distribution": ("images/WordCount.png"),
    "Fake vs Real": ("images/SameReal.png")
}

# Streamlit Title
st.title("ADTA5550 Project Model Metrics Dashboard")
st.header("Group 2")
st.subheader("Omar Perez, Goutham Sai Reddy Bolleddula, Sujatha Selvabarathi")

# Dropdown for metric selection
metric = st.selectbox("Select Metric to View", list(metric_to_image.keys()))

# Load and display image
image_path = metric_to_image[metric]

if os.path.exists(image_path):
    image = Image.open(image_path)
    st.text(metric_to_image[metric])
    st.image(image, caption=metric, use_container_width=True)
else:
    st.error(f"Image not found: {image_path}")
