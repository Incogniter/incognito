def bio_data(name,age):#name , age are formal aguments or argumengs
#def bio_data(name,age=18) here age =18 is default values executes only if actual arguments have no value
    print(name,age)
bio_data("Abino",5) #"Abino",5 are actual arguments
#bio_data("Abino",age=5) #here age = 5 is the keyword

print("_"*40)

def multiply(x,y):
    product = x*y
    return product
answer = multiply(3,4)
print(answer)

one = multiply(2,50)
print(one)

print()
for val in range(1,5):
    firstOne = 5
    tot = multiply(firstOne,val)
    print(tot)