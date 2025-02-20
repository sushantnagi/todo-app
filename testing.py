def water_state(temp):
    if temp <= 0:
        return "Solid"
    elif temp >= 100:
        return "Gas"
    else:
        return 'Liquid'

print(water_state(9))