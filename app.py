import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Extend the mock data to include values till 2070
data = {
    "Country": ["USA", "China", "India", "Brazil", "Russia"] * 11,  # Repeat each country for 11 years
    "Year": list(range(2020, 2071)) * 5,  # Generate years from 2020 to 2070 repeated 5 times
    "Population": [331002651, 1444216107, 1380004385, 212559417, 145934462] * 11,
    "GDP (USD)": [21433225, 14342932, 2875148, 1839755, 1710000] * 11,
    "GDP Growth (%)": [2.3, 6.1, -7.3, -4.1, -3.1] * 11,
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
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["Country"], df["GDP (USD)"])
ax.set_xlabel("Country")
ax.set_ylabel("GDP (USD)")
ax.set_title("GDP Comparison")
st.pyplot(fig)

# Create a line chart for GDP growth by country
st.write("### GDP Growth Comparison")
fig, ax = plt.subplots(figsize=(10, 6))
for country in df["Country"]:
    country_data = df[df["Country"] == country]
    ax.plot(country_data["Year"], country_data["GDP Growth (%)"], label=country)
ax.set_xlabel("Year")
ax.set_ylabel("GDP Growth (%)")
ax.set_title("GDP Growth Comparison")
ax.legend()
st.pyplot(fig)

# Display the data table
st.write("### Data Table")
st.write(filtered_df)

