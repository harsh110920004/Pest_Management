import streamlit as st
import numpy as np

st.title("Fuzzy Logic-based Dosage and Interval Recommendation")

st.markdown("""
The Fuzzy Logic model provides a more human-like decision mechanism for determining pesticide dosage.  
It considers multiple uncertain environmental factors such as pest severity, temperature, humidity, and crop maturity.
""")

severity = st.slider("Infestation Severity (%)", 0, 100, 50)
temperature = st.slider("Temperature (°C)", 10, 45, 30)
humidity = st.slider("Humidity (%)", 10, 100, 70)
growth = st.selectbox("Crop Growth Stage", ["Early", "Mid", "Late"])

def fuzzy_dosage(severity, temp, humid, stage):
    sev = severity / 100
    dosage = 2 + 3 * sev
    if stage == "Late": dosage -= 1
    if humid > 70: dosage += 0.5
    return round(np.clip(dosage, 0.5, 6.0), 2)

dosage = fuzzy_dosage(severity, temperature, humidity, growth)
interval = int(np.clip(12 - severity / 10, 3, 14))

st.write("### Recommended Treatment Plan")
col1, col2 = st.columns(2)
with col1:
    st.metric("Pesticide Dosage (ml/L)", dosage)
with col2:
    st.metric("Spray Interval (Days)", interval)

st.caption("This logic can be expanded to incorporate soil type, pest species, and weather forecasts for higher precision.")
