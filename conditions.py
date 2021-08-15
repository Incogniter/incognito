#conditon or comparison (AND,OR)
#AND has higher predcdence than OR
age = int(input('Enter the age:'))
if (age > 16 and age < 65):
    print("have a good day")
else:
    print('Enjoy your day')    


    print()

age = int(input('Enter the age:'))
if(age < 16 or age > 65):
    print('have a good day')
else:
    print("go do ur work")


    print()

#challange
Name = input('Enter the name:')
Age = int(input('Enter the age:'))
if(Age >= 16 and Age <= 31 ):
    print('Welcome to the holiday {0}'.format(Name))
else:
    print("oops only 18-31 are allowed sorry")


    print()

#boolean expressions true or false
#AND has higher predcdence than OR 
#AND operator stop checking as soon as it finds a false
#OR operator stops checking as soon as it finds a true
day = "sunday"
temperature = 30
raining = False
if((day == "sunday" and temperature < 27) or raining):
    print('go swiming')
else:
    print('learn python')
#in boolean expression all zero are considered to be false 
#constant and zero of any numeric types and empty is considered to be false
if 0:
    print('True')
else:
    print('false')

    print()

#name is an empty string
name = input('please enter your name:')
if name:
    print('hello {}'.format(name))
else:
    print('Motherfucker just enter the name')
    name =input('Enter your name')
    print('hello {}'.format(name))



    print()

today = "friday"
print('day' in today)
print('fri' in today)
#here in operator evaluates the first thing exists in the second

print("----------")


#checking IN and NOT IN 
#IN
Mylove = "sheryl priscilla"
letter = input('Enter the letter you wanna find:')
if (letter in Mylove):
    print('{0} is in {1}'.format(letter,Mylove))
else:
    print("SORRY I dont need any letter that wasnt included in My love")


    print()

#NOT IN 
activity = input('whats your plan today?')
if ('movie' not in activity.casefold()):
    print('I want to watch movie')
else:
    print("I want to learn python")