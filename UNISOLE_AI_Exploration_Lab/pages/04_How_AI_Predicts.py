import streamlit as st
import time

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Mission 2 - How AI Predicts",
    page_icon="🧠",
    layout="wide"
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

.card{
background:#F8FAFC;
padding:25px;
border-radius:15px;
border-left:8px solid #2563EB;
margin-top:15px;
margin-bottom:15px;
}

.quote{
background:#FEF3C7;
padding:20px;
border-radius:15px;
font-size:22px;
font-weight:bold;
color:#92400E;
}

.highlight{
color:#2563EB;
font-weight:bold;
font-size:22px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# HERO
# -------------------------------------------------------

st.markdown("""
<div class="hero">

# 🧠 UNISOLE AI Exploration Lab

## Mission 2 : How Does AI Predict?

### Every sentence begins with just ONE word...

But how does AI know the next one?

Today you'll discover the secret.

</div>
""", unsafe_allow_html=True)

st.progress(20)

st.success("Mission Progress : 20 %")

# -------------------------------------------------------
# THINK FIRST
# -------------------------------------------------------

st.divider()

st.header("🤔 Think Before You Scroll")

st.markdown("""
Take **10 seconds**.

Don't search.

Don't ask anyone.

Just think.

### How does ChatGPT know what to write next?

Choose your answer below.
""")

idea = st.radio(

    "What do you think?",

    [

        "It memorizes every sentence",

        "It searches Google",

        "It predicts the next word",

        "It understands everything like humans"

    ]

)

if st.button("Submit My Answer"):

    if idea == "It predicts the next word":

        st.success("Excellent! 🎉 That's very close to the real answer.")

    else:

        st.warning("""
Interesting!

Let's continue the mission.

By the end of today's activity,
you'll discover the real answer yourself.
""")

# -------------------------------------------------------
# ACTIVITY 1
# -------------------------------------------------------

st.divider()

st.header("🎮 Activity 1 : Complete The Sentence")

st.markdown("""
Imagine someone starts speaking...

Can you predict the next word?

Let's try.
""")

answer = st.text_input(

    "The Sun rises in the ______"

)

if st.button("Check Answer"):

    st.success(f"You answered : **{answer}**")

    st.info("""
Most people around the world answer:

🌞 **East**

But here's the interesting question...

Did everyone memorize this exact sentence?

Probably not.

Instead...

Your brain predicted the most likely word.
""")

# -------------------------------------------------------
# SECOND EXAMPLE
# -------------------------------------------------------

st.divider()

st.header("🌍 One More Experiment")

answer2 = st.text_input(

    "India's capital is ______"

)

if st.button("Reveal"):

    st.success(f"You answered : **{answer2}**")

    st.info("""
Most people say:

🇮🇳 New Delhi

Again...

Nobody searched Google.

Nobody opened a book.

Your brain predicted
the most likely answer.
""")

# -------------------------------------------------------
# THIRD EXAMPLE
# -------------------------------------------------------

st.divider()

st.header("☕ One Last Prediction")

answer3 = st.text_input(

    "I drink tea with ______"

)

if st.button("Show Result"):

    st.success(f"You answered : **{answer3}**")

    st.markdown("""

People usually answer things like:

🥛 Milk

🍬 Sugar

🫖 Lemon

Notice something...

Different people give slightly different answers.

But nobody says:

🚀 Rocket

🧱 Brick

💻 Computer

Why?

Because some words are much more likely than others.
""")

# -------------------------------------------------------
# BIG DISCOVERY
# -------------------------------------------------------

st.divider()

st.header("🧠 Discovery Time")

st.markdown("""
<div class="card">

# What just happened?

Your brain did **NOT** memorize these sentences.

Instead...

It looked at the words already written.

Then it predicted the most likely next word.

Guess what?

<span class="highlight">

ChatGPT does something very similar.

</span>

It predicts the next most probable word.

Not magic.

Not mind reading.

Prediction.

</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# QUOTE
# -------------------------------------------------------

st.markdown("""
<div class="quote">

Prediction is one of the most powerful ideas in Artificial Intelligence.

</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# NEXT MISSION
# -------------------------------------------------------

st.success("""
🚀 Great Job AI Explorer!

In the next activity you'll discover

👉 WHY some words are more likely than others.

We'll even visualize probabilities!

Keep going...
""")

# ===========================================================
# ACTIVITY 2 : WHY SOME WORDS ARE MORE LIKELY?
# ===========================================================

st.divider()

st.header("🎲 Activity 2 : Why Are Some Words More Likely?")

st.markdown("""
Imagine I start a sentence...

## **I drink tea with ______**

What word would you expect next?

Choose one.
""")

prediction = st.radio(

    "Your Prediction",

    [
        "🥛 Milk",
        "🧱 Brick",
        "💻 Computer",
        "🚀 Rocket",
        "⛽ Petrol"
    ]

)

if st.button("Reveal Most Likely Word"):

    if prediction == "🥛 Milk":

        st.success("Excellent! 🎉")

    else:

        st.warning("Interesting prediction!")

    st.info("""

Your brain immediately rejected words like

🧱 Brick

💻 Computer

🚀 Rocket

because you've probably never heard people say

'I drink tea with a brick.'

Your brain uses EXPERIENCE.

AI uses PATTERNS.

""")

# ===========================================================
# PROBABILITY
# ===========================================================

st.divider()

st.header("📊 Every Word Has A Probability")

st.markdown("""
Think of every possible next word.

Some words are

✅ Very likely

Some are

❌ Almost impossible.
""")

probabilities = {
    "🥛 Milk":99,
    "🍬 Sugar":85,
    "🍋 Lemon":30,
    "🧱 Brick":1,
    "💻 Computer":1,
    "🚀 Rocket":1
}

for word,value in probabilities.items():

    st.write(f"### {word}")

    st.progress(value)

    st.caption(f"Probability : {value}%")

st.success("""
The higher the probability,

the more likely AI is to choose that word.
""")

# ===========================================================
# VISUAL EXPLANATION
# ===========================================================

st.divider()

st.header("🧠 How Does AI Choose?")

st.markdown("""

Imagine AI is looking at many possible words.

""")

col1,col2=st.columns(2)

with col1:

    st.markdown("""

Possible Words

🥛 Milk

🍬 Sugar

🍋 Lemon

🚀 Rocket

🧱 Brick

💻 Computer

""")

with col2:

    st.markdown("""

Probability

99%

85%

30%

1%

1%

1%

""")

st.info("""

AI doesn't randomly choose words.

It gives every possible word a score.

Then it usually picks one of the highest scoring words.

""")

# ===========================================================
# INTERACTIVE SLIDER
# ===========================================================

st.divider()

st.header("🎮 Probability Playground")

confidence = st.slider(

    "Move the slider to change AI confidence",

    0,

    100,

    95

)

st.progress(confidence)

if confidence>90:

    st.success("""

AI is VERY confident.

The answer is almost certain.

""")

elif confidence>60:

    st.warning("""

AI has a few good possibilities.

More than one answer could work.

""")

else:

    st.error("""

AI is uncertain.

Many answers might be possible.

""")

# ===========================================================
# THINK LIKE AI
# ===========================================================

st.divider()

st.header("🤖 Think Like AI")

st.markdown("""

Let's play a game.

You are now the AI.

Choose the next word.

""")

sentence = st.selectbox(

    "Sentence",

    [

        "The sky is ____",

        "Fish live in ____",

        "Birds can ____",

        "Cricket is played with ____"

    ]

)

if sentence=="The sky is ____":

    choices=["Blue","Banana","Laptop","Car"]

elif sentence=="Fish live in ____":

    choices=["Water","Tree","Road","Notebook"]

elif sentence=="Birds can ____":

    choices=["Fly","Swim","Cook","Drive"]

else:

    choices=["Bat","Television","Chair","Pillow"]

guess=st.radio(

    "Choose",

    choices

)

if st.button("Was That A Good Prediction?"):

    st.success(f"You selected : {guess}")

    st.info("""

Notice something amazing?

You didn't calculate anything.

You simply chose

the word that felt

MOST LIKELY.

That's exactly the big idea behind

Large Language Models.

""")

# ===========================================================
# AI THINKING ANIMATION
# ===========================================================

st.divider()

st.header("⚙️ Inside An AI's Mind")

placeholder=st.empty()

if st.button("Watch AI Think"):

    placeholder.info("Reading previous words...")

    time.sleep(1)

    placeholder.info("Finding possible next words...")

    time.sleep(1)

    placeholder.info("Calculating probabilities...")

    time.sleep(1)

    placeholder.info("Choosing highest probability...")

    time.sleep(1)

    placeholder.success("Generated Word : 🥛 Milk")

# ===========================================================
# DISCOVERY
# ===========================================================

st.divider()

st.header("💡 What Have You Discovered?")

st.markdown("""

Until now you may have thought

AI magically knows everything.

Now you know something much deeper.

AI predicts.

It calculates.

It estimates.

It chooses the most likely next word.

That simple idea powers

ChatGPT,

Gemini,

Claude,

Llama,

and many other AI systems.

""")

st.success("""

🎉 Mission Progress Updated!

You now understand

✅ Prediction

✅ Probability

✅ Why AI usually gives sensible answers

Next,

we'll discover something even cooler...

🧩 TOKENS

The tiny building blocks

that every Large Language Model reads.

""")
# ==========================================================
# ACTIVITY 3 : HOW DOES AI READ?
# ==========================================================

st.divider()

st.header("🧩 Activity 3 : How Does AI Read Language?")

st.markdown("""

Imagine you are reading this sentence:

# I love playing cricket with my friends.

Easy, right?

But here's something surprising...

🤖 AI does **NOT** read this sentence the way humans do.

Let's discover how AI actually reads language.

""")

st.info("""
🧠 Fun Fact

Large Language Models like ChatGPT don't see language exactly like we do.

Instead...

They break it into small pieces called **TOKENS**.
""")

# ==========================================================
# TOKEN VISUALIZATION
# ==========================================================

st.divider()

st.subheader("🔍 Example 1 : Sentence to Tokens")

sentence = [
    "I",
    "love",
    "playing",
    "cricket",
    "with",
    "my",
    "friends",
    "."
]

st.markdown("### Original Sentence")

st.success("I love playing cricket with my friends.")

st.markdown("### How AI Sees It")

cols = st.columns(len(sentence))

for col, token in zip(cols, sentence):

    col.markdown(
        f"""
<div style='
background:#2563EB;
padding:15px;
border-radius:10px;
text-align:center;
color:white;
font-size:20px;
font-weight:bold;
'>
{token}
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown("""

Instead of reading one big sentence,

AI reads **one token at a time.**

""")

# ==========================================================
# TOKEN WALK
# ==========================================================

st.divider()

st.subheader("🚶 Let's Walk Through The Sentence")

placeholder = st.empty()

if st.button("▶️ Read Like AI"):

    for token in sentence:

        placeholder.success(f"Reading Token : **{token}**")

        time.sleep(0.8)

    placeholder.info("Sentence Complete ✅")

# ==========================================================
# LONG WORDS
# ==========================================================

st.divider()

st.subheader("🤯 Do Tokens Always Mean Words?")

st.markdown("""

Most people think:

One Word = One Token

❌ Not always.

Some long words are split into smaller pieces.

""")

st.success("unbelievable")

st.markdown("""

AI may internally read something similar to:

""")

cols = st.columns(3)

cols[0].markdown(
"""
<div style='background:#0EA5E9;
padding:18px;
border-radius:10px;
text-align:center;
color:white;
font-size:22px;'>

un

</div>
""",
unsafe_allow_html=True
)

cols[1].markdown(
"""
<div style='background:#10B981;
padding:18px;
border-radius:10px;
text-align:center;
color:white;
font-size:22px;'>

believ

</div>
""",
unsafe_allow_html=True
)

cols[2].markdown(
"""
<div style='background:#F97316;
padding:18px;
border-radius:10px;
text-align:center;
color:white;
font-size:22px;'>

able

</div>
""",
unsafe_allow_html=True
)

st.warning("""

Remember:

These are only **illustrations** to help understand the idea.

Real AI tokenizers may split text differently depending on the model.

The important idea is that AI often works with **pieces of text**, not always whole words.

""")

# ==========================================================
# CRICKET EXAMPLE
# ==========================================================

st.divider()

st.header("🏏 Cricket Example")

st.markdown("""

Let's take another sentence.

""")

st.success("Virat Kohli hit a beautiful cover drive.")

tokens = [
    "Virat",
    "Kohli",
    "hit",
    "a",
    "beautiful",
    "cover",
    "drive",
    "."
]

cols = st.columns(len(tokens))

colors = [
    "#2563EB",
    "#0EA5E9",
    "#10B981",
    "#F97316",
    "#8B5CF6",
    "#EF4444",
    "#14B8A6",
    "#6B7280"
]

for col, token, color in zip(cols, tokens, colors):

    col.markdown(
        f"""
<div style='
background:{color};
padding:15px;
border-radius:10px;
text-align:center;
color:white;
font-weight:bold;
'>
{token}
</div>
""",
unsafe_allow_html=True
)

st.info("""

AI predicts

one token

↓

then another token

↓

then another token

until the complete sentence is generated.

It does **NOT** create the whole paragraph at once.

""")

# ==========================================================
# BUILD A SENTENCE
# ==========================================================

st.divider()

st.header("🎮 Activity : Build The Sentence")

st.markdown("""

Press the button below.

Watch AI build a sentence

**one token at a time.**

""")

placeholder = st.empty()

if st.button("🚀 Generate Token By Token"):

    generated = [
        "Artificial",
        "Intelligence",
        "helps",
        "people",
        "solve",
        "problems",
        "faster",
        "."
    ]

    sentence = ""

    for token in generated:

        sentence += token + " "

        placeholder.markdown(f"""
# 🤖

{sentence}
""")

        time.sleep(0.7)

st.success("""

Did you notice?

The sentence appeared gradually.

Large Language Models work in a very similar way.

They keep predicting

one token,

then the next,

then the next.

""")

# ==========================================================
# BIG DISCOVERY
# ==========================================================

st.divider()

st.header("🧠 Discovery")

st.markdown("""

Today you discovered something amazing.

Humans usually read

📖 ideas.

AI reads

🧩 tokens.

Humans understand meaning.

AI predicts the next token.

Thousands of predictions happen every second.

That's how ChatGPT creates essays,

stories,

emails,

poems,

and even computer programs.

""")
# ==========================================================
# REAL WORLD AI
# ==========================================================

st.divider()

st.header("🌍 AI Prediction Is Everywhere")

st.markdown("""

Many people think ChatGPT is the only AI.

Actually...

AI prediction is already part of your daily life.

Let's explore.

""")

# ----------------------------------------------------------

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
### ⌨️ Google Keyboard

When you type,

your keyboard predicts

the next word.

Example:

I am going ______

👉 home

👉 there

👉 now

""")

with col2:

    st.markdown("""
### 🎬 YouTube

YouTube predicts

which video

you are most likely

to watch next.

""")

with col3:

    st.markdown("""
### 📷 Instagram

Instagram predicts

which Reel

you'll probably watch

for the longest time.

""")

# ----------------------------------------------------------

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
### 🎵 Spotify

Spotify predicts

which song

you might enjoy next.

""")

with col2:

    st.markdown("""
### 🎥 Netflix

Netflix predicts

which movie

you may like.

""")

with col3:

    st.markdown("""
### 🛒 Amazon

Amazon predicts

which products

you may buy.

""")

st.success("""

Prediction is one of the biggest ideas behind modern AI.

Different companies predict different things.

ChatGPT predicts words.

YouTube predicts videos.

Netflix predicts movies.

Spotify predicts songs.

Amazon predicts products.

""")

# ==========================================================
# CAN AI BE WRONG?
# ==========================================================

st.divider()

st.header("🤔 Can AI Ever Be Wrong?")

st.markdown("""

Think carefully.

Does prediction always guarantee

the correct answer?

""")

choice = st.radio(

    "What do you think?",

    [

        "AI is always correct",

        "AI can sometimes be wrong"

    ],

    key="wrong"

)

if st.button("Reveal Truth"):

    if choice=="AI can sometimes be wrong":

        st.success("Excellent! 🎉")

    else:

        st.warning("Interesting thought!")

    st.info("""

Even the smartest AI

can make mistakes.

Why?

Because prediction

is not certainty.

Sometimes

the highest probability

is still wrong.

That's why humans should always

check important information.

""")

# ==========================================================
# INTERACTIVE EXAMPLE
# ==========================================================

st.divider()

st.header("🎮 Prediction Game")

st.markdown("""

Imagine you have never seen

snow before.

Would you correctly predict

how it feels?

Probably not.

Prediction depends on

experience and data.

AI also depends on

the data it has learned from.

""")

level = st.slider(

    "How much information does AI have?",

    0,

    100,

    50

)

st.progress(level)

if level>80:

    st.success("""

Lots of examples.

Prediction becomes much better.

""")

elif level>40:

    st.warning("""

Some examples.

Prediction improves,

but mistakes are still possible.

""")

else:

    st.error("""

Very little data.

Prediction becomes difficult.

""")

# ==========================================================
# MYTH VS FACT
# ==========================================================

st.divider()

st.header("🧠 Myth vs Fact")

myth = st.selectbox(

    "Choose a statement",

    [

        "AI understands everything",

        "AI has feelings",

        "AI predicts patterns",

        "AI never makes mistakes"

    ]

)

if myth=="AI understands everything":

    st.error("❌ Myth")

    st.success("""

AI predicts patterns.

It does not understand

the world exactly

like humans.

""")

elif myth=="AI has feelings":

    st.error("❌ Myth")

    st.success("""

AI can generate emotional language.

But it does not

feel happiness,

sadness,

love,

or pain.

""")

elif myth=="AI predicts patterns":

    st.success("✅ Fact")

    st.info("""

This is one of the most important ideas

behind Large Language Models.

""")

else:

    st.error("❌ Myth")

    st.success("""

Even the best AI

can sometimes be wrong.

Always think critically.

""")

# ==========================================================
# HUMAN VS AI
# ==========================================================

st.divider()

st.header("🧠 Human Brain vs AI")

col1,col2=st.columns(2)

with col1:

    st.subheader("👨 Human")

    st.write("""

❤️ Feelings

🧠 Understanding

🎨 Creativity

👀 Experience

😊 Emotions

🤝 Common Sense

""")

with col2:

    st.subheader("🤖 AI")

    st.write("""

📊 Patterns

🎲 Probability

🔢 Mathematics

⚡ Prediction

💾 Data

🧩 Tokens

""")

st.info("""

Humans and AI can produce

similar answers.

But the way they reach

those answers

is completely different.

""")

# ==========================================================
# DAILY LIFE CHALLENGE
# ==========================================================

st.divider()

st.header("🏠 Daily Life Challenge")

st.markdown("""

Look around your home today.

Can you find

THREE places

where prediction is happening?

Examples:

✅ Mobile Keyboard

✅ YouTube

✅ Netflix

✅ Amazon

✅ Google Maps

Write your answers below.

""")

challenge = st.text_area(

    "My Three Examples"

)

if st.button("Submit Challenge"):

    st.success("""

Excellent observation!

Once you start noticing AI,

you'll realize

prediction is everywhere.

""")

# ==========================================================
# MINI QUIZ
# ==========================================================

st.divider()

st.header("🎯 Mission Quiz")

st.markdown("""
Let's see how much you've discovered.

No pressure.

Think carefully before answering.
""")

score = 0

# ----------------------------------------------------------

q1 = st.radio(

    "1️⃣ ChatGPT mainly works by...",

    [

        "Remembering every book",

        "Predicting the next token",

        "Searching Google",

        "Thinking like humans"

    ],

    key="quiz1"

)

if q1 == "Predicting the next token":
    score += 1

# ----------------------------------------------------------

q2 = st.radio(

    "2️⃣ Which word is most likely after 'I drink tea with ____' ?",

    [

        "Milk",

        "Brick",

        "Rocket",

        "Television"

    ],

    key="quiz2"

)

if q2 == "Milk":
    score += 1

# ----------------------------------------------------------

q3 = st.radio(

    "3️⃣ AI predictions are based on",

    [

        "Magic",

        "Probability",

        "Luck",

        "Feelings"

    ],

    key="quiz3"

)

if q3 == "Probability":
    score += 1

# ----------------------------------------------------------

q4 = st.radio(

    "4️⃣ AI reads language using",

    [

        "Dreams",

        "Tokens",

        "Pictures",

        "Thoughts"

    ],

    key="quiz4"

)

if q4 == "Tokens":
    score += 1

# ----------------------------------------------------------

if st.button("🏆 Check My Score"):

    st.metric(
        "Your Score",
        f"{score}/4"
    )

    if score == 4:

        st.balloons()

        st.success("""
Outstanding!

You understood one of the biggest ideas behind
Large Language Models.
""")

    elif score >= 3:

        st.success("""
Excellent!

You're becoming an AI Explorer.
""")

    else:

        st.warning("""
Great effort!

Scroll through the mission once more.

You'll definitely get it.
""")

# ==========================================================
# REFLECTION WALL
# ==========================================================

st.divider()

st.header("🪞 Reflection Wall")

st.markdown("""

Scientists don't finish an experiment
without reflecting.

Take a moment.

Think.

Then answer honestly.

""")

reflection1 = st.text_area(

    "🤔 What surprised you the most?"

)

reflection2 = st.text_area(

    "💡 What became clearer today?"

)

reflection3 = st.text_area(

    "🌍 Where do you see prediction in everyday life?"

)

reflection4 = st.text_area(

    "🚀 If you could improve ChatGPT, what would you add?"

)

if st.button("Save Reflection"):

    st.success("""
Excellent!

Curiosity is the beginning of intelligence.

Keep asking questions.
""")

# ==========================================================
# BIG SUMMARY
# ==========================================================

st.divider()

st.header("🧠 Mission Summary")

summary = {
    "Concept":[
        "Prediction",
        "Probability",
        "Tokens",
        "Patterns",
        "Large Language Models"
    ],
    "What You Learned":[
        "AI predicts the next token",
        "Every possible answer has a probability",
        "AI reads tokens instead of full ideas",
        "AI learns patterns from data",
        "ChatGPT is a Large Language Model"
    ]
}

import pandas as pd

st.dataframe(
    pd.DataFrame(summary),
    use_container_width=True
)

# ==========================================================
# FINAL MESSAGE
# ==========================================================

st.divider()

st.markdown("""
<div style='
background:linear-gradient(90deg,#2563EB,#06B6D4);
padding:35px;
border-radius:20px;
color:white;
text-align:center;
'>

<h1>🎉 Mission Complete</h1>

<h2>You Have Discovered Something Amazing.</h2>

AI does not magically know answers.

It predicts.

One token at a time.

Every sentence.

Every paragraph.

Every story.

</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# LEVEL UP
# ==========================================================

st.success("""
🏅 Achievement Unlocked

AI Explorer

Level 2
""")

st.progress(40)

st.info("""
Mission Progress

████░░░░░░░

40%
""")

# ==========================================================
# THINK DEEPLY
# ==========================================================

st.divider()

st.header("💭 Before You Leave...")

st.markdown("""

Take 30 seconds.

Close your eyes.

Think.

Every sentence you have spoken today...

Your brain predicted it.

Every sentence ChatGPT generates...

It predicts it too.

Humans and AI both predict.

But...

Humans understand meaning.

AI predicts patterns.

That small difference
changes everything.

""")

# ==========================================================
# PREVIEW
# ==========================================================

st.divider()

st.header("🚀 Next Mission")

st.markdown("""

# Mission 3

## Prompt Engineering

Today you learned

how AI predicts.

Next,

you'll discover something even more powerful.

You'll learn

how to ask better questions.

Because...

The quality of AI's answer

depends on

the quality of your prompt.

""")

st.success("""

Coming Up Next

🎯 Good Prompt vs Bad Prompt

🎯 GOLD Framework

🎯 Prompt Builder

🎯 AI Playground

🎯 Prompt Competition

""")

# ==========================================================
# HOMEWORK
# ==========================================================

st.divider()

st.header("🏠 Mission Homework")

st.markdown("""

Tonight,

Open any AI assistant.

Ask one simple question.

Example:

Tell me about water.

Now improve it.

Explain water

to a Class 5 student

using cricket examples

in Hindi

within 100 words

using emojis.

Compare both answers.

Tomorrow,

tell us

which answer was better

and WHY.

""")

st.success("""
Mission 2 Successfully Completed.

See you in Mission 3!
""")
