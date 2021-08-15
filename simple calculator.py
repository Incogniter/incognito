def add(x,y):
    return x + y

def subrat(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y
def get_remainder(x,y):
    return x % y

print("Enter the operation you want to do")
print("1.Addition")
print("2.subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Remainder")
while True:
    operation =(input("Enter the chose( '0',1','2','3','4','5') :"))
    if operation in ('1', '2', '3', '4','5','0'):
        if operation == '0':
            break
        num1 = float(input("Enter the number :"))
        num2 = float(input("Enter the another value :"))
        if operation == '1':
            print("num1 + num2", "=", add(num1, num2))
        elif operation =='2':
            print("num1 -  num2", "=", subrat(num1, num2))
        elif operation == '3':
            print("num1 * num2", "=", multiply(num1, num2))
        elif operation == '4':
            print("num1 / num2", "=", divide(num1, num2))
        elif operation == '5':
            print( "num1 % num2 =",get_remainder(num1,num2))
    else:
        print("invalid entry")