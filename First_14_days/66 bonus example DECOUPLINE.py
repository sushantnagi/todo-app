"""
A function should only perform one thing.
More than one makes the program complicated.
So we break the function into two.
"""

feet_inches = input('Enter Feet and Inches: ')


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


f, i = parse(feet_inches)

print(f, i)

result = convert(f, i)
print(result)

if result < 1:
    print('Kid is too small.')
else:
    print('Move ahead.')