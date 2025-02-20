from First_14_days.converter66 import convert
from First_14_days.parser66 import parse

feet_inches = input('Enter Feet and Inches: ')

f, i = parse(feet_inches)

print(f, i)

result = convert(f, i)
print(result)

if result < 1:
    print('Kid is too small.')
else:
    print('Move ahead.')