def get_todos(filepath='Files/TDL.txt'):  # Default parameter, you can only tell coffee, not coffee in a cup.
    """Read a text file and return a list of Todos"""  # How to add documentation. Docstrings.
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = 'Files/TDL.txt'):
    """Writes the todos in the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



if __name__ == '__main__':
    print('Hello')
    print(get_todos())
