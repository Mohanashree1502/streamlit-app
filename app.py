import streamlit as st

st.title("🚀 My Streamlit App")
st.write("Hello Nanba! This is running inside Docker 😎")

number = st.slider("Choose a number", 1, 100)
st.write("Your number squared is:", number * number)
