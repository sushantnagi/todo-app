# for loops run as long as there are items in a list,
# whereas while loops run as long as the condition specified is true

#  ex1
meals = ['Pasta',
         'Pizza',
         'Burger']
for meal in meals:
    print(meal.title())

print('Thanks')

# ex 2 : for loops can also iterate over strings
Letters = 'qwertyuiop'
for alphabet in Letters:
    print(alphabet.title())

