import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the page
st.set_page_config(page_title="Property Assessment", layout="wide")

# Add IAC University Logo
st.image(r"C:\Users\hp\Downloads\Images.jpeg", width=200)
st.title("Property Assessment Dashboard")

# Load the data (mockup data used for this demonstration)
data = {
    "Property Size": ["3.8 Marla", "1 Kanal", "10 Marla", "5 Marla", "7 Marla"],
    "Price (PKR)": [13500000, 31500000, 23000000, 9000000, 22500000],
    "Location": ["Rawalpindi", "Rawalpindi", "Rawalpindi", "Rawalpindi", "Rawalpindi"],
    "Agent": ["Cantt", "Premier Properties", "Gulistan-e-Jauhar", "Unknown", "Well Known Properties"]
}

df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("Filters")
location_filter = st.sidebar.multiselect("Select Location:", options=df["Location"].unique(), default=df["Location"].unique())
agent_filter = st.sidebar.multiselect("Select Agent:", options=df["Agent"].unique(), default=df["Agent"].unique())

# Filter data based on selection
filtered_data = df[(df["Location"].isin(location_filter)) & (df["Agent"].isin(agent_filter))]

# Main KPIs
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Properties", len(filtered_data))
col2.metric("Average Price (PKR)", f"{filtered_data['Price (PKR)'].mean():,.0f}")
col3.metric("Total Locations", len(filtered_data["Location"].unique()))

# Charts
st.subheader("Visualizations")

# Bar chart of property prices
fig_price = px.bar(
    filtered_data,
    x="Property Size",
    y="Price (PKR)",
    color="Location",
    title="Property Prices by Size and Location",
    labels={"Price (PKR)": "Price in PKR"},
    template="plotly_white",
)

st.plotly_chart(fig_price, use_container_width=True)

# Scatter plot of property prices
fig_scatter = px.scatter(
    filtered_data,
    x="Property Size",
    y="Price (PKR)",
    color="Agent",
    size="Price (PKR)",
    title="Scatter Plot of Prices by Agent",
    labels={"Price (PKR)": "Price in PKR"},
    template="plotly_white",
)

st.plotly_chart(fig_scatter, use_container_width=True)

# Data Table
st.subheader("Filtered Data")
st.dataframe(filtered_data)
