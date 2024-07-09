todos = []
while True:
    user_input = input('Enter add, show or exit: ')
    user_input = user_input.strip()
    match user_input:
        case 'add':
            task = input('Add a task: ')
            todos.append(task)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
print('Thanks')

