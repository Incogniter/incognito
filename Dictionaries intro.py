fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
print(fruit.keys())
print(fruit.values())
print(fruit["lemon"])
fruit["pear"] = "an odd shaped apple" #adding an item in dictionary
print(fruit)
fruit.update({"jack fruit":"yellow in color"})#addiing an item in dictionary
print(fruit)
fruit["lime"] = "great with tequila" #Editing an item in dictionary
print(fruit)
del fruit["lemon"] #deleting an item in dictionary
print(fruit)
pazham=fruit.copy()# copy() function "makes a copy of fruit and assign to pazham".so fruit  is fixed in line 20
print(pazham)       #https://youtu.be/MQ7VXRAK59M use this youtube link
del pazham["apple"]
print(fruit)
# del fruit (which deletes the dictionary)
fruit.clear() #clearing the entries that are present in the dictionary
print(fruit)

