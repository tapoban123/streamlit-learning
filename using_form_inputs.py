import streamlit as st
from datetime import datetime
import time

st.title("Form Inputs")

min_date = datetime(2000, 1, 1)
max_date = datetime.now()

form_values = {
    "name": None,
    "age": None,
    "password": None,
    "feedback": None,
    "date": None,
    "time": None,
    "option": None,
    "gender": None,
    "range": None,
    "slider_range": None,
    "notify": None,
    "dark_mode": None,
}


# Using the following with statement prevents unnecessary rebuilds.
with st.form("form_demo"):
    # Text inputs
    form_values["name"] = st.text_input(
        label="Enter your name:", placeholder="Your name"
    )
    form_values["age"] = st.number_input("Enter your age", min_value=10)
    form_values["password"] = st.text_input("Enter your password", type="password")
    form_values["feedback"] = st.text_area("Provide your feedback")

    # Date and time inputs
    form_values["date"] = st.date_input(
        "Enter your date of birth", max_value=max_date, min_value=min_date
    )
    form_values["time"] = st.time_input("Choose a preferred time")

    # Selectors and Sliders
    form_values["option"] = st.radio(
        "Choose an option", options=["Option 1", "Option 2", "Option 3"]
    )
    form_values["gender"] = st.selectbox(
        "Select your gender", options=["Male", "Female", "Other"]
    )
    form_values["range"] = st.slider(
        "Select your preferred range", min_value=0, max_value=20
    )
    form_values["slider_range"] = st.select_slider(
        "Select a slider range", options=[1, 5, 10, 15, 20]
    )

    # Toggles and Checkboxes
    form_values["notify"] = st.checkbox("Receive notifications.")
    form_values["dark_mode"] = st.checkbox("Dark Mode:", value=False)

    is_submitted = st.form_submit_button(label="Submit")

    if is_submitted:
        if not all(form_values.values()):
            st.warning("Please enter all the values.")
        else:
            st.balloons()
            st.success("Your form has been submitted.")

if is_submitted and all(form_values.values()):
    st.header("User Details:")

    st.write(f"Name: {form_values["name"]}")
    st.write(f"Name: {form_values["age"]}")
    st.write(f"Name: {form_values["password"]}")
    st.write(f"Name: {form_values["time"]}")
    st.write(f"Name: {form_values["date"]}")
    st.write(f"Name: {form_values["feedback"]}")
    st.write(f"Name: {form_values["option"]}")
    st.write(f"Name: {form_values["gender"]}")
    st.write(f"Name: {form_values["range"]}")
    st.write(f"Name: {form_values["slider_range"]}")
    st.write(f"Name: {form_values["notify"]}")
    st.write(f"Name: {form_values["dark_mode"]}")
