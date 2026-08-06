import streamlit as st


def load_css():
    st.markdown("""
    <style>

    .stApp{
        background-color:#F5F7FA;
    }

    h1,h2,h3{
        color:#1E293B;
    }

    .metric-card{
        background:white;
        padding:20px;
        border-radius:18px;
        box-shadow:0px 4px 15px rgba(0,0,0,.08);
        text-align:center;
        margin-bottom:15px;
    }

    .metric-title{
        color:#64748B;
        font-size:15px;
    }

    .metric-value{
        font-size:34px;
        font-weight:700;
        color:#2563EB;
    }

    .section-card{
        background:white;
        padding:22px;
        border-radius:18px;
        box-shadow:0px 4px 15px rgba(0,0,0,.08);
        margin-bottom:25px;
    }

    .welcome-card{

        background:linear-gradient(135deg,#2563EB,#1D4ED8);

        color:white;

        padding:35px;

        border-radius:20px;

        margin-bottom:30px;
    }

    .small-text{

        color:#CBD5E1;

        font-size:15px;

    }

    </style>

    """, unsafe_allow_html=True)