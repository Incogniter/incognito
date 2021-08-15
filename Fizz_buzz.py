def fizz_buzz(n):
    if n % 3 and n % 5 == 0:
        return ("Fizz Buzz")
    elif n % 3 == 0:
        return ("Fizz")
    elif n % 5 == 0:
        return ("Buzz")
    else:
        return n
input("Please press Enter to start")
n = int(input("Enter the range:"))
for i in range(1,n+1):
    print(fizz_buzz(i))