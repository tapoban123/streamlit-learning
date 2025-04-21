import streamlit as st

# Sidebar layout
st.sidebar.title("This is a Sidebar")
st.sidebar.write("This is how you use a Sidebar in Streamlit.")
sidebar_input = st.sidebar.text_input("Enter some value")

# Tabs layout
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("You are in Tab 1")

with tab2:
    st.write("You are in Tab 2")

# Columns layout
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is Column 1")

with col2:
    st.header("Column 2")
    st.write("This is Column 2")
    
# Containers
with st.container(border=True):
    st.write("This is inside a Streamlit container.")
    st.write("You learnt how to use a Streamlit container.")

# Placeholders
placeholder = st.empty()
placeholder.write("This is a placeholder.\nIt can change on button clicks.")

if st.button("Change Placeholder text"):
    placeholder.write("This is the updated placeholder text.")
    
with st.expander("Expand for more details"):
    st.write("This is an Expander that expands on click.")
    
# Tooltip
st.write("Tooltip will appear on hover over this button.")
st.button("Hover over me", help="This is a tooltip.")

if sidebar_input:
    st.write(f"You have entered in sidebar_input: {sidebar_input}")
