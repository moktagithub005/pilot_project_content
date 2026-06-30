import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# -------------------------------------------------------
# CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="UNISOLE AI Exploration Lab",
    page_icon="🧠",
    layout="wide"
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.hero{
background:linear-gradient(90deg,#2563EB,#06B6D4);
padding:35px;
border-radius:20px;
color:white;
}

.mission{
background:#F8FAFC;
padding:20px;
border-radius:15px;
border-left:8px solid #2563EB;
}

.quote{
background:#FFF7ED;
padding:20px;
border-radius:15px;
font-size:20px;
font-weight:bold;
color:#9A3412;
}

.big{
font-size:30px;
font-weight:bold;
}

.small{
font-size:18px;
}

</style>
""",unsafe_allow_html=True)

# -------------------------------------------------------
# HERO
# -------------------------------------------------------

st.markdown("""
<div class="hero">

# 🧠 UNISOLE AI Exploration Lab

### Mission 1 : AI That Can Create

#### Learn • Explore • Build • Create

Welcome AI Explorer!

Today you are NOT attending a lecture.

Today you are entering an AI Laboratory.

There are no wrong questions.

Only discoveries.

</div>
""",unsafe_allow_html=True)

st.progress(10)

st.success("Mission Progress : 10%")

# -------------------------------------------------------
# PHILOSOPHY
# -------------------------------------------------------

st.header("🚀 Today's Mission")

col1,col2=st.columns(2)

with col1:

    st.markdown("""
### Today's Objective

By the end of today's mission you should understand:

✅ AI can create

✅ AI predicts instead of thinking

✅ Prompt quality matters

✅ AI is a powerful tool

✅ You can use AI responsibly
""")

with col2:

    st.info("""
Today's Journey

🎬 Hook

↓

🤔 Curiosity

↓

🧠 Discovery

↓

💻 Hands-on

↓

🌍 Real World

↓

🎯 Reflection
""")

# -------------------------------------------------------
# MAGIC SHOW
# -------------------------------------------------------

st.divider()

st.header("🎬 Activity 1 : The Magic Show")

st.write("""
Choose a single example from dropdown:
""")

examples = [
    "Write a poem on Himachal Pradesh.",
    "Write the same poem as if Virat Kohli is speaking.",
    "Write the same poem like a Bollywood villain.",
    "Write the same poem in Shakespeare's style."
]

choice = st.selectbox(
    "Choose a Prompt",
    examples
)

if st.button("✨ Generate with AI"):

    with st.spinner("AI is creating..."):

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role":"system",
                    "content":"You are an expert creative writer."
                },
                {
                    "role":"user",
                    "content":choice
                }
            ]
        )

        st.success(response.choices[0].message.content)

st.info("""
🤔 Think...

Did anyone teach AI poetry?

If not...

How did it create this?
""")

# -------------------------------------------------------
# IMPOSSIBLE CHALLENGE
# -------------------------------------------------------

st.divider()

st.header("🎮 Activity 2 : The Impossible Challenge")

st.write("""
choose  random words.

Let's see whether AI can create a story.
""")

c1,c2,c3=st.columns(3)

with c1:
    word1=st.text_input("Word 1","Banana")

with c2:
    word2=st.text_input("Word 2","Rocket")

with c3:
    word3=st.text_input("Word 3","Grandmother")

if st.button("📖 Create Funny Story"):

    prompt=f"""
Write a funny story using

{word1}

{word2}

{word3}

The story should be suitable for Class 9 students.
"""

    with st.spinner("Creating Story..."):

        response=client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        st.success(response.choices[0].message.content)

# -------------------------------------------------------
# THINK
# -------------------------------------------------------

st.divider()

st.header("🤔 Stop And Think")

question=st.radio(

    "What surprised you the most?",

    [

        "AI wrote a poem",

        "AI used random words",

        "AI changed writing style",

        "Everything"

    ]

)

if question:

    st.success(f"You selected : {question}")

# -------------------------------------------------------
# DISCOVERY
# -------------------------------------------------------

st.divider()

st.header("🧠 Discovery")

st.markdown("""
### AI is NOT copying.

### AI is NOT searching.

### AI is GENERATING.

It creates brand-new content by predicting what should come next.

That is why it is called

## Generative AI
""")

# -------------------------------------------------------
# GENERATIVE AI
# -------------------------------------------------------

st.header("📚 What Does 'Generative' Mean?")

col1,col2=st.columns(2)

with col1:

    st.metric("Old AI","Recognize")

    st.write("""

Recognize Images

Recognize Speech

Recognize Faces

Recognize Spam

""")

with col2:

    st.metric("Generative AI","Create")

    st.write("""

Create Stories

Create Poems

Create Images

Create Emails

Create Code

""")

# -------------------------------------------------------
# PLAYGROUND
# -------------------------------------------------------

st.divider()

st.header("🛠 AI Playground")

user_prompt=st.text_area(

    "Ask AI Anything",

    height=150,

    placeholder="Explain black holes like a cricket commentator..."

)

if st.button("🚀 Ask AI"):

    with st.spinner("Thinking..."):

        response=client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role":"system",
                    "content":"Explain everything in simple language using analogies."
                },
                {
                    "role":"user",
                    "content":user_prompt
                }
            ]
        )

        st.success(response.choices[0].message.content)

# -------------------------------------------------------
# REFLECTION
# -------------------------------------------------------

st.divider()

st.header("🪞 Reflection")

q1=st.text_area(

"What surprised you today?"

)

q2=st.text_area(

"What excited you today?"

)

q3=st.text_area(

"How could AI help your family?"

)

if st.button("Save Reflection"):

    st.success("Excellent! Scientists always reflect after every experiment.")

# -------------------------------------------------------
# HOMEWORK
# -------------------------------------------------------

st.divider()

st.header("🏡 AI Homework Challenge")

st.info("""
Tonight,

Use AI to help one member of your family.

Examples

✅ Help your mother plan weekly meals.

✅ Help your father write a formal letter.

✅ Help your younger sibling understand Science.

✅ Translate something for your grandparents.

Tomorrow,

Tell us whether AI actually helped.
""")

# -------------------------------------------------------
# FINAL MESSAGE
# -------------------------------------------------------

st.divider()

st.markdown("""
<div class="quote">

"The future will not belong to the people who simply use AI."

<br><br>

"It will belong to the people who know WHAT to ask AI."

</div>
""",unsafe_allow_html=True)

st.success("""
🏆 Mission 1 Complete!

Next Mission:

🧠 How AI Predicts Words
""")
