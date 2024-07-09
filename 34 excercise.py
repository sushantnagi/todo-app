user_input = input('Enter the new member: ') + '\n'

file = open(r'C:\Users\SUSHANT NAGI\Downloads\members1.txt', 'r')  # file opens as read only
store = file.readlines()
file.close()

store.append(user_input)

file = open(r'C:\Users\SUSHANT NAGI\Downloads\members1.txt', 'w')
ap_pend = file.writelines(store)
file.close()

file = open(r'C:\Users\SUSHANT NAGI\Downloads\members1.txt', 'r')  # file opens as read only
store2 = file.readlines()
print(list(store2))
