import streamlit as st
import pandas as pd
import numpy as np



# -----------------------------
# App Config
# -----------------------------
st.set_page_config(page_title="GA Spray Scheduler", layout="centered")

st.title("Spray Scheduling Optimization using Genetic Algorithm")

st.markdown("""
This module uses a **Genetic Algorithm (GA)** to optimize spray schedules  
based on workload balancing and capacity constraints.
""")

# -----------------------------
# Inputs
# -----------------------------
fields = st.number_input("Number of Fields", 3, 20, 6)
capacity = st.number_input("Daily Spray Capacity (L)", 50, 1000, 200)
days = st.slider("Number of Days", 3, 10, 7)
seed = st.number_input("Random Seed", value=42)

np.random.seed(seed)

# -----------------------------
# Generate Field Data
# -----------------------------
areas = np.round(np.random.uniform(0.5, 2.5, fields), 2)
severity = np.round(np.random.uniform(0.2, 1.0, fields), 2)

df = pd.DataFrame({
    "Field": [f"Field-{i+1}" for i in range(fields)],
    "Area (ha)": areas,
    "Severity Index": severity
})

# Assume dosage proportional to severity
df["Required Spray (L)"] = df["Area (ha)"] * df["Severity Index"] * 50

st.dataframe(df, use_container_width=True)

# -----------------------------
# GA Functions
# -----------------------------
POP_SIZE = 30
GENERATIONS = 50
MUTATION_RATE = 0.1

def create_individual():
    return np.random.randint(1, days + 1, size=fields)

def fitness(individual):
    """Lower is better"""
    day_load = np.zeros(days)

    for i in range(fields):
        d = individual[i] - 1
        day_load[d] += df["Required Spray (L)"].iloc[i]

    # Penalize overload
    overload_penalty = np.sum(np.maximum(day_load - capacity, 0)**2)

    # Balance workload
    balance_penalty = np.var(day_load)

    return overload_penalty + balance_penalty

def selection(pop, fitnesses):
    idx = np.argsort(fitnesses)
    return pop[idx[:len(pop)//2]]

def crossover(parent1, parent2):
    point = np.random.randint(1, fields - 1)
    child = np.concatenate([parent1[:point], parent2[point:]])
    return child

def mutate(individual):
    if np.random.rand() < MUTATION_RATE:
        idx = np.random.randint(0, fields)
        individual[idx] = np.random.randint(1, days + 1)
    return individual

# -----------------------------
# GA Execution
# -----------------------------
population = np.array([create_individual() for _ in range(POP_SIZE)])

for _ in range(GENERATIONS):
    fitnesses = np.array([fitness(ind) for ind in population])
    selected = selection(population, fitnesses)

    new_population = []

    while len(new_population) < POP_SIZE:
        p1, p2 = selected[np.random.randint(len(selected), size=2)]
        child = crossover(p1, p2)
        child = mutate(child)
        new_population.append(child)

    population = np.array(new_population)

# Best solution
fitnesses = np.array([fitness(ind) for ind in population])
best_idx = np.argmin(fitnesses)
best_solution = population[best_idx]

df["Scheduled Day"] = best_solution

# -----------------------------
# Load Analysis
# -----------------------------
day_load = [0] * days
for i in range(fields):
    d = best_solution[i] - 1
    day_load[d] += df["Required Spray (L)"].iloc[i]

load_df = pd.DataFrame({
    "Day": list(range(1, days + 1)),
    "Total Load (L)": np.round(day_load, 2)
})

# -----------------------------
# Output
# -----------------------------
st.subheader("Optimized Spray Schedule")
st.dataframe(df, use_container_width=True)

st.subheader("Daily Load Distribution")
st.dataframe(load_df, use_container_width=True)

st.success("Optimized schedule generated using Genetic Algorithm.")

# -----------------------------
# Insights
# -----------------------------
st.markdown("---")
st.markdown(f"""
**Insights:**
- Total workload distributed across {days} days
- Capacity constraint: {capacity} L/day
- GA minimized overload and imbalance
- Best fitness score: {fitnesses[best_idx]:.2f}
""")

st.caption("This can be extended with distance cost, weather constraints, and multi-vehicle routing.")