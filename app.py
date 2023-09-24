import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mock data (replace this with real data or API integration)
data = {
    "Country": ["USA", "China", "India", "Brazil", "Russia"],
    "Year": [2020, 2020, 2020, 2020, 2020],
    "Population": [331002651, 1444216107, 1380004385, 212559417, 145934462],
    "GDP (USD)": [21433225, 14342932, 2875148, 1839755, 1710000],
    "GDP Growth (%)": [2.3, 6.1, -7.3, -4.1, -3.1],
}

df = pd.DataFrame(data)

# Streamlit App
st.title("UN Data Analysis")

# Sidebar for user input
st.sidebar.header("Filters")

# Create a filter for selecting data by country and year
selected_country = st.sidebar.selectbox("Select Country", df["Country"].unique())
selected_year = st.sidebar.slider("Select Year", min_value=df["Year"].min(), max_value=df["Year"].max(), value=df["Year"].max())

# Filter the data based on user input
filtered_df = df[(df["Country"] == selected_country) & (df["Year"] == selected_year)]

# Display basic statistics
st.write(f"### Basic Statistics for {selected_country} in {selected_year}")
st.write(filtered_df.describe())

# Create a bar chart for GDP by country
st.write("### GDP Comparison")
plt.figure(figsize=(10, 6))
plt.bar(df["Country"], df["GDP (USD)"])
plt.xlabel("Country")
plt.ylabel("GDP (USD)")
plt.title("GDP Comparison")
st.pyplot()

# Create a line chart for GDP growth by country
st.write("### GDP Growth Comparison")
plt.figure(figsize=(10, 6))
for country in df["Country"]:
    country_data = df[df["Country"] == country]
    plt.plot(country_data["Year"], country_data["GDP Growth (%)"], label=country)
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.title("GDP Growth Comparison")
plt.legend()
st.pyplot()

# Display the data table
st.write("### Data Table")
st.write(filtered_df)
