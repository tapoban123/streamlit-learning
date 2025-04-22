import streamlit as st

st.title("Rerun Demo")

if st.button("Rerun app"):
    st.rerun(scope="app") # Scope can be either app or fragment