import random
def get_integer(promt):
    while True:
        temp =(input(promt))
        if temp.isnumeric():
            return int(temp)
        else:
            print("{} is not valid ".format(temp))
answer = random.randint(1, 10)
print(answer)
print("Guess a number between 1 to 10")
Guess = 0
while (Guess != answer):
    Guess = get_integer("Make your Guess:")
    if (Guess == 0):
        print("Game over")
        break
    else:
        if (Guess < answer):
            print('Guess higher you bloody bitch')
            Guess = get_integer("Make your Guess:")
            if (Guess == answer):
                print("Bitch you are out of the loop")
            else:
                print("Stay here you mother fucker")
        elif (Guess > answer):
            print('lower you idiot')
            Guess = get_integer("Make your Guess:")
            if (Guess != answer):
                print("nah!! sorry")
            else:
                print("You got it ")
