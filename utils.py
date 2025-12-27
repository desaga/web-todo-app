import os


TODOS_FILE_NAME = 'todos.txt'

def save_todos(todo_list):
    """"Saves a 'todos' list to the file
    params: todos [list]
    output: None
    """
    file = open(TODOS_FILE_NAME, 'w')
    file.writelines((task + '\n' for task in todo_list))
    file.close()

def read_todos():
    if not os.path.exists(TODOS_FILE_NAME):
        with open(TODOS_FILE_NAME, 'w') as file:
            pass
    file = open(TODOS_FILE_NAME, 'r')
    lines = [line.strip() for line in file.readlines()]
    return lines

def show_todos(todo_list):
    if todo_list:
        print("\nYour todos:")
        for i, item in enumerate(todo_list, start=1):
            print(f"{i}.'{item}'")
        print()
    else:
        print("Your todo list is empty.\n")