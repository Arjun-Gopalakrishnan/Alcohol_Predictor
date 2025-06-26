# Alcohol Consumption Predictor
📌 Core Functionality
Inputs:

Interactive sliders for beer, spirit, and wine servings (0-500)

Dropdown menu for continent selection (Africa, Asia, Europe, etc.)

Output:

Real-time prediction of total_litres_of_pure_alcohol (e.g., "4.92 litres")

Deployment:

Hosted on Streamlit Cloud with a public URL
Technical Stack
Backend:

Python (Pandas, Scikit-learn)

Regression models (Random Forest, Linear Regression)

Hyperparameter tuning (GridSearchCV)

Frontend:

Streamlit for UI components

Auto-generated interactive charts

 Data & Modeling
Dataset: Global alcohol consumption data (beer, wine, spirit servings by country)

Key Steps:

Data cleaning (handled missing values)
Feature engineering (one-hot encoded continents)
Model selection (R² score optimization)
#Links
Live App: https://alcoholpredictor-gozxsmmabywfbqkvz6jmgr.streamlit.app/
