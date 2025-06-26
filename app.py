# app.py
import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('alcohol_model.pkl')

# App title
st.title("🍺 Alcohol Consumption Predictor")

# Input sliders
# Input sliders
beer = st.slider("Beer Servings", 0, 500, 100)
spirit = st.slider("Spirit Servings", 0, 500, 50)
wine = st.slider("Wine Servings", 0, 500, 30)
continent = st.selectbox("Continent", ["Africa", "Asia", "Europe", "North America", "Oceania", "South America"])

# Predict button
if st.button("Predict Alcohol"): 
    input_data = pd.DataFrame({ 
        'beer_servings': [beer],
        'spirit_servings': [spirit],
        'wine_servings': [wine],
        'continent_Africa': [1 if continent == "Africa" else 0],
        'continent_Asia': [1 if continent == "Asia" else 0],
        'continent_Europe': [1 if continent == "Europe" else 0],
        'continent_North America': [1 if continent == "North America" else 0],
        'continent_Oceania': [1 if continent == "Oceania" else 0],
        'continent_South America': [1 if continent == "South America" else 0]
    })  # Added closing brace
    
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Alcohol: {prediction:.2f} litres")
    