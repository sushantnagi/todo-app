# for i,j in enumerate('hello'):
#     print(i,j)
#     row = f"{i}.{j}"
#     print(row)

a = enumerate('YouTube')
print(a)

print(list(a)) #to visualize the <> object
print('The output is a list of several tuples')

for j, item in list([(0, 'Y'), (1, 'o'), (2, 'u'), (3, 'T'), (4, 'u'), (5, 'b'), (6, 'e')]):
    print(j, item)

# for k, ktem in list(a):
#     print(k, ktem)