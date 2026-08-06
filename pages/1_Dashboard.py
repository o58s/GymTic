import streamlit as st

from operations import get_user_by_id, get_user_workouts, get_latest_measurement, get_user_goals, get_personal_records, get_weekly_streak

from ui.styles import load_css
from ui.components import welcome_card, metric_card, section

load_css()

if "user_id" not in st.session_state:
    st.warning("Please log in first.")
    st.stop()

user_id = st.session_state.user_id

user = get_user_by_id(user_id)
workouts = get_user_workouts(user_id)
measurement = get_latest_measurement(user_id)
goals = get_user_goals(user_id)
records = get_personal_records(user_id)

welcome_card(user["name"])


if measurement:
    current_weight = measurement["body_weight"]
else:
    current_weight = user["weight"]

col1, col2 = st.columns(2)

with col1:
    metric_card(
        "Total Workouts",
        len(workouts)
    )

with col2:
    metric_card(
        "Current Weight",
        f"{current_weight} kg"
    )

col3, col4 = st.columns(2)

streak = get_weekly_streak(user_id)

with col3:
    metric_card(
        "🔥 Week Streak",
        f"{streak} weeks"
    )

with col4:
    metric_card(
        "Personal Records",
        len(records)
    )

st.divider()

section("🔥 Recent Activity")

if workouts:

    for workout in workouts[:5]:

        with st.container(border=True):

            st.markdown(
                f"""
                **{workout['workout_type']} Workout**

                📅 {workout['date']}

                ⏱️ Duration: {workout['duration']} minutes
                """
            )

else:

    st.info("No workouts logged yet. Start your first workout!")

st.divider()

section("Goal Progress")

if goals:

    goal = goals[0]

    target = float(goal["target_weight"])

    current = float(current_weight)

    st.write(f"**Current Weight:** {current:.1f} kg")
    st.write(f"**Target Weight:** {target:.1f} kg")

    difference = current - target

    st.write(f"**Remaining:** {difference:.1f} kg")

    progress = min(current / target, 1.0)

    st.progress(progress)

else:

    st.info("No goal has been set yet.")


st.divider()

section("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏋️ Log Workout", use_container_width=True):
        st.switch_page("pages/2_Workout.py")

with col2:
    if st.button("📈 Progress", use_container_width=True):
        st.switch_page("pages/3_Progress.py")

with col3:
    if st.button("👤 Profile", use_container_width=True):
        st.switch_page("pages/4_Profile.py")