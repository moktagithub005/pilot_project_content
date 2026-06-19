import streamlit as st
import pandas as pd

try:
    import plotly.express as px
except ImportError:
    px = None

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.title("🥧 Pie Charts: Understanding Parts of a Whole")

st.markdown("""
# 🍕 The Pizza Story

Imagine a pizza cut into slices.

If you eat 4 slices out of 8 slices,
you have eaten **50%** of the pizza.

Pie Charts work exactly the same way.

A Pie Chart shows:

### Parts of a Whole
""")

st.divider()

# ---------------------------------------------------
# Interactive Example
# ---------------------------------------------------

st.header("🎮 Build Your Own Pie Chart")

youtube = st.slider(
    "YouTube Hours",
    0,
    10,
    5,
    key="youtube_hours"
)

instagram = st.slider(
    "Instagram Hours",
    0,
    10,
    3,
    key="instagram_hours"
)

gaming = st.slider(
    "Gaming Hours",
    0,
    10,
    2,
    key="gaming_hours"
)

total_hours = youtube + instagram + gaming

if total_hours == 0:
    st.warning("Please choose at least one activity.")
else:

    df = pd.DataFrame({
        "Activity": [
            "YouTube",
            "Instagram",
            "Gaming"
        ],
        "Hours": [
            youtube,
            instagram,
            gaming
        ]
    })

    if px is None:
        st.warning("Plotly is not installed. Install it with `pip install plotly` to view the pie chart.")
    else:
        fig = px.pie(
            df,
            names="Activity",
            values="Hours",
            title="Daily Screen Time Breakdown"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
st.header("🤔 Why Do Pie Charts Exist?")

st.info("""
Bar Charts help us compare categories.

Pie Charts help us understand:

'How much of the whole belongs to each category?'
""")

st.markdown("""
### Example

Suppose your daily screen time is:

- YouTube = 5 Hours
- Instagram = 3 Hours
- Gaming = 2 Hours

Total = 10 Hours

Pie Chart immediately shows:

- YouTube = 50%
- Instagram = 30%
- Gaming = 20%

This is called:

### Composition

or

### Parts of a Whole
""")

st.divider()

st.header("⚔️ Bar Chart vs Pie Chart")

comparison_df = pd.DataFrame({
    "Bar Chart": [
        "Compare Categories",
        "Ranking",
        "Many Categories",
        "Precise Comparison"
    ],
    "Pie Chart": [
        "Parts of a Whole",
        "Percentages",
        "Few Categories",
        "Composition"
    ]
})

st.table(comparison_df)

st.divider()

st.header("🕵️ Pie Chart Detective")

st.write("""
Whenever you see a Pie Chart ask:
""")

questions = [
    "Do all slices add up to 100%?",
    "Is there a clear title?",
    "Are there too many slices?",
    "Could a Bar Chart explain this better?",
    "Is the chart trying to tell a story?"
]

for q in questions:
    st.write("✅", q)

st.divider()

st.header("✅ When Should We Use Pie Charts?")

st.success("""
Good Uses:

✔ School Budget

✔ Favorite Subjects

✔ Mobile Usage

✔ Family Expenses

✔ House Competition Points
""")

st.error("""
Bad Uses:

❌ Too Many Categories

❌ Comparing Similar Values

❌ Ranking Large Lists

❌ Time Series Data
""")

st.divider()

st.header("🎯 Classroom Challenge")

st.markdown("""
Collect data from your classroom:

### Favorite Sport

Create:

1. Table
2. Bar Chart
3. Pie Chart

Then answer:

- Which sport got the most votes?
- What percentage likes Cricket?
- Which chart made comparison easier?
- Which chart showed composition better?

Think like a Data Detective!
""")

st.divider()

st.header("🎨 Create Your Own Pie Chart")

cat1 = st.text_input(
    "Category 1",
    "Science"
)

cat2 = st.text_input(
    "Category 2",
    "Maths"
)

cat3 = st.text_input(
    "Category 3",
    "English"
)

val1 = st.slider(
    "Value 1",
    0,
    100,
    50,
    key="pie_custom_1"
)

val2 = st.slider(
    "Value 2",
    0,
    100,
    30,
    key="pie_custom_2"
)

val3 = st.slider(
    "Value 3",
    0,
    100,
    20,
    key="pie_custom_3"
)

custom_df = pd.DataFrame({
    "Category": [cat1, cat2, cat3],
    "Value": [val1, val2, val3]
})

if px is None:
    st.warning("Plotly is not installed. Install it with `pip install plotly` to view the custom pie chart.")
else:
    custom_fig = px.pie(
        custom_df,
        names="Category",
        values="Value",
        title="My Own Pie Chart"
    )

    st.plotly_chart(
        custom_fig,
        use_container_width=True
    )


st.header("🏏 Build Your Cricket Pie Chart")

rohit = st.slider("Rohit Runs", 0, 100, 50)
kohli = st.slider("Kohli Runs", 0, 100, 30)
gill = st.slider("Gill Runs", 0, 100, 20)

df = pd.DataFrame({
    "Player": ["Rohit", "Kohli", "Gill"],
    "Runs": [rohit, kohli, gill]
})

fig = px.pie(
    df,
    names="Player",
    values="Runs",
    title="Contribution to Team Score"
)

st.plotly_chart(fig, use_container_width=True)

total = rohit + kohli + gill

if total > 0:
    st.write(f"🏏 Rohit Contribution: {(rohit/total)*100:.1f}%")
    st.write(f"🏏 Kohli Contribution: {(kohli/total)*100:.1f}%")
    st.write(f"🏏 Gill Contribution: {(gill/total)*100:.1f}%")
