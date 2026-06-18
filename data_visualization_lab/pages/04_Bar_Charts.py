import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 The King of Comparison: Bar Charts")

st.header("🏏 Favourite Sports Survey")

st.write(
    """
Suppose we surveyed students and asked:

'Which sport do you like the most?'
"""
)

cricket = st.slider("Cricket", 0, 50, 25)
football = st.slider("Football", 0, 50, 15)
basketball = st.slider("Basketball", 0, 50, 10)
volleyball = st.slider("Volleyball", 0, 50, 5)

df = pd.DataFrame({
    "Sport": [
        "Cricket",
        "Football",
        "Basketball",
        "Volleyball"
    ],
    "Students": [
        cricket,
        football,
        basketball,
        volleyball
    ]
})

fig = px.bar(
    df,
    x="Sport",
    y="Students",
    title="Favourite Sports of Students"
)

st.plotly_chart(fig, use_container_width=True)


st.divider()

st.header("🤔 Why Are There Spaces Between Bars?")

st.write(
    """
Look carefully.

Why do bars have gaps between them?
"""
)

answer = st.radio(
    "Choose your answer:",
    [
        "To make graph beautiful",
        "Because categories are separate things",
        "No reason"
    ]
)

if answer == "Because categories are separate things":
    st.success(
        """
Correct!

Cricket is different from Football.

Football is different from Basketball.

The gaps remind us that these are separate categories.
"""
    )

st.divider()

st.header("🎮 Which Data Should Use A Bar Chart?")

choice = st.selectbox(
    "Choose a dataset",
    [
        "Favourite Sport",
        "Favourite Subject",
        "Student Heights",
        "Daily Temperature"
    ]
)

if choice in ["Favourite Sport", "Favourite Subject"]:
    st.success(
        """
Excellent!

Bar Charts are perfect because these are categories.
"""
    )

else:
    st.warning(
        """
Not the best choice.

These are continuous measurements.
"""
    )

st.divider()

st.header("🔍 Anatomy of a Bar Chart")

st.image(
    "https://dummyimage.com/800x400/cccccc/000000&text=Bar+Chart+Components"
)

st.write(
    """
Every good bar chart needs:

1. Title
2. X Axis
3. Y Axis
4. Bars
5. Labels
"""
)

st.divider()

st.header("🕵️ Data Detective Challenge")

questions = [
    "What are the categories?",
    "What do the numbers mean?",
    "Which bar is highest?",
    "Which bar is lowest?",
    "What story is this graph telling?"
]

for q in questions:
    st.write("✅", q)

st.divider()

st.header("🎨 Create Your Own Bar Chart")

category1 = st.text_input("Category 1", "Apple")
category2 = st.text_input("Category 2", "Mango")
category3 = st.text_input("Category 3", "Banana")

value1 = st.slider("Value 1", 0, 100, 50)
value2 = st.slider("Value 2", 0, 100, 30)
value3 = st.slider("Value 3", 0, 100, 20)

custom_df = pd.DataFrame({
    "Category": [
        category1,
        category2,
        category3
    ],
    "Value": [
        value1,
        value2,
        value3
    ]
})

custom_fig = px.bar(
    custom_df,
    x="Category",
    y="Value",
    title="My First Bar Chart"
)

st.plotly_chart(custom_fig, use_container_width=True)

st.divider()

st.header("📐 Vertical vs Horizontal Bar Charts")

st.write(
    """
Vertical bar charts are the classic choice when categories are short and easy to read on the x-axis.
Horizontal bar charts are better when category labels are long or there are many categories.
"""
)

orientation_df = pd.DataFrame({
    "Fruit": [
        category1,
        category2,
        category3
    ],
    "Count": [
        value1,
        value2,
        value3
    ]
})

vertical_fig = px.bar(
    orientation_df,
    x="Fruit",
    y="Count",
    title="Vertical Bar Chart"
)

horizontal_fig = px.bar(
    orientation_df,
    x="Count",
    y="Fruit",
    orientation="h",
    title="Horizontal Bar Chart"
)

st.plotly_chart(vertical_fig, use_container_width=True)
st.plotly_chart(horizontal_fig, use_container_width=True)

st.divider()

st.header("📚 Stacked Bar Charts")

stacked_df = pd.DataFrame({
    "Subject": ["Math", "Science", "Art"],
    "Boys": [40, 30, 20],
    "Girls": [35, 25, 30]
})

stacked_fig = px.bar(
    stacked_df,
    x="Subject",
    y=["Boys", "Girls"],
    title="Stacked Bar Chart",
    labels={"value": "Students", "variable": "Group"},
    barmode="stack"
)

percent_df = stacked_df.copy()
percent_df["Total"] = percent_df["Boys"] + percent_df["Girls"]
percent_df["Boys"] = percent_df["Boys"] / percent_df["Total"] * 100
percent_df["Girls"] = percent_df["Girls"] / percent_df["Total"] * 100

percent_fig = px.bar(
    percent_df,
    x="Subject",
    y=["Boys", "Girls"],
    title="100% Stacked Bar Chart",
    labels={"value": "Percent", "variable": "Group"},
    barmode="stack"
)

st.write(
    """
Stacked bar charts show how multiple groups contribute to the total for each category.
100% stacked bars normalize each category to the same height so you can compare the share of each group.
"""
)

st.plotly_chart(stacked_fig, use_container_width=True)
st.plotly_chart(percent_fig, use_container_width=True)

st.write(
    """
Why use these charts?

- Vertical bar charts are great for comparing category sizes.
- Horizontal bar charts are easier to read for long labels.
- Stacked bar charts help compare parts of a whole across categories.
- 100% stacked bar charts show the composition of each category in percentages.
"""
)