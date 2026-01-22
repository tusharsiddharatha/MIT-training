import streamlit as st

st.title("Basic calculator")


num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2

    elif operation == "Subtract":
        result = num1 - num2

    elif operation == "Multiply":
        result = num1 * num2
        
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    st.write("Result:", result)