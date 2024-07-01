todos = []
while True:
    user_input = input('Enter add, show, edit or exit: ')
    user_input = user_input.strip()
    match user_input:
        case 'add':
            task = input('Add a task: ')
            todos.append(task)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = input('Enter task number to edit: ')
            number = int(number) - 1  #input always is a string
            new_task = input('Enter the new task: ')
            todos[number] = new_task
            print('Task successfully edited.')
        case 'exit':
            break
        case random_input:
            print('Please enter the correct input')
print('Thanks')
