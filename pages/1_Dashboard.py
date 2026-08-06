import streamlit as st
from operations import get_user_by_id, get_user_workouts, get_latest_measurement, get_user_goals, get_personal_records

if "user_id" not in st.session_state:
    st.warning("You need to log in to access the dashboard.")
    st.stop()

user_id = st.session_state.user_id

user = get_user_by_id(user_id)
workouts = get_user_workouts(user_id)
measurements = get_latest_measurement(user_id)
goals = get_user_goals(user_id)
records = get_personal_records(user_id)

st.title("GymTic")

st.write(f"### Welcome, {user['name']}!")   
st.caption("Track your progress. Stay consistent")

st.divider()


col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Workouts",
        len(workouts)
    )

with col2:
    if measurements:
        current_weight = measurements["body_weight"]
    else:
        current_weight = user["weight"]

    st.metric(
        "Current Weight",
        f"{current_weight} kg"
    )

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "Current Goal",
        user["goal"]
    )

with col4:
    st.metric(
        "Personal Record",
        len(records)
    )

st.divider()

st.subheader("Recent Activity")

if workouts:
    for workout in workouts:
        st.write(f"{workout['date']} - {workout['workout_type']}")

else:
    st.info("No workouts logged yet. Start your first workout")

st.divider()

st.subheader('Goal Progress')

if goals:
    goal = goals[0]
    st.write(f"Target Weight: {goal['target_weight']} kg")

    if measurements:
        remaining = float(measurements["body_weight"] - float(goal['target_weight']))
        st.write(f"Remaining: {remaining:.1f} kg")

else:
    st.info("No goal has been set yet.")

st.divider()

st.subheader("Quick Action")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Log Workout"):
        st.switch_page("pages/2_Workout.py")

with col2:
    if st.button("Progress"):
        st.switch_page("pages/3_Progress.py")

with col3:
    if st.button("Profile"):
        st.switch_page("pages/4_Profile.py")
