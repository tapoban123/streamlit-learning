import streamlit as st
import numpy as np
import pandas as pd

# Define time points (like days or months)
categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Generate random but smooth values using numpy
np.random.seed(42)  # For reproducibility

bar_data = np.random.randint(20, 100, size=len(categories))  # Random for bar chart
line_data = np.cumsum(np.random.randn(len(categories)) * 5 + 50)  # Smooth line trend
area_data = np.abs(
    np.random.normal(loc=30, scale=15, size=len(categories))
)  # Area with variations

# Build DataFrame
df = pd.DataFrame(
    {
        "Month": categories,
        "Bar Values": bar_data,
        "Line Values": line_data,
        "Area Values": area_data,
    }
)

scatter_x = np.random.randint(150, 200, size=10)  # Heights in cm
scatter_y = np.random.randint(50, 100, size=10)  # Weights in kg

scatter_df = pd.DataFrame({"Height(cm)": scatter_x, "Weight(kg)": scatter_y})

st.header("Area Chart")
st.area_chart(df)

st.header("Bar Chart")
st.bar_chart(bar_data)

st.header("Line chart")
st.line_chart(line_data)

st.header("Area Chart 2")
st.area_chart(area_data)

st.header("Scatter Chart")
st.scatter_chart(scatter_df)

# displaying map
st.header("Map")
df_map = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

data = pd.DataFrame(
    {
        "latitude": [37.7749, 34.0522, 40.7128],
        "longitude": [-122.4194, -118.2437, -74.0060],
    }
)


st.map(
    df_map,
)


# We can also display pyplot chart
