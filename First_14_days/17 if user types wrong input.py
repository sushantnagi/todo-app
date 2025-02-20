todos = []
while True:
    user_input = input('Enter add, show or exit: ')
    user_input = user_input.strip()
    match user_input:
        case 'add':
            task = input('Add a task: ')
            todos.append(task)
        case 'show' | 'display':  # | stands for or
            for item in todos:
                item = item.title()  #  title method
                print(item)
        case 'exit':
            break
        case random_input:  # _ is used conventionally i.e case _
            print('Please enter the correct input')
print('Thanks')
