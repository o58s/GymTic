import streamlit as st
from operations import add_user, get_user_by_username

def Create_account(username, password, name, age, height, weight, goal):
    existing_user = get_user_by_username(username)

    if existing_user:
        st.error("Username already exists. Please choose a different username.")
        return False

    user_id = add_user(username, password, name, age, height, weight, goal)
    return True, "Account created successfully!"

def login(username, password):
    user = get_user_by_username(username)

    if user is None:
        return False, "User not found. Please check your username."
    
    if user['password'] != password:
        return False, "Incorrect password. Please try again."

    st.session_state.user_id = user['user_id']   
    st.session_state.username = user['username']
    st.session_state.name = user['name']
    return True, "Login successful!"


def logout():
    st.session_state.pop('user_id', None)
    st.session_state.pop('username', None)
    st.session_state.pop('name', None)
    st.success("Logged out successfully!")