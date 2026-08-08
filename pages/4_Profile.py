import streamlit as st
from operations import get_user_by_id, update_user, delete_user
from auth import logout
from time import sleep
from ui.styles import load_css
from ui.components import section, metric_card

st.set_page_config(
    page_title="GymTic Profile",
    layout="wide"
)

load_css()

if "user_id" not in st.session_state:
    st.warning("You need to log in to access your profile.")
    st.stop()

user_id = st.session_state.user_id

user = get_user_by_id(user_id)

if user is None:
    st.error("User not found.")
    st.stop()

st.markdown(
    """
    <div class="dashboard-title">
        Your Profile
    </div>
    <div class="dashboard-subtitle">
        Manage your personal information and account settings.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card(
        "NAME",
        user["name"]
    )

with col2:
    metric_card(
        "AGE",
        f"{user['age']} years"
    )

with col3:
    metric_card(
        "HEIGHT",
        f"{float(user['height']):.1f} cm"
    )

with col4:
    metric_card(
        "WEIGHT",
        f"{float(user['weight']):.1f} kg"
    )

st.divider()

section("Personal Information")

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Name",
            value=user["name"]
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=int(user["age"])
        )

        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            max_value=250.0,
            value=float(user["height"]),
            step=0.5
        )

    with col2:

        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=300.0,
            value=float(user["weight"]),
            step=0.5
        )

        goals = [
            "Strength",
            "Hypertrophy",
            "Fat Loss"
        ]

        goal = st.selectbox(
            "Goal",
            goals,
            index=goals.index(user["goal"])
        )

    st.write("")

    if st.button(
        "Save Changes",
        use_container_width=True
    ):

        update_user(
            user_id,
            name,
            age,
            height,
            weight,
            goal
        )

        st.success("Profile updated successfully!")

        sleep(0.5)

        st.rerun()

st.divider()

section("Account")

with st.container(border=True):

    st.markdown(
        "**ACCOUNT**"
    )

    st.write(
        f"Username: **{user['username']}**"
    )

    st.caption(
        "This is your GymTic account."
    )

    if st.button(
        "Logout",
        use_container_width=True
    ):

        logout()

        sleep(0.5)

        st.switch_page("app.py")

st.divider()

section("Danger Zone")

with st.container(border=True):

    st.markdown(
        "**DELETE ACCOUNT**"
    )

    st.caption(
        "Permanently delete your GymTic account and all associated data."
    )

    confirmation = st.checkbox(
        "I understand that this action cannot be undone."
    )

    if confirmation:

        if st.button(
            "Delete Account",
            use_container_width=True
        ):

            delete_user(user_id)

            logout()

            st.success("Account deleted successfully!")

            sleep(0.5)

            st.switch_page("app.py")