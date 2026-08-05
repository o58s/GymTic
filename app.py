import streamlit as st
from auth import Create_account, login

st.set_page_config(
    page_title="GymTic",
    layout="centered"
)

if "user_id" in st.session_state:
    st.success(f"Welcome back, {st.session_state.name}!")
    st.write("You are already logged in.")
    st.stop()

st.title("Gymtic")

option = st.selectbox(
    "Select an option",
    [
        "Login",
        "Create Account"
    ]
)

if option == "login":
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    success, message = login(username, password)

    if success:
        st.success(message)
        st.rerun()
    else:
        st.error(message)

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

        success, result = create_account(
            username,
            password,
            name,
            age,
            height,
            weight,
            goal
        )


        if success:
            st.success(
                f"Account created! User ID: {result}"
            )

        else:
            st.error(result)