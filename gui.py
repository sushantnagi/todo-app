import functions
import FreeSimpleGUI as sg

label = sg.Text('Enter a To-Do')
InputBox = sg.InputText(tooltip='Enter a To-Do:')
addbutt = sg.Button('Add')

window = sg.Window('To-Do List App', layout=[[label, InputBox], [addbutt]])
window.read()
window.close()

