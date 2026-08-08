import streamlit as st


def load_css():
    st.markdown("""
    <style>

    .stApp {
        background-color: #0B0D0F;
    }

    h1,
    h2,
    h3 {
        color: #FACC15 !important;
    }

    .metric-card {
        background: #121518;
        border: 1px solid #252A2F;
        padding: 20px;
        border-radius: 12px;
        min-height: 105px;
    }

    .metric-title {
        color: #FACC15 !important;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    .metric-value {
        color: #F8FAFC !important;
        font-size: 30px;
        font-weight: 700;
        margin-top: 8px;
    }

    .section-card {
        background: #121518;
        border: 1px solid #252A2F;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 25px;
    }

    .welcome-card {
        background: #121518;
        border: 1px solid #252A2F;
        color: #F8FAFC;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
    }

    .small-text {
        color: #CBD5E1 !important;
        font-size: 15px;
    }

    .dashboard-title {
        font-size: 32px;
        font-weight: 700;
        color: #FACC15 !important;
    }

    .dashboard-subtitle {
        font-size: 15px;
        color: #CBD5E1 !important;
        margin-top: 5px;
    }

    .streak-badge {
        background: #211F12;
        border: 1px solid #854D0E;
        color: #FACC15 !important;
        padding: 10px 16px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: 600;
        text-align: center;
    }

    div[data-testid="stRadio"] > div {
        background: #121518;
        border: 1px solid #252A2F;
        border-radius: 12px;
        padding: 6px;
    }

    div[data-testid="stRadio"] label {
        background: transparent;
        border-radius: 8px;
        padding: 9px 18px;
        color: #CBD5E1 !important;
    }

    div[data-testid="stRadio"] label:hover {
        background: #1C2126;
    }

    div[data-testid="stRadio"] label[data-checked="true"] {
        background: #A3E635;
        color: #0B0D0F !important;
    }

    .chart-description {
        color: #FACC15 !important;
        font-size: 14px;
        margin-top: -8px;
        margin-bottom: 12px;
    }

    [data-testid="stMarkdownContainer"] h2 {
        color: #FACC15 !important;
    }

    [data-testid="stVerticalBlock"] strong {
        color: #FACC15 !important;
    }

    [data-testid="stCaptionContainer"] {
        color: #CBD5E1 !important;
    }

    [data-testid="stMetricLabel"] {
        color: #FACC15 !important;
    }

    [data-testid="stMetricValue"] {
        color: #F8FAFC !important;
    }

    [data-testid="stMetricDelta"] {
        color: #CBD5E1 !important;
    }

    [data-testid="stMarkdownContainer"] p {
        color: #E2E8F0 !important;
    }

    [data-testid="stText"] {
        color: #FFFFFF !important;
    }

    section[data-testid="stSidebar"] {
        background: #101316;
    }

    div[data-testid="stTextInput"] label,
    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label {
        color: #FACC15 !important;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        background-color: #121518 !important;
        color: #F8FAFC !important;
        border: 1px solid #252A2F !important;
        border-radius: 8px !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        background-color: #121518 !important;
        color: #F8FAFC !important;
        border-color: #252A2F !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] span {
        color: #F8FAFC !important;
    }

    div[data-baseweb="popover"] {
        background-color: #121518 !important;
    }

    ul[data-baseweb="menu"] {
        background-color: #121518 !important;
        border: 1px solid #252A2F !important;
    }

    li[role="option"] {
        background-color: #121518 !important;
        color: #F8FAFC !important;
    }

    li[role="option"]:hover {
        background-color: #1C2126 !important;
        color: #FACC15 !important;
    }

    li[role="option"][aria-selected="true"] {
        background-color: #211F12 !important;
        color: #FACC15 !important;
    }

    .stButton > button {
        background-color: #FACC15 !important;
        color: #0B0D0F !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        min-height: 45px;
    }

    .stButton > button p,
    .stButton > button span,
    .stButton > button div {
        color: #0B0D0F !important;
        font-weight: 700 !important;
    }

    .stButton > button:hover {
        background-color: #EAB308 !important;
        color: #0B0D0F !important;
    }

    div[data-testid="stCheckbox"] label {
        color: #CBD5E1 !important;
    }

    div[data-testid="stCheckbox"] label span {
        color: #CBD5E1 !important;
    }

    </style>
    """, unsafe_allow_html=True)