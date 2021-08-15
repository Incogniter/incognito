#nested list

odd = [1,3,5,7,9]
even =[2,4,6,8]

number = [odd , even]
print(number)

for number_list in number:
    print(number_list)
    for value in number_list:
        print(value)