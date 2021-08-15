N=int(input('Enter the number of subjects:'))

tot = 0
for i in range(0,N):
    i=i+1
    subject = int(input('Enter the mark obtained in subject {0}:'.format(i)))
    tot = tot + subject
    avg = tot // N
print("The total marks is",tot, "Average is",avg)   
    
print()



answer = 6
print('guess the number between 1 to 10')
guess = int(input())
if(guess > answer):
    print('guess lower')
    guess = int(input())
    if(guess == answer):
        print('you are right')
    else:
        if(guess < answer):
            print('guess higher')
            guess = int(input())
            if(guess == answer):
                print('you are right')
else:
    print('got it ')