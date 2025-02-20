date = input(f"Enter today's date: ")
mood = input('Rate your mood today on a scale of 1-10: ') + 2 * '\n'
journal = input('Enter your journal:\n ')

with open(f'Journal App/{date}.txt', 'w') as file:
    file.write(mood + journal)
print('Journal Successfully created')
