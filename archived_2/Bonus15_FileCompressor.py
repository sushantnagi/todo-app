import FreeSimpleGUI as sg

label1 = sg.Text('Select File to Compress: ')
input1 = sg.Input()
button1 = sg.FileBrowse('Add')

label2 = sg.Text('Select Destination Folder: ')
input2 = sg.Input()
button2 = sg.FolderBrowse('Choose')

compress_button = sg.Button('Compress')

window = sg.Window('File Compressor',
                   layout=[[label1, input1, button1],
                           [label2, input2, button2],
                           [compress_button]])
window.read()
window.close()