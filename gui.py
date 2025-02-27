import functions
import FreeSimpleGUI as sg
import time

sg.theme('LightBlue3')

clock = sg.Text('', key='clock')
label = sg.Text('Enter a To-Do')
InputBox = sg.InputText(tooltip='Enter a To-Do:', key='todo')
addbutt = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
editbutt = sg.Button('Edit')
completebutt = sg.Button('Complete')
exitbutt = sg.Button('Exit')

window = sg.Window('To-Do List App',
                   layout=[[clock],
                           [label, InputBox],
                           [addbutt, editbutt, completebutt, exitbutt],
                           [list_box]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%Y-%m-%d %H:%M:%S"))
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
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup('Please select an item first.', font='Algerian')

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")

            except IndexError:
                sg.popup('Please select an item first.', font='Algerian',)

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

        case None:
            break
window.close()
