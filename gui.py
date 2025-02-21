import functions
import FreeSimpleGUI as sg

label = sg.Text('Enter a To-Do')
InputBox = sg.InputText(tooltip='Enter a To-Do:', key='todo')
addbutt = sg.Button('Add')

window = sg.Window('To-Do List App',
                   layout=[[label, InputBox], [addbutt]],
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

        case sg.WIN_CLOSED:
            break



window.close()

