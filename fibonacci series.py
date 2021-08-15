def fibonacci(n):
    if 0 <=n <=1:
        return n


    X,Y=0,1

    result = None
    for i in range(n-1):
        result =X+Y
        X = Y
        Y = result

    return result
F = int(input("Enter the number of times the value should execute:"))
for i in range(F):
    print(fibonacci(i))
