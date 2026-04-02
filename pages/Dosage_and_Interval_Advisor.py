import streamlit as st
import numpy as np

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(page_title="Fuzzy Dosage System", layout="centered")

st.title("Fuzzy Logic-based Dosage and Interval Recommendation")

st.markdown("""
This module simulates a **Fuzzy Inference System (FIS)** for pesticide dosage.  
It uses membership functions and rule-based reasoning instead of fixed formulas.
""")

# -----------------------------
# Inputs
# -----------------------------
severity = st.slider("Infestation Severity (%)", 0, 100, 50)
temperature = st.slider("Temperature (°C)", 10, 45, 30)
humidity = st.slider("Humidity (%)", 10, 100, 70)
growth = st.selectbox("Crop Growth Stage", ["Early", "Mid", "Late"])

# -----------------------------
# Membership Functions
# -----------------------------
def low(x, a, b):
    return np.clip((b - x) / (b - a), 0, 1)

def high(x, a, b):
    return np.clip((x - a) / (b - a), 0, 1)

def medium(x, a, b, c):
    return np.clip(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0, 1)

# -----------------------------
# Fuzzy Inference
# -----------------------------
def fuzzy_dosage(sev, temp, humid, stage):
    # Normalize
    sev_n = sev / 100

    # Membership values
    sev_low = low(sev_n, 0, 0.5)
    sev_high = high(sev_n, 0.3, 1)

    temp_high = high(temp, 25, 45)
    humid_high = high(humid, 60, 100)

    # Rules
    # Rule 1: High severity → High dosage
    rule1 = sev_high * 5.5

    # Rule 2: Low severity → Low dosage
    rule2 = sev_low * 2.0

    # Rule 3: High temp + high humidity → increase dosage
    rule3 = min(temp_high, humid_high) * 4.5

    # Rule 4: Late stage → reduce dosage
    stage_factor = 0.8 if stage == "Late" else 1.0

    # Aggregation (weighted average)
    numerator = rule1 + rule2 + rule3
    denominator = sev_high + sev_low + min(temp_high, humid_high) + 1e-5

    dosage = (numerator / denominator) * stage_factor

    return round(np.clip(dosage, 0.5, 6.0), 2)

# -----------------------------
# Interval Logic
# -----------------------------
def spray_interval(sev, humid):
    base = 12 - (sev / 10)
    if humid > 75:
        base -= 1  # faster pest spread in humidity
    return int(np.clip(base, 3, 14))

# -----------------------------
# Compute Results
# -----------------------------
dosage = fuzzy_dosage(severity, temperature, humidity, growth)
interval = spray_interval(severity, humidity)

# -----------------------------
# Output
# -----------------------------
st.write("### Recommended Treatment Plan")

col1, col2 = st.columns(2)

with col1:
    st.metric("Pesticide Dosage (ml/L)", dosage)

with col2:
    st.metric("Spray Interval (Days)", interval)

# -----------------------------
# Explanation (Optional Expand)
# -----------------------------
with st.expander("See reasoning"):
    st.write("""
    - Severity influences dosage directly (higher severity → higher dosage)
    - Temperature & humidity affect pest growth rate
    - Late crop stage reduces chemical requirement
    - Interval shortens when infestation is severe or humidity is high
    """)

st.markdown("---")
st.caption("Extend this system with real fuzzy rule bases, soil data, pest species, and weather APIs for production use.")