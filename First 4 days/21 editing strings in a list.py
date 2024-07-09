filenames = ['1.Textfile.txt', '2.game.exe', '3.browser.exe']
#problem = replace first . with -

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)

# 1 means only first dot will be replaces
