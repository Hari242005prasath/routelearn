import streamlit as st

# Create a list to hold our to-do items
todo_list = []

# Streamlit app title and description
st.title('To-Do List App')
st.write('Welcome to a simple to-do list app!')

# Input field to add new to-do items
new_item = st.text_input('Add new item', '')

# Add button to add the new item to the list
if st.button('Add'):
    if new_item:
        todo_list.append(new_item)
        st.success('Item added successfully!')
    else:
        st.warning('Please enter a valid item.')

# Display the current to-do list
st.write('### Your To-Do List:')
if not todo_list:
    st.write('Your list is empty.')
else:
    for i, item in enumerate(todo_list, start=1):
        st.write(f'{i}. {item}')

# Checkbox to remove completed items
if st.checkbox('Click to remove completed items'):
    items_to_remove = [item for item in todo_list if st.checkbox(f'Complete: {item}', key=item)]
    if items_to_remove:
        for item in items_to_remove:
            todo_list.remove(item)
        st.success('Selected items removed.')

