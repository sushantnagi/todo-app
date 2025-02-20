import glob

myfiles = glob.glob('Files//*.txt')  # Used for filtering files

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())