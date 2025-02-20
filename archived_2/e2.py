import csv

with open('archived/weather.csv', 'r') as file:
    data = list(csv.reader(file))

print(data)

city = input('Enter city: ')

for row in data:
    if row[0] == city:
        print(list[1])