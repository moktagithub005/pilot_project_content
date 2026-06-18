import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Why Do Graphs Exist?")

st.header("🤔 Can Your Brain Understand Raw Numbers?")

st.write(
    """
Imagine you are the Principal of a school.

You receive marks of students like this:
"""
)

marks = [
    45, 67, 89, 34, 76,
    54, 91, 82, 73, 65,
    88, 92, 40, 58, 71,
    69, 77, 84, 60, 95
]

st.code(marks)

st.divider()

st.subheader("🕵️ Detective Challenge")

st.write(
    """
Without calculating:

Can you answer these questions?
"""
)

st.write("1. What mark appears most often?")
st.write("2. Are most students scoring above 70?")
st.write("3. Is the class performing well?")

st.warning(
    """
Difficult, right?

Your brain is looking at numbers one by one.
"""
)

st.divider()

show_graph = st.button("📈 Convert Data Into Graph")

if show_graph:

    df = pd.DataFrame({
        "Student": [f"S{i}" for i in range(1, 21)],
        "Marks": marks
    })

    fig = px.bar(
        df,
        x="Student",
        y="Marks",
        title="Marks of Students"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success(
        """
Now your brain can instantly see:

✔ High scorers

✔ Low scorers

✔ Overall pattern

This is why graphs exist.
"""
    )

st.divider()

st.header("🎮 Make Your Own Class Data")

cricket = st.slider("Students who like Cricket", 0, 50, 20)
football = st.slider("Students who like Football", 0, 50, 10)
basketball = st.slider("Students who like Basketball", 0, 50, 5)

sports_df = pd.DataFrame({
    "Sport": ["Cricket", "Football", "Basketball"],
    "Students": [cricket, football, basketball]
})

fig2 = px.bar(
    sports_df,
    x="Sport",
    y="Students",
    title="Favourite Sports"
)

st.plotly_chart(fig2, use_container_width=True)



st.divider()

st.header("🧠 Human Brain Experiment")

st.write(
    """
Which is easier?

Option A:
"""
)

st.code("""
12
45
67
89
23
56
78
""")

st.write("Option B: A graph of the same values")

small_df = pd.DataFrame({
    "Value": [12, 45, 67, 89, 23, 56, 78]
})

fig3 = px.bar(
    small_df,
    y="Value"
)

st.plotly_chart(fig3, use_container_width=True)

st.info(
    """
Your brain naturally prefers visuals.

That is why charts are powerful.
"""
)