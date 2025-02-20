while True:
    user_input = input('Enter add, show, edit, completed or exit: ')
    user_input = user_input.strip()
    user_input = user_input.lower()
    match user_input:
        case 'add':

            task = input('Add a task: ') + "\n"
            with open('../Files/TDL.txt', 'r') as file:
                todos = file.readlines()

            todos.append(task)

            with open('../Files/TDL.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('../Files/TDL.txt', 'r') as fileshow:
                todos = fileshow.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                index = index + 1
                row = f"{index}.{item}"
                print(row)

        case 'edit':
            number = input('Enter task number to edit: ')
            number = int(number) - 1

            with open('../Files/TDL.txt', 'r') as file:
                todos = file.readlines()
            new_task = input('Enter the new task: ')
            todos[number] = new_task + '\n'
            with open('../Files/TDL.txt', 'w') as file:
                file.writelines(todos)


            print('Task successfully edited.')

        case 'exit':
            break

        case 'completed':
            number = int(input('Enter task number to mark completed: '))

            with open('../Files/TDL.txt', 'r') as file:
                todos = file.readlines()
            uuuu = number - 1
            todo_rem = todos[uuuu].strip('\n')
            todos.pop(number - 1)
            with open('../Files/TDL.txt', 'w') as file:
                file.writelines(todos)
            print (f"Todo {todo_rem} has been removed")


        case random_input:
            print('Please enter the correct input')

print('Thanks')
