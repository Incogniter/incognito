fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)
while True:
    dict_key = input("Enter the key:")
    if dict_key.casefold() == "quite":
        break
    if dict_key in fruit:
        answer = fruit.get(dict_key)
        print(answer)
    else:
        print("{} is not in fruit".format(dict_key))

print("_"*50)
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)
for snacks in fruit:
    print(snacks+ " is " +fruit[snacks])
    #here the output is not in a sorted manner it changes the output every time you run the program

print("_"*40)

#for printing the output in a order so that it doesnt change everytime you run the program
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)
ordered_keys =list(fruit.keys())
ordered_keys.sort()
#ordered_keys =sorted(list(fruit.keys()))
for keys in ordered_keys:
    print(keys +" is "+fruit[keys])
#for keys in fruit:
    #rint(keys + " is " + fruit[keys])

print("_"*40)