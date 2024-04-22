import streamlit as st

# Welcome users to the app
st.title("RouteLearn: Study Scheduling App")
st.write("Welcome to RouteLearn, the study scheduling app that will help you manage your daily study commitments and excel academically!")

# Allow users to enter their course information
course_names = st.text_input("Enter the names of the courses you are taking, separated by commas:")
syllabus_urls = st.text_input("Enter the URLs of your course syllabi:")
exam_dates = st.date_input("Enter the dates of your exams:")

# Analyze the user's learning style and create a personalized study plan
learning_style = st.radio("Select your learning style:", ("Visual", "Auditory", "Reading/Writing", "Kinesthetic"))

if learning_style == "Visual":
    study_plan = "Create flashcards and use diagrams to help you study."
elif learning_style == "Auditory":
    study_plan = "Record yourself reading your notes and listen to them to help you study."
elif learning_style == "Reading/Writing":
    study_plan = "Take detailed notes and rewrite them to help you study."
elif learning_style == "Kinesthetic":
    study_plan = "Use hands-on activities and simulations to help you learn."

# Display the study plan to the user
st.write("Based on your learning style, your study plan is:")
st.write(study_plan)

# Allow users to prioritize their study tasks
task_list = st.text_area("Enter a list of your study tasks, separated by commas:")
priority_levels = st.slider("Select the priority level for each task:", min_value=1, max_value=5)

# Display the prioritized task list to the user
sorted_tasks = sorted(zip(priority_levels, task_list), reverse=True)
st.write("Your prioritized task list is:")
for priority, task in sorted_tasks:
    st.write(f"{priority}: {task}")

# Offer rewards and reminders to the user
rewards = st.slider("Select the rewards you will give yourself for completing tasks:", min_value=1, max_value=5)
deadline_reminders = st.date_input("Enter the dates for your deadline reminders:")

# Display the rewards and reminders to the user
st.write("Your rewards and deadline reminders are:")
st.write(f"Rewards: {rewards}")
st.write(f"Deadline reminders: {deadline_reminders}")

