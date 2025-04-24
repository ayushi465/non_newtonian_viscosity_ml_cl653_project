import streamlit as st
import numpy as np
import joblib

# Load the trained model (make sure this file exists in the same directory or update path)
model = joblib.load('decision_tree_viscosity_model.pkl')

# Page title
st.set_page_config(page_title="Viscosity Predictor")
st.title("🧪 Viscosity Predictor for Non-Newtonian Fluids")
st.markdown("Enter fluid parameters below to predict viscosity using the trained ML model.")

# Input fields
shear_rate = st.number_input("Shear Rate (1/s)", min_value=0.0, value=10.0, step=1.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, value=25.0, step=1.0)
particle_size = st.number_input("Particle Size (μm)", min_value=0.0, value=5.0, step=0.1)

# Predict button
if st.button("Predict Viscosity"):
    # Input as 2D array
    input_data = np.array([[shear_rate, temperature, particle_size]])
    prediction = model.predict(input_data)[0]
    
    # Display prediction
    st.success(f"Predicted Viscosity: **{prediction:.2f} cP**")
