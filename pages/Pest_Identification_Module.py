iimport streamlit as st
from PIL import Image
import numpy as np

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="Pest Detection System",
    page_icon="🌿",
    layout="centered"
)

# -----------------------------
# Title and Description
# -----------------------------
st.title("Pest Detection using Image Analysis")

st.markdown("""
This module demonstrates image-based pest identification using basic visual features.

In a production system, this would be replaced by a **Convolutional Neural Network (CNN)** 
trained on region-specific agricultural datasets for accurate pest detection.
""")

# -----------------------------
# Helper Functions
# -----------------------------
def preprocess_image(image):
    """Convert image to numpy array and normalize"""
    img_array = np.array(image)
    return img_array / 255.0


def predict_pest(image_array):
    """Dummy prediction logic (replace with ML model)"""
    classes = ["Aphid", "Leaf Miner", "Whitefly", "Fungal Spot"]

    # Set seed for reproducibility (optional)
    np.random.seed(42)

    pest = np.random.choice(classes)
    confidence = np.random.uniform(0.80, 0.98)

    return pest, confidence


# -----------------------------
# File Upload Section
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload an image of the affected crop or leaf:",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_file is not None:
    try:
        # Load Image
        image = Image.open(uploaded_file).convert("RGB")

        # Display Image
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Preprocess Image
        processed_image = preprocess_image(image)

        # Prediction
        pest, confidence = predict_pest(processed_image)

        # Display Result
        st.success(f"Predicted Pest: {pest}")
        st.info(f"Confidence Score: {confidence:.2f}")

    except Exception as e:
        st.error(f"Error processing image: {str(e)}")

else:
    st.warning("Please upload a crop image to proceed.")


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("Note: This is a demo system. Replace the prediction function with a trained ML model for real-world use.")