filenames = ['doc35.txt', 'report35.txt', 'presentation35.txt']

for filename in filenames:
    file_object = open(f'files/{filename}', 'w')
    file_object.write('Hello')
    file_object.close()

