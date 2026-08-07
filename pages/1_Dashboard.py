import streamlit as st

from operations import (
    get_user_by_id,
    get_user_workouts,
    get_latest_measurement,
    get_user_goals,
    get_personal_records,
    get_weekly_streak,
    get_workout_sets_by_workout_id,
    get_muscle_distribution
)

from analytics import (
    workout_frequency,
    weight_progress,
    training_volume,
    muscle_distribution
)

from ui.styles import load_css
from ui.components import (
    welcome_card,
    metric_card,
    section,
    chart_description
)

from ui.charts import (
    workout_frequency_chart,
    weight_progress_chart,
    training_volume_chart,
    muscle_distribution_chart
)


st.set_page_config(
    page_title="GymTic Dashboard",
    layout="wide"
)

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

streak = get_weekly_streak(user_id)


if user is None:
    st.error("User not found.")
    st.stop()


if measurement:
    current_weight = float(measurement["body_weight"])
else:
    current_weight = float(user["weight"])



col1, col2 = st.columns([4, 1])

with col1:
    st.markdown(
        f"## Welcome, {user['name']} 👋"
    )

    st.caption(
        "Here's how your training is going."
    )

with col2:
    st.markdown(
        f"### 🔥 {streak} weeks"
    )


col1, col2, col3, col4 = st.columns(4)

with col1:
    metric_card(
        "TOTAL WORKOUTS",
        len(workouts)
    )

with col2:
    metric_card(
        "CURRENT WEIGHT",
        f"{current_weight:.1f} kg"
    )

with col3:
    metric_card(
        "WEEK STREAK",
        f"{streak} weeks"
    )

with col4:
    metric_card(
        "PERSONAL RECORDS",
        len(records)
    )


section("Performance")



frequency_data = workout_frequency(workouts)
measurement_history = []

try:
    from operations import get_user_measurements

    measurement_history = get_user_measurements(user_id)

except Exception:
    measurement_history = []


weight_data = weight_progress(measurement_history)

all_sets = []

for workout in workouts:

    workout_sets = get_workout_sets_by_workout_id(
        workout["workout_id"]
    )

    all_sets.extend(workout_sets)


volume_data = training_volume(all_sets)

muscle_raw_data = get_muscle_distribution(user_id)

muscle_data = muscle_distribution(
    muscle_raw_data
)

chart_option = st.radio(
    "Analytics",
    [
        "Workout Frequency",
        "Weight Progression",
        "Training Volume",
        "Muscle Distribution"
    ],
    horizontal=True,
    label_visibility="collapsed"
)


if chart_option == "Workout Frequency":

    st.markdown(
        "### Workout Frequency"
    )

    chart_description(
        "Shows how consistently you train each week. "
        "Use it to monitor your training frequency and consistency."
    )

    workout_frequency_chart(
        frequency_data
    )


elif chart_option == "Weight Progression":

    st.markdown(
        "### Weight Progression"
    )

    chart_description(
        "Tracks your body weight over time so you can see "
        "whether you are moving toward your target weight."
    )

    weight_progress_chart(
        weight_data
    )


elif chart_option == "Training Volume":

    st.markdown(
        "### Training Volume"
    )

    chart_description(
        "Shows the total amount of work performed during your workouts "
        "using weight × reps."
    )

    training_volume_chart(
        volume_data
    )


elif chart_option == "Muscle Distribution":

    st.markdown(
        "### Muscle Distribution"
    )

    chart_description(
        "Shows how your training is distributed across muscle groups "
        "and helps identify muscles that may be receiving less attention."
    )

    muscle_distribution_chart(
        muscle_data
    )

st.divider()

section("Goal Progress")


if goals:

    goal = goals[0]

    target = float(goal["target_weight"])

    difference = current_weight - target

    if target > 0:

        progress = min(
            current_weight / target,
            1.0
        )

    else:

        progress = 0


    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Current Weight",
            f"{current_weight:.1f} kg"
        )

    with col2:

        st.metric(
            "Target Weight",
            f"{target:.1f} kg"
        )

    with col3:

        st.metric(
            "Remaining",
            f"{abs(difference):.1f} kg"
        )


    st.progress(
        progress
    )


else:

    st.info(
        "No goal has been set yet."
    )


st.divider()

section("Recent Activity")


if workouts:

    for workout in workouts[:5]:

        with st.container(border=True):

            col1, col2, col3 = st.columns(
                [2, 1, 1]
            )

            with col1:

                st.markdown(
                    f"**{workout['workout_type']} Workout**"
                )

            with col2:

                st.caption(
                    f"📅 {workout['date']}"
                )

            with col3:

                st.caption(
                    f"⏱️ {workout['duration']} min"
                )

else:

    st.info(
        "No workouts logged yet."
    )