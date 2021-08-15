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

print("-"*20)
flower =[
    "rose",
    "lily",
    "jasmine",
    "lotus",
    "sun flower",
    "tiger lily"
]

#for flowers in flower:
#   print(flowers)

seperators = ","
flowers = seperators.join(flower)
print(flowers)
print(",".join(flower))

print("-"*50)

panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

print()
#Replacing the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)