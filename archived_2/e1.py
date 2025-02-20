import glob

myfiles = glob.glob('Files/*txt')
print(myfiles)

for filepath in myfiles:
    with open(filepath, 'w') as file:
        file.writelines('glob')
        file.close()