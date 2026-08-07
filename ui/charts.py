import plotly.express as px
import streamlit as st


def workout_frequency_chart(data):
    if data is None or data.empty:
        st.info("Not enough workout data yet.")
        return

    fig = px.bar(
        data,
        x="week",
        y="workouts",
        title="Weekly Workout Frequency",
        labels={
            "week": "Week",
            "workouts": "Workouts"
        }
    )

    fig.update_layout(
        height=350,
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FFFFFF"),
        title_font=dict(color="#FFFFFF"),
        xaxis=dict(
            color="#FFFFFF",
            gridcolor="#252A2F",
            tickfont=dict(color="#FFFFFF"),
            title_font=dict(color="#FFFFFF")
        ),
        yaxis=dict(
            color="#FFFFFF",
            gridcolor="#252A2F",
            tickfont=dict(color="#FFFFFF"),
            title_font=dict(color="#FFFFFF")
        )
    )

    fig.update_traces(
        marker_color="#FACC15"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def weight_progress_chart(data):
    if data is None or data.empty:
        st.info("No weight measurements available.")
        return

    fig = px.line(
        data,
        x="date",
        y="body_weight",
        markers=True,
        title="Weight Progression",
        labels={
            "date": "Date",
            "body_weight": "Weight (kg)"
        }
    )

    fig.update_layout(
        height=350,
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FFFFFF"),
        title_font=dict(color="#FFFFFF"),
        xaxis=dict(
            color="#FFFFFF",
            gridcolor="#252A2F",
            tickfont=dict(color="#FFFFFF"),
            title_font=dict(color="#FFFFFF")
        ),
        yaxis=dict(
            color="#FFFFFF",
            gridcolor="#252A2F",
            tickfont=dict(color="#FFFFFF"),
            title_font=dict(color="#FFFFFF")
        )
    )

    fig.update_traces(
        line_color="#FACC15",
        marker_color="#FACC15"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def training_volume_chart(data):
    if data is None or data.empty:
        st.info("No training volume data available.")
        return

    fig = px.line(
        data,
        x="workout_id",
        y="volume",
        markers=True,
        title="Training Volume Progress",
        labels={
            "workout_id": "Workout",
            "volume": "Volume (kg)"
        }
    )

    fig.update_layout(
        height=350,
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FFFFFF"),
        title_font=dict(color="#FFFFFF"),
        xaxis=dict(
            color="#FFFFFF",
            gridcolor="#252A2F",
            tickfont=dict(color="#FFFFFF"),
            title_font=dict(color="#FFFFFF")
        ),
        yaxis=dict(
            color="#FFFFFF",
            gridcolor="#252A2F",
            tickfont=dict(color="#FFFFFF"),
            title_font=dict(color="#FFFFFF")
        )
    )

    fig.update_traces(
        line_color="#FACC15",
        marker_color="#FACC15"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def muscle_distribution_chart(data):
    if data is None or data.empty:
        st.info("No muscle data available.")
        return

    fig = px.pie(
        data,
        names="muscle_group_name",
        values="count",
        hole=0.45,
        title="Muscle Group Distribution"
    )

    fig.update_layout(
        height=500,
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#FFFFFF"),
        title_font=dict(color="#FFFFFF"),
        legend=dict(
            font=dict(color="#FFFFFF")
        )
    )

    fig.update_traces(
        textposition="outside",
        textfont=dict(
            color="#FFFFFF",
            size=14
        ),
        marker=dict(
            line=dict(
                color="#0B0D0F",
                width=2
            )
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )