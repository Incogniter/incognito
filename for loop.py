#for loop
#for i in range(start,End):
for i in range(1,4):
    print(i)

print()
#string formating
for i in range(1,11):
    print('No {0:2} square is {1:3} and cube is {2:4}'.format(i,i**2,i**3))
    print('No {0:<2} square is {1:^3} and cube is {2:>4}'.format(i,i**2,i**3))
    
print('-------------')

Name = "abino robilin"
for character in Name:
    print(character)

print("___________")

#stepping through for loop
lists = '456,1,25.25;45:698:548'
special_character= " "
for char in lists:
   if not char.isnumeric():
       special_character =special_character +char
print(special_character)

print('--------------------------')

for i in range(1,13):
    for j in range(1,13):
        print("{0} times {1} is {2}".format(j,i,i*j))
    print("--------------------------------")   

print('---------------')   
#continue statement
lists = ["1",'2','3','4','5','7','9']
for number in lists:
    if number != "5":
        print('figure '+ number) 

print("----------")
lists = ['1','2','3','4','5','6','7','8','9','10']
for numbers in lists:
    if numbers == '6':
        continue
    print("figure "+ numbers)       


    print('------------------------')

#break
#it stops the loop when the condition is statisfied
lists = ["meat","juice","drug","water","rice","coffie","shit","pie"]
item_to_find = "shit" 
found_at = None
for index in range(len(lists)):
    if lists[index] == item_to_find:
        found_at = index
        break
print("the item is found at {}".format(found_at))

print("------------------------------")
#Augmented assignment
#it is an more efficiant method to represent a data
#for example
x = 5
x +=1
print(x)
x *=2
print(x)  #etc
greeting = "good "
greeting +="Morning "
print(greeting)
greeting *=2
print(greeting)

print("---------------------------------------")
#else in loop code
numbers = (1,2,3,4,5,6,7,8,9)
for numbers in numbers:
    if numbers % 5 == 0:
        print("this is shit")
        break
else:
    print("its fine")
print("--------------------------------------------")