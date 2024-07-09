# last program terminates at 2 attempts
password = input('Enter password: ')
while password != '1234':
    print('Password is incorrect.')
    password = input('Enter password: ')
print('PASSWORD IS CORRECT!')

