import streamlit as st

st.title("Few more features added")

name=st.text_input("Enter your name")

if st.button("Submit"):
    st.write(f"Hello", name)