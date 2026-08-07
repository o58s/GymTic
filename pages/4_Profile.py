import streamlit as st
from operations import get_user_by_id, update_user, delete_user
from auth import logout
from time import sleep

#Check if user is logged in
if "user_id" not in st.session_state:
    st.warning("You need to log in to access your profile.")
    st.stop()

user_id = st.session_state.user_id

user = get_user_by_id(user_id)

if user is None:
    st.error("User not found.")
    st.stop()

st.title("Profile")

username = user["username"]
st.write(f"### Username: {username}")

st.divider()


st.subheader('Personal Information')

name = st.text_input("Name", value=user["name"])
age = st.number_input("Age", min_value=1, value=user["age"])
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=float(user["height"]))
weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=float(user["weight"]))

goal = st.selectbox(
    "Goal",
    [
        "Strength",
        "Hypertrophy",
        "Fat Loss"
    ],
    index=[
        "Strength",
        "Hypertrophy",
        "Fat Loss"
    ].index(user["goal"])
)

if st.button("Update Profile"):
    update_user(user_id, name, age, height, weight, goal)
    st.success("Profile updated successfully!")
    sleep(3)
    st.rerun()

st.divider()

# Logout Section
st.subheader("Logout")
if st.button("Logout"):
    logout()
    st.success("Logged out successfully!")
    sleep(0.5)
    st.switch_page("app.py")

st.divider()
# Delete Account Section
st.subheader("Delete Account")

confirmation = st.checkbox("I want to permanently delete my account")
if confirmation:
    if st.button("Delete Account"):
        delete_user(user_id)
        logout()
        st.success("Account deleted successfully!")
        sleep(0.5)
        st.switch_page("app.py")