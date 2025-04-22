import streamlit as st


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "ai_response" not in st.session_state:
    st.session_state.ai_response = "Hi there!"

if "response" not in st.session_state:
    st.session_state.response = "Hi!"

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Say Something...")

# with st.chat_message("user"):
#     st.write("Hello")


with st.chat_message("assistant"):
    st.markdown(st.session_state.ai_response)
    st.session_state.chat_history.append(
        {"role": "assistent", "content": st.session_state.ai_response}
    )


if prompt is not None:
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})
