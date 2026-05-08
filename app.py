import streamlit as st

st.title("AutoFlow AI")

task = st.text_input("Enter your task")

if st.button("Run"):
    st.write("Running workflow...")
    st.write(f"Task: {task}")
    st.write("Result: (simulated output)")
