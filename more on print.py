name = "Abino"
age = "20"
#sep= is used only when there is two variables to be print instead use end=
print(name,age,sep= ",")
print(name,end=",")
print()

print("-"*30)
#for example
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
                print(item,end=", ")
    print()
print("-"*30)

