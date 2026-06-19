import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏏 Cricket Analytics with Line Charts")

st.header("📈 Understanding Line Charts")

st.markdown("""
### The Big Idea

A Line Chart shows:

➡️ How something changes over time.

Think about cricket.

If we know how many runs a player scored in one match,
that is just one number.

But if we know his runs across many matches,
we can discover a story.

A Line Chart helps us see that story.
""")

st.divider()

# ----------------------------------
# Interactive Cricket Example
# ----------------------------------

st.header("🏏 Virat Kohli's Runs Across Matches")

m1 = st.slider("Match 1 Runs", 0, 150, 25)
m2 = st.slider("Match 2 Runs", 0, 150, 45)
m3 = st.slider("Match 3 Runs", 0, 150, 70)
m4 = st.slider("Match 4 Runs", 0, 150, 30)
m5 = st.slider("Match 5 Runs", 0, 150, 90)

df = pd.DataFrame({
    "Match": [
        "Match 1",
        "Match 2",
        "Match 3",
        "Match 4",
        "Match 5"
    ],
    "Runs": [
        m1,
        m2,
        m3,
        m4,
        m5
    ]
})

fig = px.line(
    df,
    x="Match",
    y="Runs",
    markers=True,
    title="Virat Kohli Runs Across Matches"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.header("🕵️ Become a Cricket Data Detective")

highest = max([m1, m2, m3, m4, m5])
lowest = min([m1, m2, m3, m4, m5])

st.write(f"🏆 Highest Score: {highest}")
st.write(f"📉 Lowest Score: {lowest}")

st.info("""
Ask yourself:

1. Is the line moving up?
2. Is it moving down?
3. Is there a sudden jump?
4. Is there a sudden drop?
5. Is the player becoming more consistent?

This is how analysts think.
""")

st.divider()

st.header("🤔 Why Not Use a Bar Chart?")

st.markdown("""
A Bar Chart is great for comparing categories.

Example:

- Virat
- Rohit
- Gill

Question:

Who scored more?

Use a Bar Chart.

---

But today we are asking:

### How did Virat's performance change across matches?

Now order matters:

Match 1 → Match 2 → Match 3 → Match 4 → Match 5

That is why we use a Line Chart.
""")

st.divider()

st.header("✅ Conditions For Using A Line Chart")

st.success("""
Use a Line Chart when:

✔ Order matters

✔ Time matters

✔ Data changes

✔ You want to see trends

✔ You want to tell a story
""")

st.error("""
Do NOT use a Line Chart when:

❌ Comparing Sports

❌ Comparing Countries

❌ Comparing Subjects

❌ Comparing Brands

Use a Bar Chart instead.
""")

st.divider()

st.header("🔥 Team Run Rate Across Overs")

o1 = st.slider("Over 1", 0, 20, 6)
o2 = st.slider("Over 2", 0, 20, 7)
o3 = st.slider("Over 3", 0, 20, 8)
o4 = st.slider("Over 4", 0, 20, 9)
o5 = st.slider("Over 5", 0, 20, 10)

rr_df = pd.DataFrame({
    "Over": [1, 2, 3, 4, 5],
    "Run Rate": [o1, o2, o3, o4, o5]
})

fig2 = px.line(
    rr_df,
    x="Over",
    y="Run Rate",
    markers=True,
    title="Run Rate Progression"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("""
### What Story Does This Tell?

If the line rises:

📈 Batters are accelerating

If the line falls:

📉 Batters are slowing down

If the line is flat:

➡️ Performance is stable
""")

st.divider()

st.header("🏆 IPL Team Points Across Seasons")

season_df = pd.DataFrame({
    "Season": [
        "2022",
        "2023",
        "2024",
        "2025",
        "2026"
    ],
    "Points": [
        14,
        18,
        16,
        20,
        22
    ]
})

fig3 = px.line(
    season_df,
    x="Season",
    y="Points",
    markers=True,
    title="IPL Team Growth"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.write("""
This chart tells us:

The team is improving over time.

This is exactly why Line Charts exist.
""")

st.divider()

st.header("🌍 Where Are Line Charts Used?")

applications = [
    "🌡 Weather Forecasting",
    "📈 Stock Market",
    "🏏 Cricket Analytics",
    "📱 YouTube Subscriber Growth",
    "❤️ Heart Rate Monitoring",
    "🌧 Rainfall Analysis",
    "🍎 Apple Production in Himachal Pradesh",
    "🤖 AI Model Training"
]

for app in applications:
    st.write(app)

st.divider()

st.header("🤖 AI Connection")

st.markdown("""
Machine Learning Engineers use Line Charts every day.

Examples:

• Model Accuracy vs Epochs

• Training Loss vs Epochs

• Validation Accuracy vs Time

If the line improves:

Model is learning.

If the line drops:

Something is wrong.

Line Charts help AI Engineers understand model behavior.
""")
st.divider()

st.header("🎯 Final Summary")

summary = pd.DataFrame({
    "Chart": [
        "Bar Chart",
        "Pie Chart",
        "Line Chart"
    ],
    "Purpose": [
        "Compare Categories",
        "Parts of a Whole",
        "Show Change Over Time"
    ]
})

st.table(summary)

st.success("""
Remember:

📊 Bar Chart → Compare

🥧 Pie Chart → Divide

📈 Line Chart → Tell a Story Through Time
""")

