import streamlit as st

st.title("Learning Streamlit")
st.header("Hello as Header")
st.subheader("Hello as Subheader")
st.markdown("Hello as _**Markdown**_")
st.caption("Hello as Caption")

st.divider()


code_example = """
#include <stdio.h>

int main(){
    printf("Hello World");
}
"""
st.code(code_example, language="C", line_numbers=True,)

python_code ="""
def add(num1: int, num2: int):
    print(num1 + num2)
"""

st.code(python_code, language="python")

java_script = """
fun myFunc(){
    console.log("Hello World")}
    
"""

st.code(java_script, language="javascript")