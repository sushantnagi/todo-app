while True:  #user_input.startswith()
    user_input = input('Enter add, show, edit, complete or exit: ')
    user_input = user_input.strip()
    user_input = user_input.lower()

    if user_input.startswith('add'):
        task = user_input[4:] + "\n"
        with open('../TDL.txt', 'r') as file:
            todos = file.readlines()

        todos.append(task)

        with open('../TDL.txt', 'w') as file:
            file.writelines(todos)

    elif user_input.startswith('show'):
        with open('../TDL.txt', 'r') as fileshow:
            todos = fileshow.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            index = index + 1
            row = f"{index}.{item}"
            print(row)

    elif user_input.startswith('edit'):
        number = user_input[5:]
        number = int(number) - 1

        with open('../TDL.txt', 'r') as file:
            todos = file.readlines()
        new_task = input('Enter the new task: ')
        todos[number] = new_task + '\n'
        with open('../TDL.txt', 'w') as file:
            file.writelines(todos)

        print('Task successfully edited.')

    elif 'exit' in user_input:
        break

    elif user_input.startswith('complete'):
        number = int(user_input[9:])

        with open('../TDL.txt', 'r') as file:
            todos = file.readlines()
        uuuu = number - 1
        todo_rem = todos[uuuu].strip('\n')
        todos.pop(number - 1)
        with open('../TDL.txt', 'w') as file:
            file.writelines(todos)
        print(f"Todo {todo_rem} has been removed")


    else:
        print('Please enter the correct input')

print('Thanks')
