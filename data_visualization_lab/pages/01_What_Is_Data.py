import streamlit as st

st.set_page_config(page_title="What is Data?", page_icon="📊")

st.title("🕵️ Data Detective Lab")
st.header("Chapter 1: What is Data?")

st.divider()

st.subheader("🤔 Let's Think")

st.write(
    """
Imagine your school principal asks:

'Which subject is most loved by students?'

Can he ask every student every day?

No.

So he collects information.

That information is called DATA.
"""
)

st.info(
    """
Data = Facts collected from the real world.
"""
)

st.divider()

st.subheader("🎮 Activity 1")

name = st.text_input("Enter your name")

favorite_subject = st.selectbox(
    "Select your favourite subject",
    [
        "Maths",
        "Science",
        "English",
        "Computer",
        "Social Science"
    ]
)

study_hours = st.slider(
    "How many hours do you study daily?",
    0,
    10,
    2
)

if st.button("Submit Data"):
    st.success("Data Collected Successfully!")

    st.write("### Your Data")

    st.write(f"👤 Name: {name}")
    st.write(f"📚 Favourite Subject: {favorite_subject}")
    st.write(f"⏰ Study Hours: {study_hours}")