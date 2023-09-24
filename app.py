import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example API URLs
population_url = "https://your-un-api-url/population"
gdp_url = "https://your-un-api-url/gdp"

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

population_data = fetch_data(population_url)
gdp_data = fetch_data(gdp_url)

# Load data
population_df = pd.DataFrame(population_data)
gdp_df = pd.DataFrame(gdp_data)

# Streamlit app
st.title("UN Data Analysis")

st.header("Population Data")
st.write(population_df.head())

st.header("GDP Data")
st.write(gdp_df.head())

st.subheader("Population Distribution")
st.bar_chart(population_df['population'])

st.subheader("GDP Distribution")
st.bar_chart(gdp_df['gdp'])

# You can add more visualizations and data analysis here


