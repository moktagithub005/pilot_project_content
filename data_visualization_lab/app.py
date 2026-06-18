import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="UNISOLE Skill AI Labs",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# Hero Section
# ---------------------------------------------------

st.title("🚀 UNISOLE Skill AI Labs")

st.subheader(
    "Learn Data, Visualization, AI and Critical Thinking Through Interactive Experiments"
)

st.divider()

# ---------------------------------------------------
# Welcome Message
# ---------------------------------------------------

st.markdown(
    """
## 👋 Welcome Future Data Detectives!

Have you ever wondered:

- How does YouTube know which videos you like?
- How does Google Maps find the fastest route?
- How does Instagram recommend reels?
- How does AI make decisions?

The answer starts with **Data**.

In this lab, you will not just learn graphs.

You will learn how to:

✅ Collect Data

✅ Understand Data

✅ Visualize Data

✅ Spot Misleading Graphs

✅ Think Like a Data Scientist

✅ Understand How AI Learns

---

### 🎯 Our Mission

Most people see numbers.

Data Scientists see stories.

By the end of this lab, you will learn how to discover stories hidden inside data.
"""
)

# ---------------------------------------------------
# Learning Journey
# ---------------------------------------------------

st.divider()

st.header("🗺️ Your Learning Journey")

st.markdown(
    """
### Chapter 0
📚 Dataset Playground

Learn:
- What is a dataset?
- What is a row?
- What is a column?
- Where does data come from?

---

### Chapter 1
📊 What Is Data?

Learn:
- What data actually means
- Why data is everywhere
- Why data powers AI

---

### Chapter 2
🎯 Categories vs Measurements

Learn:
- Categorical Data
- Numerical Data
- Continuous Data
- Real-life examples

---

### Chapter 3
📈 Why Graphs Exist

Learn:
- Why raw numbers are difficult
- Why humans love visuals
- How graphs help us think

---

### Chapter 4
📊 Bar Charts

Learn:
- Comparing categories
- Why bars have gaps
- When bar charts should be used

---

### Chapter 5
📉 Histograms

Learn:
- Continuous data
- Distributions
- Why histogram bars touch

---

### Chapter 6
🕵️ Graphs Can Lie

Learn:
- Truncated axes
- Misleading scales
- Media manipulation
- Data detective skills

---

### Chapter 7
📊 Grouped Bar Charts

Learn:
- Compare multiple groups
- Side-by-side analysis

---

### Chapter 8
📚 Stacked Bar Charts

Learn:
- Parts of a whole
- Composition analysis

---

### Chapter 9
🎮 Data Detective Challenge

Put your skills to the test by spotting errors in real graphs.
"""
)

# ---------------------------------------------------
# Fun Facts
# ---------------------------------------------------

st.divider()

st.header("🤯 Did You Know?")

fact = st.selectbox(
    "Choose a Fun Fact",
    [
        "AI",
        "Data",
        "Visualization",
        "Internet"
    ]
)

if fact == "AI":
    st.info(
        """
Every AI system learns from data.

No Data = No AI
        """
    )

elif fact == "Data":
    st.info(
        """
More than 90% of the world's data has been created in the last few years.
        """
    )

elif fact == "Visualization":
    st.info(
        """
Humans understand pictures much faster than large tables of numbers.
        """
    )

else:
    st.info(
        """
Every Google search, YouTube video and Instagram reel creates new data.
        """
    )

# ---------------------------------------------------
# Final Message
# ---------------------------------------------------

st.divider()

st.success(
    """
🚀 Ready to Begin?

Open the sidebar and start with:

📚 Dataset Playground

Remember:

Data Scientists don't just look at data.

They ask questions.

They investigate.

They think critically.

Welcome to UNISOLE Skill AI Labs!
"""
)

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

st.caption(
    "UNISOLE Skill AI Labs | Learn AI, Data Science and Critical Thinking Through Exploration"
)