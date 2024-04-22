import streamlit as st
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create the students table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS students (name TEXT, class_course TEXT, syllabus_link TEXT, mode_of_student TEXT)''')

# Add a submit button to insert the user's input into the database
if st.button('Submit'):
    name = st.text_input('Name')
    class_course = st.text_input('Class/Course')
    syllabus_link = st.text_input('Syllabus Link')
    mode_of_student = st.selectbox('Mode of Student', ['Online', 'Offline'])

    # Insert the user's input into the database
    c.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (name, class_course, syllabus_link, mode_of_student))
    conn.commit()

# Close the database connection
conn.close()

# Add a button to display the data in the database
if st.button('Show Data'):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    # Fetch all data from the students table
    c.execute("SELECT * FROM students")
    rows = c.fetchall()

    # Display the data in a table
    st.write("Name | Class/Course | Syllabus Link | Mode of Student")
    st.write("----|--------------|---------------|-----------------")
    for row in rows:
        st.write(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

    # Close the database connection
    conn.close()
