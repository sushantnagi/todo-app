# in python, generally we do not create lists or strings (print fn)
# they are created by reading from textfiles or databases
#
# for example

file = open('Files/TDL.txt', 'r')
var = file.readlines()
print(var)
print(type(var[0]))  # a list has strings

# If file is located within a folder, but same directory as python project

file = open('folder/TDL.txt', 'r')

# If file is located somewhere outside
file =  open(r'C:\Users\SUSHANT NAGI\Downloads\file.extension', 'r' )
file =  open('C:\Users\SUSHANT NAGI\Downloads\file.extension', 'r' )
# r means row string, as \ is a special character in python

# for mac/linus

file = open('/Users/username/Downloads/file.extension')

