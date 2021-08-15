fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
# for f in fruit:
#     print(f  + " - " + fruit[f])
# for val in fruit.values():
#     print(val)
#
# print('-' * 40)
#
# for key in fruit:
#     print(fruit[key])
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
                                    #line 27 - 31 you have added a key nd decprition in the dict Fruit
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)     #printing tuple

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))