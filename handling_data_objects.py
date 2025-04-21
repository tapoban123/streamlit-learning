import streamlit as st
import pandas as pd

st.header("Dataframe")
df_dict = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "age": [28, 34, 25, 31, 29],
    "occupation": ["Engineer", "Designer", "Doctor", "Teacher", "Data Analyst"],
}
df = data = pd.DataFrame(df_dict)
st.dataframe(df)

# data editor
st.header("Data Editor")
st.data_editor(df)

# static table
st.header("Static Table")
st.table(df)

# json
st.header("Json")
st.json(df_dict)

# dictionary view
st.header("Dictionary view")
st.write(df_dict)

# metrics
st.header("Metrics")
st.metric("Age", value=19)

