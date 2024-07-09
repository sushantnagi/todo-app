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
            print(index, item) #variables remain after for loop is closed, they take the last value
            #use case
            print("Number of items in list is " +str(index))
            # the actual way to show
            print('Number of todos is ' +str(len(todos)))


