def get_todos(filepath):  # filepath is parameter
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
        # This function is a procedure so no need to have a return statement, as it does not produce anything.



while True:
    user_input = input('Enter add, show, edit, complete or exit: ')
    user_input = user_input.strip()
    user_input = user_input.lower()

    if user_input.startswith('add'):
        task = user_input[4:] + "\n"

        todos = get_todos(filepath='../Files/TDL.txt')  # Files/TDL.txt is argument

        todos.append(task)

        write_todos('../Files/TDL.txt', todos)  # No variable assignment here, as it will return none.

    elif user_input.startswith('show'):
        todos = get_todos('../Files/TDL.txt')

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

            todos = get_todos('../Files/TDL.txt')
            new_task = input('Enter the new task: ')
            todos[number] = new_task + '\n'

            write_todos('../Files/TDL.txt', todos)

            print('Task successfully edited.')
        except ValueError:
            print("Only specify task number to edit.")
            continue

    elif 'exit' in user_input:
        break

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])

            todos = get_todos('../Files/TDL.txt')
            uuuu = number - 1
            todo_rem = todos[uuuu].strip('\n')
            todos.pop(number - 1)

            write_todos('../Files/TDL.txt', todos)

            print(f"Todo {todo_rem} has been removed")
        except ValueError:
            print("Only specify task number to complete.")
        except IndexError:
            print('There is no item with that number.')
            continue

    else:
        print('Please enter the correct input')

print('Thanks')
