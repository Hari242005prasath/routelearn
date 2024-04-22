import streamlit as st

def greet_user(name):
    return f"Hi {name} welcome to rmk"


st.title("Routelearn")

user_name = st.text_input("Enter your name:")
if user_name:
        # Display a greeting message
    greeting_message = greet_user(user_name)
    st.write(greeting_message)

