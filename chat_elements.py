import streamlit as st

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# with st.chat_message("user"):
#     st.write("Hello")


response = "I am AI."

prompt = st.chat_input("Say Something...")
with st.chat_message("assistant"):
    st.write("Hi there!")

if prompt is not None:
    with st.chat_message("user"):
        st.markdown(prompt)


st.session_state.chat_history.append({"role": "assistent", "content": response})
st.session_state.chat_history.append({"role": "user", "content": prompt})
