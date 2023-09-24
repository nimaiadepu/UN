import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Extend the mock data to include values till 2070
data = {
    "Country": [],
    "Year": [],
    "Population": [],
    "GDP (USD)": [],
    "GDP Growth (%)": [],
}

# Generate data for each country from 2020 to 2070
countries = ["USA", "China", "India", "Brazil", "Russia"]
for country in countries:
    for year in range(1973, 2023):
        data["Country"].append(country)
        data["Year"].append(year)
        data["Population"].append(np.random.randint(100_000_000, 1_500_000_000))
        data["GDP (USD)"].append(np.random.randint(1_000_000, 25_000_000_000))
        data["GDP Growth (%)"].append(np.random.uniform(-10, 10))

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
colors = ['b', 'g', 'r', 'c', 'm']
for idx, country in enumerate(df["Country"].unique()):
    country_data = df[(df["Country"] == country)]
    ax.plot(country_data["Year"], country_data["GDP Growth (%)"], label=country, color=colors[idx], marker='o', linestyle='-')
ax.set_xlabel("Year")
ax.set_ylabel("GDP Growth (%)")
ax.set_title("GDP Growth Comparison")
ax.legend()
st.pyplot(fig)

# Create a line chart for Population increment over the years
st.write("### Population Increment Over the Years")
fig, ax = plt.subplots(figsize=(10, 6))
selected_country_data = df[df["Country"] == selected_country]
ax.plot(selected_country_data["Year"], selected_country_data["Population"].diff().fillna(0), marker='o', linestyle='-', color='b')
ax.set_xlabel("Year")
ax.set_ylabel("Population Increment")
ax.set_title(f"Population Increment for {selected_country} Over the Years")
st.pyplot(fig)

# Create a pie chart to show the distribution of GDP among different countries
st.subheader("Distribution of GDP Among Countries")
gdp_by_country = df.groupby("Country")["GDP (USD)"].sum()
plt.figure(figsize=(8, 8))
plt.pie(gdp_by_country, labels=gdp_by_country.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt

# Display the data table
st.write("### Data Table")
st.write(filtered_df)



