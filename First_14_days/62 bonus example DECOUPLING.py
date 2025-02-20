feet_inches = input('Enter Feet and Inches: ')

def convert(feet_inches):
    parts = feet_inches.split(" ")   # splits at " " space
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters  # always return a useable variable

result = convert(feet_inches)
print(result)

if result < 1:
    print('Kid is too small.')
else:
    print('Move ahead.')