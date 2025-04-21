import streamlit as st

st.markdown("# Preserve state with _session_state_ in Streamlit.")

st.header("Without using session_state")
counter = 0

if st.button("Increment"):
    counter += 1
if st.button("Decrement"):
    counter -= 1

st.write(f"Value of Counter: {counter}")


st.header("Using session_state")
# session_state values are used to preserve state of our values
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Session Counter"):
    st.session_state.counter += 1

if st.button("Decrement Session Counter"):
    if st.session_state.counter != 0:
        st.session_state.counter -= 1

if st.button("Reset"):
    st.session_state.counter = 0


st.write(f"Counter Value: {st.session_state.counter}")
