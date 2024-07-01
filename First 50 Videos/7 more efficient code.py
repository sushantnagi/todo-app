prompt = 'Enter a task :'
TDL = []
while True:
    task = input(prompt)
    task = task.title()
    TDL.append(task)
    print(TDL)

# in this case, the prompt variable is declared once outside the program

# if the variable is declared inside the while loop
# while True
# prompt = 'Enter a task: '
# it will be executed each time on loop increasing memory use
