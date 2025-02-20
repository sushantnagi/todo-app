password = input('Enter a password: ')


def strength(password):
    listi = []

    if len(password) >= 8:
        listi.append(True)

    else:
        listi.append(False)

    c2 = False
    for i in password:
        if i.isupper() == True:
            c2 = True
    listi.append(c2)

    c3 = False
    for i in password:
        if i.isdigit() == True:
            c3 = True
    listi.append(c3)

    print(listi)

    if all(listi):
        print('Strong password')
    else:
        print('Weak Password')

strength(password)