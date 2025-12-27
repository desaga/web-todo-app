import streamlit as st
from utils import read_todos, save_todos

print("Started again")
todos = read_todos()

def add_todo():
    todo = st.session_state["add_todo"].strip().capitalize()
    todos.append(todo)
    save_todos(todos)

st.title("My todo app")
st.write("This is a TODO app")
for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        save_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Enter new todo",
              on_change=add_todo, key='add_todo')
