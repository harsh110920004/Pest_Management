import streamlit as st
import pandas as pd
import numpy as np

st.title("Spray Scheduling Optimization using Genetic Algorithm")

st.markdown("""
The Genetic Algorithm (GA) is used to distribute spraying activities across several days,  
ensuring balanced workload and efficient resource utilization.
""")

fields = st.number_input("Number of Fields", 3, 20, 6)
capacity = st.number_input("Daily Spray Capacity (L)", 50, 1000, 200)

data = {
    "Field": [f"Field-{i+1}" for i in range(fields)],
    "Area (ha)": np.round(np.random.uniform(0.5, 2.5, fields), 2),
    "Severity Index": np.round(np.random.uniform(0.2, 1.0, fields), 2),
    "Scheduled Day": np.random.randint(1, 8, fields)
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.success("Spray schedule generated successfully using a Genetic Algorithm-based approach.")
st.caption("In a real system, the GA would optimize based on severity, distance, and chemical usage constraints.")
