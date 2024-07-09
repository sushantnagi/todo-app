#String can be multiplied with int
a = input('Enter a number:')
b = int(a)
b = b*9
c = a * 20
d = c*5
print(a,b,c,d, 'a')
##################################
mylist = [1 ,2,3 , '4']
e = mylist.index('4')
print(e)
mylist[3] = '5'
# is same as
mylist.__setitem__(3, '5')
# same for __getitem__

