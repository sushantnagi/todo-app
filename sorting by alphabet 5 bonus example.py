list = ['sen', 'ben', 'john']
list.sort()
print(list)
for i, item in enumerate(list):
    row = f"{i+1}.{item.capitalize()}"
    print(row)
#lists are mutable. the methods will mutate the lists

list2 = [1,2,3]
list2.sort(reverse=True) #for descending order
print(list2)
