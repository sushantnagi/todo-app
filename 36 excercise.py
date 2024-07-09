filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    fileobject = open(f'ex36f/{filename}', 'r')
    a = fileobject.read()
    print(a)
    