answer = 5
print("Guess the number between 1 to 10")
guess = int(input())

if (guess < answer):
    print('guess higher')
    guess = int(input())
    if(guess == answer):
        print("you guessed it")
    else:
        print("oops you missed it")
elif(guess > answer):
    print('guess lower')
    guess = int(input())
    if(guess == answer):
        print("you got it")
    else:
        print("nah!! sorry ")
else:
    print('you got it')



print( )

answer = 6
print("guess a number between 1 to 10")
Guess = int(input())
if(Guess != answer):
    if(Guess > answer):
        print('guess lower')
    else:
        print('guess higher')
    Guess = int(input())
    if(Guess == answer):
        print('well done!! you got it')
    else:
        print("YOU MISSED IT")
else:
    print("YOU GOT IT FOR THE FIRST TIME")   


#challange 
answer = 6
print("guess a number between 1 to 10")
Guess = int(input())
if(Guess == answer):
    print("you got it right")
else:
    if(Guess > answer):
        print("guess lower")
    else:
        print("guess higher")
    Guess = int(input())
    if(Guess == answer):
        print("oh yeah!!!! you got it")
    else:
        print("you are wrong")

print("--------------------------------------------------------")


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
    else:
        if (Guess < answer):
            print('Guess higher you bloody bitch')
            Guess = int(input("Make your Guess:"))
            if (Guess == answer):
                print("Bitch you are out of the loop")
            else:
                print("Stay here you mother fucker")
        elif (Guess > answer):
            print('lower you idiot')
            Guess = int(input("Make your Guess:"))
            if (Guess == answer):
                print("you got it")
            else:
                print("nah!! sorry ")

print('___________________________________________________________________________________')

# high low game
low = 1
high = 1000
print('Think of a number between {} and {}'.format(low, high))
input('press enter to continue')
guesses = 1
while True:
    guesses = low + (high - low) // 2
    high_low = input(
        "My guess is {},should higher or lower please enter h,l or c for the correct one :".format(guesses)).casefold()
    if high_low == "h":
        # Guess higher,the lower end of the range becomes one greater than guess
        low = guesses + 1
    elif high_low == "l":
        # Guess lower, the higher end of the range becomes one lesser than guess
        high = guesses - 1
    elif high_low == "c":
        print("i got it right in {} guess".format(guesses))  # error in .format(guesses) rectify it
        break
    else:
        print("please press H,L or C")
    guess = guesses + 1

print("---------------------------------")