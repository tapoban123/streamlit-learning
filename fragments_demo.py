import streamlit as st

# We can use fragments to rerun only a section of our app.
# We cannot return data from a fragment function.
# We need to use session_state values to access values of one function in another.

@st.fragment()
def toggle():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")
    # st.rerun(scope="fragment")  ## Default: reruns only the fragment
    # st.rerun(scope="app") ## Reruns the entire app
    
@st.fragment()
def input_text():
    st.text_input("Enter your name")
    st.date_input("Enter your birth data")
    
