# Viscosity Prediction of Non-Newtonian Fluids using Machine Learning

This project applies machine learning techniques to predict the viscosity of non-Newtonian fluids based on shear rate, temperature, and particle size. The work includes shear-thinning behavior analysis and a Streamlit-based web application for interactive predictions.

## Project Overview

- Data Preprocessing: Handling missing values, outlier removal, and feature scaling
- Model Training:
  - Linear Regression (baseline)
  - Decision Tree Regressor (final selected model)
  - Random Forest
  - Locally Weighted Linear Regression (LWLR)
- Model Evaluation: Metrics include R², RMSE, and MAE
- Shear-Thinning Analysis: Visualization on log-log scale to confirm expected rheological trends
- Deployment: A web app built using Streamlit for real-time viscosity prediction

## Live Demo

Access the app here:  
[Streamlit App Link](https://nonnewtonianviscositymlcl653project.streamlit.app/)  

## Files Included

- `app.py`: Streamlit app script
- `decision_tree_viscosity_model.pkl`: Trained machine learning model
- `code.ipynb`: Jupyter notebook with preprocessing, training, and evaluation
- `requirements.txt`: Required Python libraries for deployment

