import streamlit as st

st.title("My First Streamlit App -1st")

# Input box
name = st.text_input("Enter your name:")

# Button
if st.button("Greet Me"):
    st.write(f"Hello, {name}! 👋")

# Slider example
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old.")


