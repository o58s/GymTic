import streamlit as st


def metric_card(title, value):

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def welcome_card(name):

    html = f"""
    <div class="welcome-card">
        <h2>Welcome, {name} 👋</h2>
        <p class="small-text">
            Track your progress. Stay consistent. Every workout counts.
        </p>
    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True
    )


def section(title):

    st.markdown(
        f"""
        <h3>{title}</h3>
        """,
        unsafe_allow_html=True
    )

def chart_description(text):

    st.info(text)