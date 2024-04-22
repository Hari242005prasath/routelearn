import streamlit as st

def greet_user(name):
    return f"Hello, {name}! Welcome to your first Streamlit app."

def main():
    st.title("Basic Streamlit App")

    # Get user input for their name
    user_name = st.text_input("Enter your name:")

    if user_name:
        # Display a greeting message
        greeting_message = greet_user(user_name)
        st.write(greeting_message)

if __name__ == "__main__":
    main()
