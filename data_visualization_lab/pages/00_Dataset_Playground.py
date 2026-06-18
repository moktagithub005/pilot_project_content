import streamlit as st
import pandas as pd
import numpy as np

st.title("📚 Dataset Playground")

st.header("Where Do Graphs Come From?")

st.write(
    """
Before creating graphs,
we need data.

A collection of data arranged in rows and columns
is called a Dataset.
"""
)

num_students = st.slider(
    "Number of Students",
    10,
    100,
    30
)

names = [
    f"Student_{i}"
    for i in range(1, num_students + 1)
]

sports = np.random.choice(
    [
        "Cricket",
        "Football",
        "Basketball",
        "Badminton"
    ],
    num_students
)

subjects = np.random.choice(
    [
        "Maths",
        "Science",
        "English",
        "Computer"
    ],
    num_students
)

heights = np.random.normal(
    160,
    8,
    num_students
).round(1)

study_hours = np.random.randint(
    1,
    8,
    num_students
)

df = pd.DataFrame({
    "Name": names,
    "Favourite Sport": sports,
    "Favourite Subject": subjects,
    "Height (cm)": heights,
    "Study Hours": study_hours
})

st.subheader("🏫 Student Dataset")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

st.header("🔍 Explore Columns")

column = st.selectbox(
    "Choose a Column",
    df.columns
)

st.write(df[column])

st.divider()

st.header("🎮 Data Detective")

choice = st.selectbox(
    "Select a Column",
    [
        "Favourite Sport",
        "Favourite Subject",
        "Height (cm)",
        "Study Hours"
    ]
)

if choice in [
    "Favourite Sport",
    "Favourite Subject"
]:
    st.success(
        """
Categorical Data

These are labels or names.
"""
    )
else:
    st.success(
        """
Numerical Data

These are measurements or counts.
"""
    )

st.divider()

st.header("📊 Quick Summary")

st.write(
    "Average Height:",
    round(
        df["Height (cm)"].mean(),
        2
    )
)

st.write(
    "Average Study Hours:",
    round(
        df["Study Hours"].mean(),
        2
    )
)

st.divider()

st.header("💾 Save Dataset")

if st.button("Generate New Dataset"):

    df.to_csv(
        "student_dataset.csv",
        index=False
    )

    st.success(
        "Dataset Saved!"
    )