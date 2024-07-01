todos = []

while True:
    user_input = input('Enter add, show or exit: ')
    match user_input:
        case 'add':
            todo = input('Enter a task: ')
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
print('Thanks for using the ToDoList.')
