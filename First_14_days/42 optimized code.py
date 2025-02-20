while True:
    user_input = input('Enter add, show, edit, completed or exit: ')
    user_input = user_input.strip()
    user_input = user_input.lower()
    match user_input:
        case 'add':

            task = input('Add a task: ') + "\n"

            # file = open('../Files/TDL.txt', 'r')
            # todos = file.readlines()
            # file.close()
            with open('../Files/TDL.txt', 'r') as file:
                todos = file.readlines()

            todos.append(task)

            #SIMILARLY HERE
            with open('../Files/TDL.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('../Files/TDL.txt', 'r') as fileshow:
                todos = fileshow.readlines()



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
