import streamlit as st

# https://docs.streamlit.io/develop/concepts/multipage-apps

# We can also use st.navigate


def goto_Page1():
    st.switch_page("pages/1_Page1.py")


def goto_Page2():
    st.switch_page("pages/2_Page2.py")


st.set_page_config(page_title="Home Page", page_icon="🤓")

st.title("Home Page")

if st.button("Go to Page 1"):
    goto_Page1()
if st.button("Go to Page 2"):
    goto_Page2()
