# When we use show, it has two lines gap, one due to \n and another due to default print function.
# So we remove \n using strip method in show case
while True:
    user_input = input('Enter add, show, edit, completed or exit: ')
    user_input = user_input.strip()
    user_input = user_input.lower()
    match user_input:
        case 'add':

            task = input('Add a task: ') + "\n"

            file = open('../Files/TDL.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(task)

            file = open('../Files/TDL.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            fileshow = open('../Files/TDL.txt', 'r')
            todos = fileshow.readlines()
            fileshow.close()


            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):

                item = item.strip('\n')  # JUST STRIP IN SAME LOOP

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

        case 'newfile':
            filenew = open('whatever.txt', 'w')
            file.close()

        case random_input:
            print('Please enter the correct input')
print('Thanks')
