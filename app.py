import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Car Sales Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df

df = load_data()

# Show header
st.header("Explore Used Car Listings in the U.S.")

# Checkbox to show raw data
if st.checkbox("Show raw data"):
    st.write(df.head())

# Histogram: Price distribution
st.subheader("Distribution of Car Prices")
fig1 = px.histogram(df, x="price", nbins=50, title="Price Distribution")
st.plotly_chart(fig1)

# Scatter plot: Odometer vs Price
st.subheader("Relationship Between Odometer and Price")
fig2 = px.scatter(df, x="odometer", y="price", title="Price vs. Odometer")
st.plotly_chart(fig2)