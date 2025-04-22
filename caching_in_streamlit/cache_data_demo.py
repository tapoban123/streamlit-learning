import streamlit as st
import time

# Returns immutable data.
# Cached output cannot be altered.
# If external applications alter output, data in cache will remain unchanged.

@st.cache_data(ttl=60)  # Cache this data for 60 seconds.
def fetch_data():
    # Fetching data
    time.sleep(3)
    return {"data": "data received from api"}


# Here we create permanent cache.
# We need to manually clear the cache here.
@st.cache_data
def fetch_more_data():
    time.sleep(3)
    return {"data", "More data fetched"}


st.write("Fetching")
data = fetch_data()  # function is called only after 60 seconds.
st.write(data)
st.button("Fetch Data", on_click=fetch_data)

@st.cache_data(ttl=120)  # Cache gets cleared after 120 seconds
def fetch_user(uid: str):
    # Here, this function is cached with the arguments.
    # So only if the arguments change within 120 seconds, 
    # the function is called. 
    time.sleep(3)
    return {"data": "user data"}
