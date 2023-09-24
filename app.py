import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    for year in range(2020, 2071):
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

# Create a scatter plot for Population vs. GDP
st.write("### Population vs. GDP")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x="Population", y="GDP (USD)")
plt.xlabel("Population")
plt.ylabel("GDP (USD)")
plt.title("Population vs. GDP")
st.pyplot()

# Create a histogram for GDP Growth (%)
st.write("### GDP Growth Histogram")
plt.figure(figsize=(10, 6))
sns.histplot(filtered_df["GDP Growth (%)"], bins=20, kde=True)
plt.xlabel("GDP Growth (%)")
plt.ylabel("Frequency")
plt.title("GDP Growth Histogram")
st.pyplot()

# Data download button
st.sidebar.write("### Data Download")
if st.sidebar.button("Download Data as CSV"):
    st.sidebar.write("Downloading...")
    csv = filtered_df.to_csv(index=False)
    st.sidebar.download_button("Click to Download", csv, "filtered_data.csv")

# Display the data table
st.write("### Data Table")
st.write(filtered_df)
