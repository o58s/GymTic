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

    p,
    span,
    label,
    div {
        color: #E2E8F0;
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
        color: #E2E8F0 !important;
    }

    section[data-testid="stSidebar"] {
        background: #101316;
    }

    </style>
    """, unsafe_allow_html=True)