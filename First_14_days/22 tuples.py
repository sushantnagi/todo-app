# immutable lists ()
filenames = '1.Textfile.txt', '2.game.exe', '3.browser.exe'
# or use ()
filenames = ('1.Textfile.txt', '2.game.exe', '3.browser.exe')

filenames[1] = 'new'  #shows error
# TypeError: 'tuple' object does not support item assignment


