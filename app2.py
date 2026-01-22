import streamlit as st


st.title("Kindly add your city and age")
age=st.slider("Select your age",0,100)
city=st.selectbox("Select your city",["delhi","mumbai","chennai","kolkata","bangalore"])

if st.button("Submit"):
    st.write("age:",age)
    st.write("city:",city)
