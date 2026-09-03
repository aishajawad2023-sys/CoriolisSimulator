import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# PAGE SETUP
# -----------------------------------------

st.set_page_config(
    page_title="Coriolis Physics Simulator",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Coriolis Physics Simulator")

st.write(
    "Explore circular motion, velocity, and centripetal acceleration."
)

# -----------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------

st.sidebar.header("Simulation Controls")

radius = st.sidebar.slider(
    "Radius (m)",
    min_value=50.0,
    max_value=300.0,
    value=200.0,
    step=1.0
)

omega = st.sidebar.slider(
    "Angular velocity (rad/s)",
    min_value=0.1,
    max_value=5.0,
    value=1.0,
    step=0.1
)

mass = st.sidebar.slider(
    "Mass (kg)",
    min_value=0.1,
    max_value=10.0,
    value=1.0,
    step=0.1
)

# -----------------------------------------
# PHYSICS
# -----------------------------------------

# Linear velocity
velocity = omega * radius

# Centripetal acceleration
centripetal_acceleration = omega ** 2 * radius

# Centripetal force
centripetal_force = mass * centripetal_acceleration

# -----------------------------------------
# DISPLAY NUMBERS
# -----------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Linear velocity",
        f"{velocity:.2f} m/s"
    )

with col2:
    st.metric(
        "Centripetal acceleration",
        f"{centripetal_acceleration:.2f} m/s²"
    )

with col3:
    st.metric(
        "Centripetal force",
        f"{centripetal_force:.2f} N"
    )

# -----------------------------------------
# CIRCULAR MOTION GRAPH
# -----------------------------------------

theta = np.linspace(
    0,
    2 * np.pi,
    500
)

x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Current particle position
particle_angle = np.pi / 4

particle_x = radius * np.cos(particle_angle)
particle_y = radius * np.sin(particle_angle)

# -----------------------------------------
# CREATE FIGURE
# -----------------------------------------

fig, ax = plt.subplots(
    figsize=(8, 8)
)

# Circle
ax.plot(
    x,
    y,
    linewidth=2
)

# Particle
ax.scatter(
    particle_x,
    particle_y,
    s=150
)

# Center
ax.scatter(
    0,
    0,
    s=80
)

# Radius line
ax.plot(
    [0, particle_x],
    [0, particle_y],
    linewidth=2
)

# Make the graph circular
ax.set_aspect("equal")

ax.set_xlabel("x position (m)")
ax.set_ylabel("y position (m)")

ax.set_title(
    "Uniform Circular Motion"
)

ax.grid(True)

# -----------------------------------------
# SHOW GRAPH
# -----------------------------------------

st.pyplot(fig)

# -----------------------------------------
# EQUATIONS
# -----------------------------------------

st.subheader("Physics")

st.latex(
    r"v = \omega r"
)

st.latex(
    r"a_c = \omega^2 r"
)

st.latex(
    r"F_c = ma_c"
)

# -----------------------------------------
# EXPLANATION
# -----------------------------------------

st.info(
    "The velocity of an object in circular motion "
    "is tangent to the circle, while centripetal "
    "acceleration points toward the center."
)
