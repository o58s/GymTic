import streamlit as st 

st.set_page_config(
    page_title="GymTic Dashboard",
    layout="wide"
)

#Title
st.title("GymTic")

st.subheader("Personal Fitness Analytics Platform")
st.write(
    "Track your workouts, monitor your progress, "
    "and analyze your performance."
)


#Dashboard Section
st.divider()

st.header('Overview')
st.write("Workout statistics will appear here.")

st.header("Recent Activity")
st.write("Your latest workouts will appear here.")

st.header("Quick Actions")
st.write("Workout logging and measurement actions will appear here.")

