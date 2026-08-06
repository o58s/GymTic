import streamlit as st
from auth import create_account, login
from time import sleep

st.set_page_config(
    page_title="GymTic",
    layout="centered"
)


#Check if already logged in
if "user_id" in st.session_state:

    st.switch_page("pages/1_Dashboard.py")


st.title("GymTic")


option = st.selectbox(
    "Select an option",
    [
        "Login",
        "Create Account"
    ]
)


#Login Section

if option == "Login":

    st.subheader("Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        success, message = login(
            username,
            password
        )

        if success:
            st.success(message)
            sleep(0.5)
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error(message)


# Create Account Section

else:

    st.subheader("Create Account")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )

    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=300.0
    )

    goal = st.selectbox(
        "Goal",
        [
            "Strength",
            "Hypertrophy",
            "Fat Loss"
        ]
    )

    if st.button("Create Account"):

        success, message = create_account(
            username,
            password,
            name,
            age,
            height,
            weight,
            goal
        )

        if success:
            st.success(message)
            sleep(0.5)
            st.switch_page("pages/1_Dashboard.py")

        else:
            st.error(message)