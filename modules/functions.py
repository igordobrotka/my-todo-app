FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reading lines from a todos text file."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Writing the text from a list in the code
    back to the todos text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__== ("__main__"):
    print("Hello")
