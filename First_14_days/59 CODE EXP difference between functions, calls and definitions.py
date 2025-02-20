def greet():
    message = 'hello'
    new_message = message.capitalize()
    print('hey hey')
    # return new_message (Function will return a special object 'none')
    return None

greeting = greet()

print(greeting)

# whenever a function is called using function(), its return
# value is stored in the variable assigned