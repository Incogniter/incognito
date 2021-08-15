#zip() function
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
products =[]
#zip() function is used in matrix(list and tuples)  arithmetic operation
for num1,num2 in zip(even,odd):
    products.append(num1 * num2)
sum = sum(products)
print(products)
print(sum)