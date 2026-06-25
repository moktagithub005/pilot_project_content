import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🤖 How AI Makes Predictions")

st.markdown("""
# Welcome to the AI Brain Lab

Today we will discover:

How does AI make decisions?

How does ChatGPT predict words?

How does YouTube recommend videos?

How does Netflix recommend movies?

Let's find out!
""")

st.divider()

st.header("🧠 Step 1: AI Learns From Examples")

st.write("""
Imagine we collect information about students.
""")

df = pd.DataFrame({
    "Student": ["Rahul","Priya","Aman","Neha"],
    "Coding Skill": [2,4,7,9],
    "Board Marks": [50,65,80,95],
    "Future Salary (Lakhs)": [3,5,10,15]
})

st.dataframe(df,use_container_width=True)

st.success("""
Look carefully.

Students with better skills tend to get better salaries.

AI learns from examples like these.
""")

st.divider()

st.header("📥 Step 2: Input Features")

st.write("""
AI cannot magically predict things.

It needs information first.
""")

st.info("""
Coding Skill

Board Marks

Study Hours

Attendance

These pieces of information are called FEATURES.
""")

coding = st.slider(
    "Coding Skill",
    0,
    10,
    5
)

marks = st.slider(
    "Board Marks (%)",
    0,
    100,
    70
)

st.success(f"""
Features Given To AI:

Coding Skill = {coding}

Board Marks = {marks}
""")

st.divider()

st.header("🎯 Step 3: What Are We Predicting?")

st.write("""
Every AI system has a goal.

Something it wants to predict.
""")

st.success("""
Future Salary

is our TARGET.
""")

st.markdown("""
Features
↓
AI
↓
Prediction
""")

st.divider()

st.header("🧠 Step 4: Meet The Neuron")

st.write("""
The Neuron is the basic decision-maker inside AI.

Think of it as a tiny brain.
""")

st.info("""
Imagine:

Should I watch Netflix tonight?

Your brain thinks:

• Homework Done?

• Exam Tomorrow?

• Sleep Needed?

Then makes a decision.

A Neuron works exactly the same way.
""")

st.divider()

st.header("⚖️ Step 5: Importance (Weight)")

study_weight = st.slider(
    "Importance of Coding Skill",
    0,
    10,
    8
)

marks_weight = st.slider(
    "Importance of Marks",
    0,
    10,
    5
)

st.write("""
In AI, importance is called a WEIGHT.

Bigger Weight = More Important
""")

st.info("""
Imagine a principal choosing School Captain.

Leadership may matter more.

Attendance may matter less.

These importance values are called WEIGHTS.
""")

st.divider()

st.header("🏁 Step 6: Starting Point (Bias)")

bias = st.slider(
    "Bias",
    0,
    50,
    10
)

st.info("""
Imagine a shop.

Even before customers arrive:

• Rent Exists

• Electricity Bill Exists

There is already a starting cost.

This starting point is called BIAS.
""")

st.divider()

st.header("🤖 Step 7: AI Makes A Prediction")

prediction = (
    coding * study_weight
    +
    marks * marks_weight
    +
    bias
)

st.latex(
    r"Prediction = (Weight \times Feature) + Bias"
)

st.success(
    f"Predicted Score = {prediction}"
)


st.write(f"""
AI looked at:

Coding Skill = {coding}

Marks = {marks}

Weights = Importance

Bias = Starting Point

and made a prediction.
""")

st.divider()

st.header("🎲 Step 8: Probability")

st.write("""
Suppose I say:

I drink tea with ______
""")


option = st.radio(
    "Choose the most likely word",
    [
        "Milk",
        "Potato",
        "Laptop",
        "Football"
    ]
)

if option == "Milk":
    st.success("""
Correct!

AI chooses the most likely answer.

This idea is called Probability.
""")
    


st.divider()

st.header("📊 Step 9: Why Statistics Matters")


students = st.slider(
    "Number of Students Surveyed",
    1,
    1000,
    10
)

st.write(f"""
Suppose we ask {students} students
about their study habits.
""")

if students < 10:
    st.warning("""
Very few students.

Prediction may be poor.
""")
else:
    st.success("""
More examples.

Better learning.

This is why AI loves data.
""")
    
st.divider()

st.header("📏 Step 10: Normalization")

norm_df = pd.DataFrame({
    "Feature": [
        "Study Hours",
        "Pocket Money"
    ],
    "Value": [
        5,
        500
    ]
})

fig = px.bar(
    norm_df,
    x="Feature",
    y="Value",
    title="Before Normalization"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info("""
Study Hours = 5

Pocket Money = 500

One feature is much larger.

AI gets confused.

So we scale them to similar ranges.

This is called NORMALIZATION.
""")

norm_df2 = pd.DataFrame({
    "Feature": [
        "Study Hours",
        "Pocket Money"
    ],
    "Value": [
        0.5,
        0.5
    ]
})

fig2 = px.bar(
    norm_df2,
    x="Feature",
    y="Value",
    title="After Normalization"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

st.header("🚀 How AI Really Works")

st.markdown("""
Data
↓
Features
↓
Neuron
↓
Weights
↓
Bias
↓
Prediction
""")

summary = pd.DataFrame({
    "Concept":[
        "Features",
        "Weights",
        "Bias",
        "Statistics",
        "Probability",
        "Prediction"
    ],
    "Meaning":[
        "Information",
        "Importance",
        "Starting Point",
        "Learning From Examples",
        "Chance",
        "Final Answer"
    ]
})

st.table(summary)


st.success("""
AI is NOT magic.

AI learns from examples.

AI finds patterns.

AI gives importance to useful information.

AI uses mathematics to make predictions.

Just like humans learn from experience,
AI learns from data.
""")

