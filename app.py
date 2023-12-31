import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Disable the Matplotlib warning
st.set_option('deprecation.showPyplotGlobalUse', False)

import pandas as pd
import numpy as np

# Original data
data = {
    "Country": [],
    "Year": [],
    "Population": [],
    "GDP (USD)": [],
    "GDP Growth (%)": [],
}

# Generate fixed random values for population, GDP, and GDP growth
population_values = np.random.randint(100_000_000, 1_500_000_000, size=250)  # Generate 250 random values
gdp_values = np.random.randint(1_000_000, 25_000_000_000, size=250)  # Generate 250 random values
gdp_growth_values = np.random.uniform(-10, 10, size=250)  # Generate 250 random values

# Generate data for each country from 1973 to 2022 with fixed random values
countries = ["USA", "China", "India", "Brazil", "Russia"]
value_index = 0  # Index for accessing fixed random values
for country in countries:
    for year in range(1973, 2023):  # Generate data for 50 years (1973 to 2022)
        data["Country"].append(country)
        data["Year"].append(year)
        data["Population"].append(population_values[value_index])
        data["GDP (USD)"].append(gdp_values[value_index])
        data["GDP Growth (%)"].append(gdp_growth_values[value_index])
        value_index += 1

df = pd.DataFrame(data)

# Streamlit App
st.title("Country Data Analysis")

# Sidebar for user input
st.sidebar.header("Filters")

# Create a filter for selecting data by country and year
selected_country = st.sidebar.selectbox("Select Country", df["Country"].unique())
selected_year = st.sidebar.slider("Select Year", min_value=df["Year"].min(), max_value=df["Year"].max(), value=df["Year"].max())

# Filter the data based on user input
filtered_df = df[(df["Country"] == selected_country) & (df["Year"] == selected_year)]

# Display basic statistics without the std column
st.write(f"### Basic Statistics for {selected_country} in {selected_year}")
st.dataframe(filtered_df.describe().drop("std"))  # Drop the std column

# Create a bar chart for GDP by country with better colors and labels
st.subheader("GDP Comparison")
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for idx, country in enumerate(df["Country"].unique()):
    country_data = df[(df["Country"] == country)]
    ax.bar(country, country_data["GDP (USD)"].max(), label=country, color=colors[idx])
ax.set_xlabel("Country")
ax.set_ylabel("GDP (USD)")
ax.set_title("GDP Comparison")
ax.legend()
st.pyplot(fig)
st.write("**Conclusion**: This bar chart provides a visual comparison of GDP (in USD) for selected countries in the chosen year. It illustrates the differences in economic strength among these nations.")

# Create a line chart for GDP growth with better colors and labels
st.subheader("GDP Growth Over the Years")
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for idx, country in enumerate(df["Country"].unique()):
    country_data = df[(df["Country"] == country)]
    ax.plot(country_data["Year"], country_data["GDP Growth (%)"], label=country, color=colors[idx], marker='o', linestyle='-')
ax.set_xlabel("Year")
ax.set_ylabel("GDP Growth (%)")
ax.set_title("GDP Growth Over the Years")
ax.legend()
st.pyplot(fig)
st.write("**Conclusion**: This line chart shows the GDP growth (%) over the years for selected countries. It provides insights into the economic performance and trends of these nations.")

# Create a pie chart to show the distribution of GDP among different countries
st.subheader("Distribution of GDP Among Countries")
gdp_by_country = df.groupby("Country")["GDP (USD)"].sum()
plt.figure(figsize=(8, 8))
plt.pie(gdp_by_country, labels=gdp_by_country.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot()
st.write("**Conclusion**: This pie chart visualizes the distribution of GDP (in USD) among different countries. It highlights the relative economic contributions of each nation.")
# Create a line chart for Population increment over the years
st.write("### Population Increment Over the Years")
fig, ax = plt.subplots(figsize=(10, 6))
selected_country_data = df[df["Country"] == selected_country]
ax.plot(selected_country_data["Year"], selected_country_data["Population"].diff().fillna(0), marker='o', linestyle='-', color='b')
ax.set_xlabel("Year")
ax.set_ylabel("Population Increment")
ax.set_title(f"Population Increment for {selected_country} Over the Years")
st.pyplot(fig)
# Conclusion for Population Increment chart
st.write("**Conclusion**: The line chart illustrates the population increment over the years for the selected country. It shows how the population has changed from year to year, providing insights into demographic trends and growth patterns.")
