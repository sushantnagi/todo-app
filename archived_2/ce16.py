import FreeSimpleGUI as s

label1 = s.Text('Enter feet')
input1 = s.Input()

label2 = s.Text('Enter Inches')
input2 = s.Input()

button1 = s.Button('Convert')

window = s.Window('Convertor', [[label1, input1],
                                [label2, input2],
                                [button1]])

window.read()
window.close()
