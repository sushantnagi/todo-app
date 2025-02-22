import functions
import FreeSimpleGUI as sg

label = sg.Text('Enter a To-Do')
InputBox = sg.InputText(tooltip='Enter a To-Do:', key='todo')
addbutt = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
editbutt = sg.Button('Edit')

window = sg.Window('To-Do List App',
                   layout=[[label, InputBox], [addbutt, editbutt], [list_box]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)


        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])





        case sg.WIN_CLOSED:
            break



window.close()

