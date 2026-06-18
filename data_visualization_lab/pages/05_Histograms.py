import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📊 Histograms & Continuous Data")

st.header("🌊 The River of Numbers")

st.write(
    """
Some data comes in separate categories.

Some data flows continuously.

Let's discover the difference.
"""
)

question = st.radio(
    "Choose a dataset:",
    [
        "Favourite Sport",
        "Student Heights"
    ]
)

if question == "Favourite Sport":

    st.success(
        """
Cricket
Football
Basketball

These are categories.
"""
    )

else:

    st.success(
        """
150 cm
150.5 cm
151 cm
151.2 cm

These are measurements.
"""
    )

st.divider()

st.header("🏫 Heights of Students")

num_students = st.slider(
    "Number of Students",
    20,
    300,
    100,
    key="num_students_height"
)

heights = np.random.normal(
    160,
    8,
    num_students
)

df = pd.DataFrame({
    "Height": heights
})

st.write(df.head())

fig = px.histogram(
    df,
    x="Height",
    nbins=15,
    title="Distribution of Student Heights"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.header("🎮 Change The Histogram")

spread = st.slider(
    "Variation in Heights",
    1,
    30,
    8
)

heights2 = np.random.normal(
    160,
    spread,
    200
)

df2 = pd.DataFrame({
    "Height": heights2
})

fig2 = px.histogram(
    df2,
    x="Height",
    nbins=15,
    title="What Happens When Variation Changes?"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

st.header("⚔️ Bar Chart vs Histogram")

comparison = pd.DataFrame({
    "Bar Chart": [
        "Categories",
        "Bars have gaps",
        "Compare groups",
        "Sports, Subjects"
    ],
    "Histogram": [
        "Measurements",
        "Bars touch",
        "Show distribution",
        "Height, Weight"
    ]
})

st.table(comparison)

st.divider()

st.header("🕵️ Data Detective Quiz")

dataset = st.selectbox(
    "Choose Dataset",
    [
        "Favourite Sport",
        "Country",
        "Height",
        "Weight",
        "Temperature"
    ]
)

if dataset in ["Favourite Sport", "Country"]:
    st.success(
        "Use a Bar Chart ✅"
    )

else:
    st.success(
        "Use a Histogram ✅"
    )

