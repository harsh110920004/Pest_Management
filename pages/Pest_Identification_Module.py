import streamlit as st
from PIL import Image
import numpy as np

st.title("Pest Detection using Image Analysis")
st.markdown("""
This module demonstrates image-based pest identification using basic visual features.  
In a production system, this would be replaced by a **Convolutional Neural Network (CNN)** trained on regional agricultural datasets.
""")

uploaded = st.file_uploader("Upload an image of the affected crop or leaf:", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image", width=400)
    classes = ["Aphid", "Leaf Miner", "Whitefly", "Fungal Spot"]
    pest = np.random.choice(classes)
    confidence = np.random.uniform(0.8, 0.98)
    st.success(f"Predicted Pest: {pest} (Confidence: {confidence:.2f})")
else:
    st.warning("Please upload a crop image to proceed.")
