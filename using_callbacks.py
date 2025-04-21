import streamlit as st

# callbacks are on_click functions for buttons.
# callbacks are run before all other code in the next re-run

## So callbacks are used when we want to execute some code just at the beginning
# of re-run

st.title("Callbacks")

if "counter" not in st.session_state:
    st.session_state.counter = 0


def increment_counter():
    st.session_state.counter += 1


def decrement_counter():
    if st.session_state.counter != 0:
        st.session_state.counter -= 1


st.write(f"Counter Value: {st.session_state.counter}")

col1, col2 = st.columns(2)

with col1:
    st.button("Increment", on_click=increment_counter)
    
with col2:
    st.button("Decrement", on_click=decrement_counter)