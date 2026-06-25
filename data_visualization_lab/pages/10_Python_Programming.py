import streamlit as st

st.title("🐍 Python Programming Adventure")

st.markdown("""
# Welcome Future Programmers!

Before we learn Python,

let's understand:

### What is Programming?

Programming is simply:

Giving instructions to a computer.

Just like giving instructions to a friend,
a robot,
or following a recipe.
""")

st.divider()

st.header("☕ Programming Without Computers")

st.markdown("""
Imagine I ask:

### How To Make Tea?

Can we write the steps?
""")

tea_steps = [
    "Take a Pan",
    "Add Water",
    "Boil Water",
    "Add Tea Leaves",
    "Add Milk",
    "Serve Tea"
]

for i, step in enumerate(tea_steps, start=1):
    st.write(f"{i}. {step}")

st.success("""
Notice something?

The steps must happen in order.

Computers work exactly the same way.

They follow instructions step-by-step.
""")

st.divider()

st.header("🤖 Human Robot Activity")


st.info("""
Imagine a robot is standing in front of you.

You say:

'Go pick up the notebook.'

Can the robot do it?

Maybe not.

Computers need very specific instructions.
""")


instructions = [
    "Move Forward 3 Steps",
    "Turn Right",
    "Bend Down",
    "Pick Up Notebook"
]

for step in instructions:
    st.write("➡️", step)

st.warning("""
Computers do not understand vague instructions.

They need clear instructions.

Always.
""")


st.divider()

st.header("🧩 What Is An Algorithm?")


st.markdown("""
Algorithm means:

### A sequence of steps used to solve a problem.
""")

daily_routine = [
    "Wake Up",
    "Brush Teeth",
    "Take Bath",
    "Eat Breakfast",
    "Go To School"
]

st.write("Morning Routine Algorithm")

for i, step in enumerate(daily_routine, start=1):
    st.write(f"{i}. {step}")


st.success("""
Algorithms are everywhere.

Google Maps uses algorithms.

Instagram uses algorithms.

YouTube uses algorithms.

Even your morning routine is an algorithm.
""")


st.divider()

st.header("🌍 Programming Is Everywhere")


apps = [
    "📱 Instagram",
    "▶️ YouTube",
    "🗺️ Google Maps",
    "🎮 Games",
    "🤖 ChatGPT",
    "🚗 Self Driving Cars"
]

for app in apps:
    st.write(app)



st.info("""
All these applications were built using programming.
""")


st.divider()

st.header("🎉 My First Python Program")


if st.button("Run Program"):
    st.success("Hello Students")


st.write("""
This is our first Python program.

print() means:

Display something on the screen.
""")


st.divider()

st.header("📦 Variables")

st.markdown("""
Imagine a school bag.

A school bag stores books.

A water bottle stores water.

A variable stores information.

Variable = Container
""")


st.code(
'''
name = "Rahul"
''',
language="python"
)


st.info("""
Container Name = name

Value Inside = Rahul
""")


student_name = st.text_input(
    "Enter Your Name"
)

if student_name:
    st.success(
        f"Stored Inside Variable: {student_name}"
    )

st.divider()

st.header("📥 Input and 📤 Output")

st.write("""
Input means:

Information enters the computer.

Output means:

Information comes out of the computer.
""")


st.code(
'''
name = input("Enter your name: ")

print("Welcome", name)
''',
language="python"
)

name = st.text_input(
    "What is your name?",
    key="name_input"
)

if name:
    st.success(
        f"Welcome {name}"
    )


st.divider()

st.header("🚀 Build Your First Program")

student = st.text_input(
    "Student Name",
    key="student"
)

age = st.slider(
    "Age",
    10,
    20,
    15
)

subject = st.selectbox(
    "Favorite Subject",
    [
        "Math",
        "Science",
        "English",
        "Computer Science"
    ]
)


if st.button("Create My Program"):
    st.success(f"""
Hello {student}

Age: {age}

Favorite Subject: {subject}

Welcome To Python Programming!
""")
    

st.divider()

st.header("🎮 Python Playground")


number = st.slider(
    "Choose a Number",
    1,
    20,
    5
)


st.write("Double =", number * 2)

st.write("Triple =", number * 3)

st.write("Square =", number ** 2)


st.info("""
The computer can perform calculations instantly.

This is one reason programming is powerful.
""")


st.divider()

st.header("🧠 Quick Quiz")


st.divider()

st.header("🧠 Quick Quiz")


q1 = st.radio(
    "What is Programming?",
    [
        "Drawing Pictures",
        "Giving Instructions To A Computer",
        "Playing Games"
    ]
)

if q1 == "Giving Instructions To A Computer":
    st.success("Correct!")


q2 = st.radio(
    "What is a Variable?",
    [
        "A Container",
        "A Computer",
        "A Monitor"
    ]
)

if q2 == "A Container":
    st.success("Excellent!")


q3 = st.radio(
    "What is an Algorithm?",
    [
        "A Sequence Of Steps",
        "A Song",
        "A Movie"
    ]
)

if q3 == "A Sequence Of Steps":
    st.success("Great Job!")


st.divider()

st.success("""
🎉 Congratulations!

Today You Learned:

✅ Programming

✅ Algorithms

✅ Variables

✅ Input

✅ Output

✅ Your First Python Program

Remember:

Programming is not about memorizing code.

Programming is about solving problems step-by-step.

Every programmer started exactly where you are today.
""")


st.divider()

st.title("🧮 Class 3: Teaching Computers Mathematics")

st.header("🎯 Quick Revision")

q1 = st.radio(
    "What is a Variable?",
    [
        "A Container",
        "A Calculator",
        "A Computer"
    ],
    key="math_quiz_1"
)

if q1 == "A Container":
    st.success("✅ Correct! Variables store information.")



q2 = st.radio(
    "What is Input?",
    [
        "Information entering the computer",
        "Information displayed by the computer"
    ],
    key="math_quiz_2"
)

if q2 == "Information entering the computer":
    st.success("✅ Excellent!")


st.divider()

st.header("🤔 Can Computers Do Mathematics?")


st.markdown("""
Imagine I ask:

### What is 25 × 45 ?

Most of us need a few seconds.

Let's ask Python.
""")


st.code(
"""
print(25 * 45)
""",
language="python"
)

if st.button("Run Python Calculation"):
    st.success("1125")



st.info("""
Computers are basically super-fast calculators.

But they need instructions from us.
""")


st.divider()

st.header("📦 Different Types of Data")


st.markdown("""
Look at these three values:

Rahul

16

85.5

Are they all the same?
""")


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Name", "Rahul")

with col2:
    st.metric("Age", "16")

with col3:
    st.metric("Marks", "85.5")


st.success("""
Computers store different kinds of information.

These are called DATA TYPES.
""")


st.code(
'''
name = "Rahul"
city = "Delhi"
''',
language="python"
)


text_input = st.text_input(
    "Enter Any Text",
    "Hello Python"
)

st.write("String Stored:", text_input)


st.subheader("🔢 Integer")



st.write("""
Whole Numbers

Examples:

10

25

100
""")


age = st.slider(
    "Choose Age",
    1,
    100,
    16
)

st.write("Integer Value =", age)


st.subheader("🎯 Float")

marks = st.slider(
    "Marks With Decimal",
    0.0,
    100.0,
    85.5
)

st.write("Float Value =", marks)


st.success("""
String → Text

Integer → Whole Number

Float → Decimal Number
""")

st.divider()

st.header("🧮 Mathematics Playground")

num1 = st.number_input(
    "Enter First Number",
    value=10
)

num2 = st.number_input(
    "Enter Second Number",
    value=5
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Addition",
        num1 + num2
    )

    st.metric(
        "Subtraction",
        num1 - num2
    )

with col2:

    st.metric(
        "Multiplication",
        num1 * num2
    )

    if num2 != 0:
        st.metric(
            "Division",
            round(num1 / num2,2)
        )

st.info("""
Python already knows mathematics.

We simply tell it what to calculate.
""")


st.divider()

st.header("📦 Variables Doing Mathematics")

st.code(
"""
a = 10
b = 20

print(a + b)
""",
language="python"
)

a = st.slider(
    "Variable a",
    0,
    100,
    10
)

b = st.slider(
    "Variable b",
    0,
    100,
    20
)


st.write("a =", a)

st.write("b =", b)

st.success(
    f"a + b = {a+b}"
)

st.markdown("""
Python looks inside:

a → value

b → value

Then performs the calculation.
""")

st.divider()

st.header("🚀 Build Your First Calculator")

st.code(
"""
num1 = int(input("Enter first number"))

num2 = int(input("Enter second number"))

sum = num1 + num2

print(sum)
""",
language="python"
)

c1 = st.number_input(
    "First Number",
    value=20,
    key="calc1"
)

c2 = st.number_input(
    "Second Number",
    value=30,
    key="calc2"
)

if st.button("Calculate Sum"):
    st.success(
        f"Answer = {c1+c2}"
    )

st.balloons()

st.success("""
🎉 Congratulations!

You just built a calculator.
""")


math_marks = st.slider(
    "Math Marks",
    0,
    100,
    80
)

science_marks = st.slider(
    "Science Marks",
    0,
    100,
    90
)

english_marks = st.slider(
    "English Marks",
    0,
    100,
    75
)

total = (
    math_marks
    + science_marks
    + english_marks
)

average = total / 3

col1,col2 = st.columns(2)

with col1:
    st.metric(
        "Total Marks",
        total
    )

with col2:
    st.metric(
        "Average",
        round(average,2)
    )

st.success("""
You just created a Marks Calculator.

This is exactly how real software performs calculations.
""")

st.divider()

st.header("🎯 What Did We Learn Today?")
import pandas as pd

summary_df = pd.DataFrame({
    "Concept":[
        "String",
        "Integer",
        "Float",
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Calculator"
    ],
    "Meaning":[
        "Text",
        "Whole Number",
        "Decimal Number",
        "+",
        "-",
        "*",
        "/",
        "Math Program"
    ]
})

st.table(summary_df)

st.success("""
🎉 Congratulations!

Today You Learned:

✅ Data Types

✅ String

✅ Integer

✅ Float

✅ Mathematical Operations

✅ Variables With Numbers

✅ How To Build A Calculator

Programming is becoming powerful now.

Next Class:

🤔 Decision Making

IF it rains → Take Umbrella

ELSE → Enjoy Sunshine

This is where computers start making decisions!
""")

st.divider()

st.title("🤔 Class 4: Decision Making (if-else)")

st.header("☂️ Decisions Are Everywhere")

st.markdown("""
Before learning Python,

let's think about real life.

### When do you carry an umbrella?

👉 If it rains

You carry an umbrella.

👉 If it does not rain

You don't carry an umbrella.

Congratulations!

You just used if-else logic.
""")

weather = st.selectbox(
    "Choose Today's Weather",
    [
        "☀️ Sunny",
        "🌧 Rainy"
    ]
)

if weather == "🌧 Rainy":
    st.success("Take an Umbrella ☂️")
else:
    st.info("Enjoy Your Day 😎")

st.divider()

st.header("🔍 What Is A Condition?")


number = st.slider(
    "Choose a Number",
    0,
    20,
    10,
    key="condition_demo"
)

if number > 10:
    st.success("Condition TRUE")
else:
    st.error("Condition FALSE")


st.info("""
The computer checks:

Is Number > 10 ?

If yes → TRUE

If no → FALSE
""")

st.divider()

st.header("🎮 Comparison Operators")


comparison_df = pd.DataFrame({
    "Operator":[
        ">",
        "<",
        "==",
        "!=",
        ">=",
        "<="
    ],
    "Meaning":[
        "Greater Than",
        "Less Than",
        "Equal To",
        "Not Equal To",
        "Greater Than Equal To",
        "Less Than Equal To"
    ]
})

st.table(comparison_df)

st.subheader("🧠 True or False?")


answer = st.radio(
    "Is 15 > 10 ?",
    ["True","False"],
    key="tf1"
)

if answer == "True":
    st.success("Correct! 🎉")


answer2 = st.radio(
    "Is 5 > 20 ?",
    ["True","False"],
    key="tf2"
)

if answer2 == "False":
    st.success("Excellent! 🎉")


st.divider()

st.header("🚀 Your First IF Statement")


st.code(
"""
marks = 95

if marks > 90:
    print("Excellent")
""",
language="python"
)


marks_demo = st.slider(
    "Student Marks",
    0,
    100,
    95
)


if marks_demo > 90:
    st.success("Excellent 🌟")
else:
    st.warning("Condition False → Nothing Happens")


st.info("""
Python asks:

Is marks > 90 ?

If TRUE:

Run the code

If FALSE:

Skip the code
""")

st.divider()

st.header("🧠 How The Computer Thinks")


st.markdown(f"""
```text
Marks = {marks_demo}

       |
       v

Is Marks > 90 ?

       |
    TRUE / FALSE
       |
       v

""")

st.divider()

st.header("🔀 If Else Statement")

st.code(
"""
marks = 70

if marks > 90:
    print("Excellent")
else:
    print("Keep Working")
""",
language="python"
)

marks_ifelse = st.slider(
    "Choose Marks",
    0,
    100,
    70,
    key="ifelse_marks"
)

if marks_ifelse > 90:
    st.success("🌟 Excellent")
else:
    st.info("📚 Keep Working")


st.markdown("""
Decision Tree:

```text
        Marks > 90 ?

          /     \

        YES      NO

         |        |

    Excellent  Keep Working
""")

age = st.slider(
    "Enter Age",
    1,
    100,
    15,
    key="vote_age"
)

if age >= 18:
    st.success("✅ You Can Vote")
else:
    st.error("❌ You Cannot Vote Yet")

st.code(
"""
age = int(input("Enter age"))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
""",
language="python"
)

st.divider()

st.header("🌡 Weather Decision System")

temp = st.slider(
    "Today's Temperature",
    0,
    50,
    25
)

if temp > 30:
    st.error("🔥 Hot Day")
else:
    st.success("🌤 Pleasant Day")

st.code(
"""
temperature = int(input())

if temperature > 30:
    print("Hot Day")
else:
    print("Pleasant Day")
""",
language="python"
)

st.divider()

st.header("🤖 Build Your Own Decision Machine")

study_hours = st.slider(
    "Study Hours",
    0,
    10,
    5
)

if study_hours >= 6:
    st.success("🌟 Good Preparation")
else:
    st.warning("📚 Study More")

st.info("""
You just created your own AI-like rule.

IF Study Hours >= 6

THEN Good Preparation

ELSE Study More
""")

st.divider()

st.header("⚠️ Common Beginner Mistakes")

mistakes_df = pd.DataFrame({
    "Wrong":[
        "if marks = 90",
        "if marks > 90",
        "No Indentation"
    ],
    "Correct":[
        "if marks == 90",
        "if marks > 90:",
        "Use spaces before print"
    ]
})

st.table(mistakes_df)

st.divider()

st.header("🎯 What Did We Learn Today?")

summary_df = pd.DataFrame({
    "Concept":[
        "Condition",
        "if",
        "else",
        "TRUE",
        "FALSE"
    ],
    "Meaning":[
        "Something we check",
        "Run code if true",
        "Run code if false",
        "Condition satisfied",
        "Condition not satisfied"
    ]
})

st.table(summary_df)

st.success("""
🎉 Congratulations!

Today You Learned:

✅ Conditions

✅ Comparison Operators

✅ IF Statements

✅ IF-ELSE Statements

✅ Decision Making

Computers do not think like humans.

They simply follow rules.

Next Class:

🚀 Multiple Decisions (if-elif-else)

Where we will build:

⭐ Grade Calculator

⭐ Smart Result System

⭐ Menu Driven Programs

⭐ Real Software Logic
""")

st.divider()
st.header("🚀 Try It Yourself #1 : Grade Calculator")

st.info("""
👨‍🏫 Teachers assign grades based on marks.

90+  → Grade A

75+  → Grade B

60+  → Grade C

40+  → Grade D

Below 40 → Fail
""")

st.subheader("💻 Python Program")

st.code("""
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Fail")
""", language="python")

marks = st.slider(
    "Enter Marks",
    0,
    100,
    75
)

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    grade = "D"

else:
    grade = "Fail"

st.success(f"Grade = {grade}")

st.info("""
if

means first check

elif

means check another condition

else

means if everything fails
""")

st.divider()

st.header("🚀 Try It Yourself #2 : Student Attendance Register")

st.markdown("""
### Class Register

1. Rahul

2. Priya

3. Aman

4. Riya
""")

st.code("""
students = [
    "Rahul",
    "Priya",
    "Aman",
    "Riya"
]

print(students)
""", language="python")


students = [
    "Rahul",
    "Priya",
    "Aman",
    "Riya"
]

st.write(students)

st.info("""
Think of a large apartment building.

Every apartment has a number.

Similarly every item inside a list has an index.

Rahul → 0

Priya → 1

Aman → 2

Riya → 3
""")

st.code("""
students = [
    "Rahul",
    "Priya",
    "Aman",
    "Riya"
]

print(students)
""", language="python")

students = [
    "Rahul",
    "Priya",
    "Aman",
    "Riya"
]

st.write(students)


st.info("""
Think of a large apartment building.

Every apartment has a number.

Similarly every item inside a list has an index.

Rahul → 0

Priya → 1

Aman → 2

Riya → 3
""")

index = st.slider(
    "Choose Index",
    0,
    3,
    0
)

st.success(
    f"Student = {students[index]}"
)

st.divider()

st.header("🚀 Try It Yourself #3 : Add New Student")

new_student = st.text_input(
    "Enter New Student Name"
)

student_list = [
    "Rahul",
    "Priya",
    "Aman"
]

if new_student:

    student_list.append(new_student)

    st.success(student_list)

st.info("""
append()

means

Add a new item at the end of the list.
""")

st.divider()

st.header("🚀 Try It Yourself #4 : Repeating Work")

st.write("""
Write:

I will complete my homework

5 times.
""")

st.code("""
for i in range(5):
    print("I will complete my homework")
""", language="python")

repeat = st.slider(
    "How Many Times?",
    1,
    20,
    5
)

for i in range(repeat):

    st.write(
        "📚 I will complete my homework"
    )

st.info("""
for

means

Repeat
Repeat
Repeat
Repeat
""")

st.divider()

st.header("🚀 Try It Yourself #5 : Counting Machine")

number = st.slider(
    "Count Up To",
    1,
    20,
    5
)

for i in range(number):

    st.write(i)

st.info("""
Python changes i automatically.

Loop 1 → i = 0

Loop 2 → i = 1

Loop 3 → i = 2

...
""")

st.divider()

st.header("🚀 Try It Yourself #6 : Visit Every Student")

students = [
    "Rahul",
    "Priya",
    "Aman"
]

st.code("""
for student in students:

    print(student)
""", language="python")

for student in students:

    st.success(student)

st.info("""
Loop Visits:

Rahul
 ↓

Priya
 ↓

Aman
""")

st.divider()

st.header("🚀 Try It Yourself #7 : Student ID Card")

student = {
    "name":"Rahul",
    "age":16,
    "city":"Shimla"
}

st.json(student)

key = st.selectbox(
    "Choose Information",
    [
        "name",
        "age",
        "city"
    ]
)

st.success(
    student[key]
)

st.info("""
Dictionary

Key → Value

name → Rahul

age → 16

city → Shimla

Just like a real dictionary.
""")

st.divider()

st.header("🚀 Try It Yourself #8 : Fixed Information")

months = (
    "January",
    "February",
    "March"
)

st.write(months)

st.success("""
[] = List

Can Change

()

Tuple

Usually Fixed
""")

st.divider()

st.title("🏆 Mini Project : Student Grade System")

students = [
    {"name":"Rahul","marks":92},
    {"name":"Priya","marks":78},
    {"name":"Aman","marks":55}
]

results = []

for student in students:

    marks = student["marks"]

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 40:
        grade = "C"

    else:
        grade = "Fail"

    results.append(
        {
            "Name":student["name"],
            "Marks":marks,
            "Grade":grade
        }
    )
import pandas as pd

st.dataframe(
    pd.DataFrame(results),
    use_container_width=True
)

st.divider()

st.title("🎓 What Have We Learned?")

summary = pd.DataFrame({
    "Concept":[
        "Variable",
        "Input",
        "Output",
        "If Else",
        "List",
        "Loop",
        "Dictionary",
        "Tuple"
    ],
    "Meaning":[
        "Stores Data",
        "Information Enters",
        "Information Displays",
        "Decision Making",
        "Collection Of Items",
        "Repeat Work",
        "Key-Value Data",
        "Fixed Data"
    ]
})

st.table(summary)

st.success("""
Programming is not about memorizing code.

Programming is about solving problems.

Step by step.

Just like humans solve problems.
""")