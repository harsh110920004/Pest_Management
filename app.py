import streamlit as st

st.set_page_config(page_title="Smart Agricultural Pest Management System", layout="wide")

st.title("Smart Agricultural Pest Management System")
st.subheader("A Multi-AI Approach for Sustainable Crop Protection")

st.markdown("""
### Overview
This system integrates multiple Artificial Intelligence (AI) techniques to support farmers and agricultural experts in managing pest infestations more efficiently.  
It combines **Computer Vision, Fuzzy Logic, Genetic Algorithms, and Heuristic Search** to achieve four main goals:

1. **Detect and classify pests or diseases** from crop images.  
2. **Recommend optimal pesticide dosage and spray intervals** based on environmental and crop factors.  
3. **Optimize spray scheduling and resource allocation** using genetic algorithms.  
4. **Plan the most efficient field routes** for drones or field workers.

---

### Methodology
Each component of the system is designed as a separate functional module for clarity and scalability.  
Use the navigation menu on the left to explore individual modules.
""")

st.image("https://cdn.pixabay.com/photo/2017/09/20/17/26/agriculture-2762993_1280.jpg", caption="AI-assisted Sustainable Farming", use_container_width=True)
