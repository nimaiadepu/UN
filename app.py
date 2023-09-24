import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
# Define your API key
api_key = "YOUR_API_KEY"

# Define the base URL for the UN Data API
base_url = "http://data.un.org/Handlers/"

# Define a function to fetch data from the API
def fetch_un_data(indicator, country="all", year="2020"):
    url = (
        f"{base_url}{indicator}.ashx?"
        f"DataSet=POP&crID={country}&sDM=YE&sp=0&" 
        f"tid={indicator}TH&thid=1&ts=5&" 
        f"rcID=1&occID=5&returnhtml=false&" 
        f"token={api_key}"
    )
    response = requests.get(url)
    print(response.text)  # Print the response content for debugging
    data = response.json()
    return data


# Fetch population data
population_data = fetch_un_data("P")
df_population = pd.DataFrame(population_data["Data"])
df_population.columns = ["Country", "Year", "Population"]
df_population["Year"] = df_population["Year"].astype(int)

# Fetch GDP data
gdp_data = fetch_un_data("GDP")
df_gdp = pd.DataFrame(gdp_data["Data"])
df_gdp.columns = ["Country", "Year", "GDP"]
df_gdp["Year"] = df_gdp["Year"].astype(int)

# Streamlit App
st.title("UN Data Analysis")
st.sidebar.header("Filters")

# Sidebar filters
selected_country = st.sidebar.selectbox("Select Country", df_population["Country"].unique())
year_range = st.sidebar.slider("Select Year Range", min(df_population["Year"]), max(df_population["Year"]), (2000, 2020))

# Filter the data
filtered_population_data = df_population[(df_population["Country"] == selected_country) & (df_population["Year"] >= year_range[0]) & (df_population["Year"] <= year_range[1])]
filtered_gdp_data = df_gdp[(df_gdp["Country"] == selected_country) & (df_gdp["Year"] >= year_range[0]) & (df_gdp["Year"] <= year_range[1])]

# Plot population and GDP
st.subheader(f"Population and GDP for {selected_country} ({year_range[0]}-{year_range[1]})")
plt.figure(figsize=(10, 5))
plt.plot(filtered_population_data["Year"], filtered_population_data["Population"], label="Population")
plt.plot(filtered_gdp_data["Year"], filtered_gdp_data["GDP"], label="GDP")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()
st.pyplot(plt)

# Display raw data
st.subheader("Raw Data")
st.write("Population Data:")
st.write(filtered_population_data)
st.write("GDP Data:")
st.write(filtered_gdp_data)
