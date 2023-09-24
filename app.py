import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
