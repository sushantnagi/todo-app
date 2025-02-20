password = input('Enter your password: ')
check = {} # dictionary ['key' : value]
if len(password) >= 8:
    check['length'] = True
else:
    check['length'] = False

# subcheck = []
# for i in password:
#     numbercheck = i.isdigit()
#     subcheck.append(numbercheck)
# result1 = any(subcheck)
# check.append(result1)
# or

digit = False
for i in password:
    if i.isdigit():
        digit = True
check['number'] = digit


upper = False
for i in password:
    if i.isupper() == True:
        upper = True
check['uppercase'] = upper


print(check.values())

if all(check.values()):
    print('Strong Password')
else:
    print('Weak Password')