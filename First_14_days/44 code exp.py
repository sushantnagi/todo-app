with open('../Files/doc35.txt', 'r') as file:
    print(file.read())

# open command doesnt is on 'r' mode by default
with open('../Files/doc35.txt') as file:
    print(file.read())

# as soon as the block of code (indentation) ends, the "WITH" command closes the file

with open('../Files/doc35.txt', 'r') as file:
    print(file.read())
# file.read()
# hence this would lead to error

# But we can assign a variable to contents of file to use it again, or use open close
with open('../Files/doc35.txt', 'r') as file:
    contents = file.read()
print(contents)

# The file.read is exhaustive. It Moves cursor
with open('../Files/doc35.txt', 'r') as file:
    file.read()
    print(file.read()) #this would give empty output