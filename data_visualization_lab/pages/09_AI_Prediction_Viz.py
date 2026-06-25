import streamlit as st
import pandas as pd
from graphviz import Digraph

st.title("🧠 AI Prediction Visualizer")

st.markdown("""
# Welcome to the AI Brain Lab

Today you will become the AI.

You will:

✅ Give information to the AI

✅ Decide importance (weights)

✅ Add a starting point (bias)

✅ Watch the AI make predictions

Let's look inside an AI brain!
""")

st.divider()


st.header("📥 Step 1: Give Information To AI")

study_hours = st.slider(
    "📚 Study Hours",
    0,
    10,
    5
)

coding_skill = st.slider(
    "💻 Coding Skill",
    0,
    10,
    5
)

attendance = st.slider(
    "🏫 Attendance",
    0,
    10,
    5
)

st.divider()

st.header("⚖️ Step 2: Decide Importance")

study_weight = st.slider(
    "Importance of Study Hours",
    0,
    10,
    5
)

coding_weight = st.slider(
    "Importance of Coding Skill",
    0,
    10,
    4
)

attendance_weight = st.slider(
    "Importance of Attendance",
    0,
    10,
    3
)

st.divider()

st.header("🏁 Step 3: Starting Point (Bias)")

bias = st.slider(
    "Bias",
    0,
    50,
    10
)

st.info("""
Imagine a shop.

Even before customers arrive:

• Rent exists

• Electricity bill exists

That starting value is called BIAS.
""")

study_score = study_hours * study_weight
coding_score = coding_skill * coding_weight
attendance_score = attendance * attendance_weight

prediction = (
    study_score
    + coding_score
    + attendance_score
    + bias
)


st.divider()

st.header("🤖 How AI Is Thinking")

st.write(
    f"📚 Study Hours Contribution = {study_hours} × {study_weight} = {study_score}"
)

st.write(
    f"💻 Coding Skill Contribution = {coding_skill} × {coding_weight} = {coding_score}"
)

st.write(
    f"🏫 Attendance Contribution = {attendance} × {attendance_weight} = {attendance_score}"
)

st.write(
    f"🏁 Bias = {bias}"
)

st.success(
    f"🎯 Final Prediction Score = {prediction}"
)

st.divider()

st.header("🧠 Inside The AI Brain")

dot = Digraph()

dot.node(
    "Study",
    f"Study Hours\n{study_hours}"
)

dot.node(
    "Coding",
    f"Coding Skill\n{coding_skill}"
)

dot.node(
    "Attendance",
    f"Attendance\n{attendance}"
)

dot.node(
    "Neuron",
    "AI Neuron"
)

dot.node(
    "Prediction",
    f"Prediction\n{prediction}"
)

dot.edge(
    "Study",
    "Neuron",
    label=f"x {study_weight}"
)

dot.edge(
    "Coding",
    "Neuron",
    label=f"x {coding_weight}"
)

dot.edge(
    "Attendance",
    "Neuron",
    label=f"x {attendance_weight}"
)

dot.edge(
    "Neuron",
    "Prediction"
)

st.graphviz_chart(dot)


st.divider()

st.header("📋 AI Report Card")

report = pd.DataFrame({
    "Feature": [
        "Study Hours",
        "Coding Skill",
        "Attendance"
    ],
    "Value": [
        study_hours,
        coding_skill,
        attendance
    ],
    "Weight": [
        study_weight,
        coding_weight,
        attendance_weight
    ],
    "Contribution": [
        study_score,
        coding_score,
        attendance_score
    ]
})

st.dataframe(
    report,
    use_container_width=True
)

st.divider()

st.header("🌍 Where Is This Used?")

st.divider()

st.header("📂 Upload Student Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)


if uploaded_file:

    df = pd.read_csv(uploaded_file)

    df["Prediction"] = (
        df["StudyHours"] * study_weight
        +
        df["CodingSkill"] * coding_weight
        +
        df["Attendance"] * attendance_weight
        +
        bias
    )

    st.success("AI Predictions Generated!")

    st.dataframe(
        df,
        use_container_width=True
    )


    st.divider()

st.success("""
What Did We Learn?

📥 Features = Information

⚖️ Weights = Importance

🏁 Bias = Starting Point

🧠 Neuron = Decision Maker

🎯 Prediction = Final Answer

AI is not magic.

AI combines information,
gives importance to useful things,
and makes predictions.
""")

