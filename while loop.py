#while loop
i=0
while i<=10:
    print("the value of i is {}".format(i))
    i=i+1

print('------------------------------------')
available_exits = ["east","west","north","south"]
chosen_exit = " "
while chosen_exit.casefold() not in available_exits:
     chosen_exit = input('CHOOSE YOUR DIRECTION :')
     if(chosen_exit.casefold() == "quite"):
         print("Game over")
         break
print("You are out of it Bitch")

print('______________________________________________---------------------')

# challange using while loop
import random

answer = random.randint(1, 10)
print(answer)
print("Guess a number between 1 to 10")
Guess = 0
while (Guess != answer):
    Guess = int(input("Make your Guess:"))
    if (Guess == 0):
        print("Game over")
        break
    elif (Guess < answer):
        print('Guess higher you bloody bitch')
    else:
        print("Guess lowe u idiot")
        if(Guess == answer):
            print("you got it")
print('___________________________________________________________________________________')


#high low game
low =1
high =1000
print("think a number bwt {} to {}".format(low,high))
input("press ENTER to start")
guesses=1
while True:
    guess=low +(high -low)//2
    high_low=input("my guess is {} should i guess higher ,lower or correct "
                   "enter h ,l or c".format(guess).casefold())
    if high_low == "h":
        # Guess higher,the lower end of the range becomes one greater than guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower, the higher end of the range becomes one lesser than guess0
        high = guess - 1
    elif high_low == "c":
        print(" i got it in {} guesses! ".format(guesses))
        break
    else:
        print("please enter h,l or c")
    guesses = guesses + 1
print("---------------------------------")
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
#high low game
#using while else statement
low = 1
high = 1000
print('Think of a number between {} and {}'.format(low,high))
input('press enter to continue')
guesses = 1
while low != high:
    guess = low+(high-low)//2
    high_low= input("My guess is {},should higher or lower please enter h,l or c for the correct one :".format(guess)).casefold()
    if high_low == "h":
        #Guess higher,the lower end of the range becomes one greater than guess
        low = guess + 1
    elif high_low == "l":
        #Guess lower, the higher end of the range becomes one lesser than guess
        high = guess - 1
    elif high_low == "c":
        print("i got it right in {} guess".format(guesses)) #error in .format(guesses) rectify it
        break
    else:
        print("please press H,L or C")
    #guess = guesses +1
    guesses +=1
else:
    print("you thought of the number{}".format(low))
    print("i got i right in {} guesses!!!".format(guesses)) #error in .format(guesses) rectify it

print("----------------------------------------------------------------------------------------------------------")
#while else statement
available_exits = ["east","west","north","south"]
chosen_exit = " "
while chosen_exit.casefold() not in available_exits:
     chosen_exit = input('CHOOSE YOUR DIRECTION :')
     if(chosen_exit.casefold() == "quite"):
         print("Game over")
         break
else:
    print("Well done You are out of it Bitch")

print("---------------------------------------------------------")

# challange
numbers = ("2")
escape = " "
while escape not in numbers:
    escape = (input("Enter the number first 10 number to get out of the loop:"))
    if escape.casefold() == "QUITE":
        print("Game over")
        break
else:
    print("Just escaped haha!!")

print("--------------------------------------------")
# challange
# actual code
print("Please choose your option from the list below:")
print("1:\tLearn Python")
print("2:\tLearn Java")
print("3:\tGo swimming")
print("4:\tHave dinner")
print("5:\tGo to bed")
print("0:\tExit")

while True:
    choice = input()

    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
print("--------------------------------------------------------")
# actual code is in the begining
# after changing the condition
choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("please enter the number you choose below in the list")
        print("1:\tgo swiming")
        print("2:\tgo sleep")
        print("3:\thave dinner")
        print("4:\tdo exercise")
        print("5:\tLearn python")
        print("0:\tExit")
    choice = input("Enter your choice:")

print("==================================================================================================")
