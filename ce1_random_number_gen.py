import random
a = int(input('Enter the lower value: '))
b = int(input('Enter the upper value: '))

output = random.randint(a, b)
rand = random.randrange(a, b+1)

print(output)
print(rand)
