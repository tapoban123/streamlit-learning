import streamlit as st


st.write("Hello World")
st.write({1: "Monday"})
st.write({"is Male": True})
st.write({"My Age": 19})
st.write(True)

# In-Line values also appear on Streamlit app.
"Hello from In-Line"

119
True
{"Hey":123}


is_pressed = st.button("Press Me") # Returns False when not pressed ELSE returns True
print(is_pressed)