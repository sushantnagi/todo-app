todos = []
while True:
    user_input = input('Enter add, show, edit, completed or exit: ')
    user_input = user_input.strip()
    match user_input:
        case 'add':
            task = input('Add a task: ')
            todos.append(task)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                item = item.title()
                index = index + 1
                row = f"{index}.{item}"
                print(row)
        case 'edit':
            number = input('Enter task number to edit: ')
            number = int(number) - 1
            new_task = input('Enter the new task: ')
            todos[number] = new_task
            print('Task successfully edited.')
        case 'exit':
            break

        case 'completed':
            number = int(input('Enter task number to mark completed: '))
            todos.pop(number - 1)

        case random_input:
            print('Please enter the correct input')

print('Thanks')
