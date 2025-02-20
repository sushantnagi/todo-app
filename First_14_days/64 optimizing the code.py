def get_todos(filepath='Files/TDL.txt'):  # Default parameter, you can only tell coffee, not coffee in a cup.
    """Read a text file and return a list of Todos"""  # How to add documentation. Docstrings.
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = 'Files/TDL.txt'):
    """Writes the todos in the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_input = input('Enter add, show, edit, complete or exit: ')
    user_input = user_input.strip()
    user_input = user_input.lower()

    if user_input.startswith('add'):
        task = user_input[4:] + "\n"

        todos = get_todos()

        todos.append(task)

        write_todos(todos)

    elif user_input.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            index = index + 1
            row = f"{index}.{item}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            number = user_input[5:]
            number = int(number) - 1

            todos = get_todos()
            new_task = input('Enter the new task: ')
            todos[number] = new_task + '\n'

            write_todos(todos)

            print('Task successfully edited.')
        except ValueError:
            print("Only specify task number to edit.")
            continue

    elif 'exit' in user_input:
        break

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])

            todos = get_todos()
            uuuu = number - 1
            todo_rem = todos[uuuu].strip('\n')
            todos.pop(number - 1)

            write_todos(todos)

            print(f"Todo {todo_rem} has been removed")
        except ValueError:
            print("Only specify task number to complete.")
        except IndexError:
            print('There is no item with that number.')
            continue

    else:
        print('Please enter the correct input')

print('Thanks')
