import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Todo App")
st.subheader("Manage your time efficiently")
st.write("A simple to do list to manage it all")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key="td")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[td]
        st.rerun()


st.text_input(label="", placeholder="Enter new todo",
              on_change=add_todo, key='new_todo')
