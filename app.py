import streamlit as st
from auth import create_account, login
from time import sleep
from ui.styles import load_css

st.set_page_config(
    page_title="GymTic",
    layout="centered"
)

load_css()

# Extra styling scoped to the login/signup screen
st.markdown(
    """
    <style>

    .login-hero {
        text-align: center;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    .login-hero .logo {
        font-size: 42px;
        font-weight: 800;
        color: #FACC15 !important;
        letter-spacing: 1px;
    }

    .login-hero .tagline {
        color: #CBD5E1 !important;
        font-size: 15px;
        margin-top: 4px;
    }

    .auth-card {
        background: #121518;
        border: 1px solid #252A2F;
        border-radius: 14px;
        padding: 30px 30px 15px 30px;
        margin-bottom: 25px;
    }

    div[data-baseweb="tab-list"] {
        background: #0B0D0F;
        border: 1px solid #252A2F;
        border-radius: 10px;
        padding: 4px;
        gap: 4px;
    }

    button[data-baseweb="tab"] {
        color: #CBD5E1 !important;
        border-radius: 8px !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: #FACC15 !important;
        color: #0B0D0F !important;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        background-color: #0B0D0F;
        color: #F8FAFC;
        border: 1px solid #252A2F;
        border-radius: 8px;
    }

    /* Selectbox closed/collapsed value */
    div[data-testid="stSelectbox"] > div {
        background-color: #0B0D0F;
        border-radius: 8px;
    }

    div[data-baseweb="select"] > div {
        background-color: #0B0D0F !important;
        border-color: #252A2F !important;
        color: #F8FAFC !important;
    }

    div[data-baseweb="select"] * {
        color: #F8FAFC !important;
    }

    /* Selectbox dropdown popover (rendered outside the widget, so these
       selectors are intentionally global rather than scoped) */
    ul[data-baseweb="menu"],
    div[data-baseweb="popover"] ul {
        background-color: #121518 !important;
        border: 1px solid #252A2F !important;
    }

    li[role="option"] {
        background-color: #121518 !important;
        color: #F8FAFC !important;
    }

    li[role="option"]:hover,
    li[aria-selected="true"] {
        background-color: #1C2126 !important;
        color: #FACC15 !important;
    }

    /* Password show/hide eye icon - default renders white-on-white and is
       invisible, force a clearly visible color on every possible target
       (button, svg, and the path/stroke inside the svg) */
    button[title="Show password text"],
    button[title="Hide password text"],
    button[aria-label="Show password text"],
    button[aria-label="Hide password text"],
    div[data-testid="stTextInput"] button,
    div[data-testid="stTextInputRootElement"] button,
    div[data-testid="stTextInputRootElement"] > div > button {
        background: transparent !important;
        color: #FACC15 !important;
        opacity: 1 !important;
    }

    button[title="Show password text"] svg,
    button[title="Hide password text"] svg,
    button[aria-label="Show password text"] svg,
    button[aria-label="Hide password text"] svg,
    div[data-testid="stTextInput"] button svg,
    div[data-testid="stTextInputRootElement"] button svg {
        fill: #FACC15 !important;
        stroke: #FACC15 !important;
        color: #FACC15 !important;
        opacity: 1 !important;
    }

    button[title="Show password text"] svg path,
    button[title="Hide password text"] svg path,
    button[aria-label="Show password text"] svg path,
    button[aria-label="Hide password text"] svg path,
    div[data-testid="stTextInput"] button svg path,
    div[data-testid="stTextInputRootElement"] button svg path {
        fill: #FACC15 !important;
        stroke: #FACC15 !important;
    }

    .stButton > button {
        background: #FACC15;
        color: #0B0D0F !important;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        font-size: 17px;
        width: 100%;
        height: auto;
        min-height: 48px;
        padding: 12px 16px;
        margin-top: 10px;
        line-height: 1.3;
        white-space: normal;
    }

    .stButton > button p,
    .stButton > button div,
    .stButton > button span {
        color: #0B0D0F !important;
        font-weight: 700;
        font-size: 17px;
    }

    .stButton > button:hover {
        background: #EAB308;
        color: #0B0D0F !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Check if already logged in
if "user_id" in st.session_state:
    st.switch_page("pages/1_Dashboard.py")


st.markdown(
    """
    <div class="login-hero">
        <div class="logo">GymTic</div>
        <div class="tagline">Track your progress. Stay consistent. Every workout counts.</div>
    </div>
    """,
    unsafe_allow_html=True
)


tab_login, tab_signup = st.tabs(["Login", "Create Account"])


# Login Section

with tab_login:

    st.markdown('<div class="auth-card">', unsafe_allow_html=True)

    st.subheader("Welcome back")

    username = st.text_input("Username", key="login_username")

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login", key="login_button"):

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

    st.markdown('</div>', unsafe_allow_html=True)


# Create Account Section

with tab_signup:

    st.markdown('<div class="auth-card">', unsafe_allow_html=True)

    st.subheader("Create your account")

    username = st.text_input("Username", key="signup_username")

    password = st.text_input(
        "Password",
        type="password",
        key="signup_password"
    )

    name = st.text_input("Name", key="signup_name")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            key="signup_age"
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=300.0,
            key="signup_weight"
        )

    with col2:
        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            max_value=250.0,
            key="signup_height"
        )

        goal = st.selectbox(
            "Goal",
            [
                "Strength",
                "Hypertrophy",
                "Fat Loss"
            ],
            key="signup_goal"
        )

    if st.button("Create Account", key="signup_button"):

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

    st.markdown('</div>', unsafe_allow_html=True)