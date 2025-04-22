import streamlit as st

### Returns mutable data from cache. 

@st.cache_resource(ttl=60) # Cache created only for 60 seconds
def get_file_handler():
    file = open("file.txt", "a+")
    return file