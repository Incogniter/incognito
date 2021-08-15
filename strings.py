#Indexing (possitive indexing 0-infinity nd negative indexing (-1)-(-infinity) )
#         01234567890123
Parrot = 'Norwegian Blue'
print(Parrot)
print(Parrot[3])
print(Parrot[4])
print(Parrot[9])
print(Parrot[3])
print(Parrot[6])
print(Parrot[8])
print()
#negative indexing
#-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# N   o    r  w   e   g  i  a  n     B  l  u  e
print(Parrot[-11])
print(Parrot[-10])
print(Parrot[-5])
print(Parrot[-11])
print(Parrot[-8])
print(Parrot[-6])
print()
#slicing(positive nd negative) parrot[(START):(STOP)] is also acceptable IT DOESNOT INCLDE STOP VALUE
print(Parrot[0:6]) #norweg
print(Parrot[:6])
print(Parrot[10:13]) #which is wrong
print(Parrot[10:14]) #which is correct
print(Parrot[10:])
print(Parrot[:6])
print(Parrot[6:])
print(Parrot[:6] + Parrot[6:])
print(Parrot[:])
#negative
print(Parrot[-14:-4])
print(Parrot[-4:])
print(Parrot[-14:-4] + Parrot[-4:])
#using a step in slice (Parrot[start:stop:step])
print(Parrot[0:6:2]) #nre
print()
numbers = "1,2,3,4,5,6,7,8,9" #for understanding purpose
print(numbers[0:17:2]) #123456789
print()
number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
print()
#slicing backward
letters = "abcdefghijklmnopqrstuvwxyz"
backward = (letters[25::-1])
print(backward)
print()

backward = (letters[16:13:-1])
print(backward) #qpo

print()
#F string => fast string
age = 60
print(type(age))
print(f'my age is {age} years')
A = 5
B = 10
print('the value of A is',A, 'the value of B is',B)

