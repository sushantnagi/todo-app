todos = []

while True:
    user_action = input("add, show or exit: ")
    a = user_action
    if a == 'add':
        todo = input('Enter a task: ')
        todo = todo.capitalize()
        todos.append(todo)
    if a == 'show':
        print(todos)
    if a == 'exit':
        print('Shutting down')
    else:
        break



