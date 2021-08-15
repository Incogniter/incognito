#nested list
menu = [["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
        ]

for meal in menu:
    if "spam" not in meal:
        print(meal)
    else:
        print("{} have {} spam".format(meal,meal.count("spam")))

#deleting "spam" in nested list
menu = [["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
        ]
for meals in menu:
    for index in range(len(meals)- 1,-1,-1):
        if meals[index] == "spam":
            del meals[index]
    print(meals)
print("-"*30)

#alternater method
menu = [["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
        ]
for meals in menu:
    for item in meals:
        if item != "spam":
                print(item)
    print()
print("-"*30)
#deleting "spam" in nested list
#with .join() function
menu = [["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
        ]
for meals in menu:
    for index in range(len(meals)- 1,-1,-1):
        if meals[index] == "spam":
            del meals[index]
    print(",".join(meals))