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
        title= "Weekly Workout Frequency",
        labels={
            "week": "Week",
            "workouts": "Workouts"
        }
    )

    fig.update_layout(
        height = 350,
        template = "plotly_white",  
        paper_bgcolor= 'rgba(0,0,0,0)',
        plot_bgcolor= 'rgba(0,0,0,0)',
        font=dict(color='#E2E8F0'),
        xaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
        yaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
    )
    fig.update_traces(
        marker_color='#FACC15'     
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
            "body_weight": "Weight(kg)"
        }
    )

    fig.update_layout(
        height=350,
        template="plotly_white",
        paper_bgcolor= 'rgba(0,0,0,0)',
        plot_bgcolor= 'rgba(0,0,0,0)',
        font=dict(color='#E2E8F0'),
        xaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
        yaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
    )
    fig.update_traces(
        line_color='#FACC15',  
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
        title="Muscle Group Distribution",
        hole=0.4
    )

    fig.update_layout(
        height=350,
        template="plotly_white",
        paper_bgcolor= 'rgba(0,0,0,0)',
        plot_bgcolor= 'rgba(0,0,0,0)',
        font=dict(color='#E2E8F0'),
        xaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
        yaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
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
        paper_bgcolor= 'rgba(0,0,0,0)',
        plot_bgcolor= 'rgba(0,0,0,0)',
        font=dict(color='#E2E8F0'),
        xaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
        yaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
    )
    fig.update_traces(
        line_color='#FACC15',   
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
        paper_bgcolor= 'rgba(0,0,0,0)',
        plot_bgcolor= 'rgba(0,0,0,0)',
        font=dict(color='#E2E8F0'),
        xaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
        yaxis=dict(color='#E2E8F0', gridcolor='#252A2F'),
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )