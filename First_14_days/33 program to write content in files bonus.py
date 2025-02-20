contents = ['This is a sentence.',
            'This is another sentence.',
            'This is yet '
            'another sentence.']
files = ['file1.txt', 'file2.txt', 'file3.rtf']

# Whenever we say multiple, we use for loop to iterate over.

for content, file, in zip(contents, files):
    filevar = open(f'Files/{file}', 'w')
    filevar.write(content)
    filevar.close()

# If this python file is in a subdirectory, use '../' to go one directory up.
# For
# Same directory, Linux, Mac : use /
# Outside directory in Windows \

a = ('I am '
     'a string '
     'on my own.')
print(a)

