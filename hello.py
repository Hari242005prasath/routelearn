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

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.experimental_memo to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT 10")

# Print results.
st.write("Some wise words from Shakespeare:")
for row in rows:
    st.write("✍️ " + row['word'])
