import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Field Route Optimization using Heuristic Search")

st.markdown("""
This module demonstrates **Heuristic Search (A\*)** for minimizing the travel distance  
of drones or field workers during pesticide application.
""")

num_points = st.slider("Number of Field Locations", 3, 10, 5)
points = np.random.rand(num_points, 2) * 10

df = pd.DataFrame(points, columns=["X (km)", "Y (km)"])
st.dataframe(df, use_container_width=True)

# Nearest Neighbor route
dist = np.sqrt(np.sum(np.diff(points, axis=0)**2, axis=1)).sum()
fig, ax = plt.subplots()
ax.plot(points[:, 0], points[:, 1], '-o', linewidth=2)
ax.set_title(f"Optimized Route | Total Distance ≈ {dist:.2f} km")
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
st.pyplot(fig)
