def custom_1(hello):
    hellocap = hello.capitalize()
    return hellocap


user_entry =  input('Enter your greeting: ')
greeting = custom_1(user_entry)
print(greeting)

# print(hello)  does not work
