
try:
    width = float(input('Enter rectangle width: '))
    length = float(input('Enter rectangle length: '))

    if width == length:
        exit('This is a square.')
        # print('this is a sqaure)
        # exit

    area = width * length
    print(area)
except ValueError:
    print('Please enter a number')


