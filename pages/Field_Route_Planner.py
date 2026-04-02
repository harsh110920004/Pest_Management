import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

//Field Route Planner
# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(
    page_title="Field Route Optimization",
    layout="centered"
)

st.title("Field Route Optimization using Heuristic Search")

st.markdown("""
This module demonstrates route optimization for drones or field workers  
using **heuristic methods** (Nearest Neighbor + improvement heuristic).

In production, this can be extended to full **A\*** or **TSP solvers**.
""")

# -----------------------------
# Controls
# -----------------------------
num_points = st.slider("Number of Field Locations", 3, 15, 6)
seed = st.number_input("Random Seed (for reproducibility)", value=42)

np.random.seed(seed)
points = np.random.rand(num_points, 2) * 10

df = pd.DataFrame(points, columns=["X (km)", "Y (km)"])
st.dataframe(df, use_container_width=True)

# -----------------------------
# Helper Functions
# -----------------------------
def euclidean(a, b):
    return np.linalg.norm(a - b)


def total_distance(route, pts):
    dist = 0
    for i in range(len(route) - 1):
        dist += euclidean(pts[route[i]], pts[route[i + 1]])
    return dist


def nearest_neighbor(pts):
    n = len(pts)
    visited = [False] * n
    route = [0]
    visited[0] = True

    for _ in range(n - 1):
        last = route[-1]
        nearest = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i]:
                d = euclidean(pts[last], pts[i])
                if d < min_dist:
                    min_dist = d
                    nearest = i

        route.append(nearest)
        visited[nearest] = True

    return route


def two_opt(route, pts):
    """Simple optimization to improve route (2-opt swap)"""
    best = route
    improved = True

    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue

                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]

                if total_distance(new_route, pts) < total_distance(best, pts):
                    best = new_route
                    improved = True

        route = best

    return best


# -----------------------------
# Route Computation
# -----------------------------
initial_route = nearest_neighbor(points)
optimized_route = two_opt(initial_route, points)

initial_dist = total_distance(initial_route, points)
optimized_dist = total_distance(optimized_route, points)

# -----------------------------
# Visualization
# -----------------------------
fig, ax = plt.subplots()

# Initial route (dashed)
ax.plot(
    points[initial_route, 0],
    points[initial_route, 1],
    '--o',
    label=f"Initial Route ({initial_dist:.2f} km)"
)

# Optimized route (solid)
ax.plot(
    points[optimized_route, 0],
    points[optimized_route, 1],
    '-o',
    linewidth=2,
    label=f"Optimized Route ({optimized_dist:.2f} km)"
)

ax.set_title("Route Optimization Comparison")
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.legend()

st.pyplot(fig)

# -----------------------------
# Results
# -----------------------------
st.success(f"Optimized Distance: {optimized_dist:.2f} km")
st.info(f"Improvement: {initial_dist - optimized_dist:.2f} km saved")

st.markdown("---")
st.markdown("Note: This uses heuristic optimization. For exact solutions, use advanced TSP or A* variants.")