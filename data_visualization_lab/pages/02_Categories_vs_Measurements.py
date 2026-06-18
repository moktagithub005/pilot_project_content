import streamlit as st

st.title("🎯 Categories vs Measurements")

st.subheader("Imagine Your Classroom")

question = st.radio(
    "Choose a question:",
    [
        "What is your favourite sport?",
        "What is your height?"
    ]
)

if question == "What is your favourite sport?":

    st.success(
        """
Answers can be:

Cricket
Football
Basketball
Badminton
"""
    )

    st.write("Can we calculate average sport?")

    if st.button("Check"):
        st.error(
            """
No!

Because these are labels.

This is called Categorical Data.
"""
        )

else:

    st.success(
        """
Answers can be:

150 cm
155 cm
160 cm
165 cm
"""
    )

    st.write("Can we calculate average height?")

    if st.button("Check Height"):
        st.success(
            """
Yes!

Average Height = Possible

This is Numerical Data.
"""
        )