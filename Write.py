# # creates a txt file using python
# cities = ["Nagercoil", "marthandam", "Thuckalay", "Monday market", ]
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)
# use "file" function to create as a txt file

cities = []
with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))
        # .strip(\n) os used to remove the space between the lines and renoves \n from the list
print(cities)
for city in cities:
    print(city)

print("_"*50)

# To understand .strip() , it removes the values only from the start and end of the string
print("abino".strip('a'))
print("abino".strip('i'))
print("abino".strip('o'))

print("_"*50)
imelda = "More Mayhem", "Imelda MAy", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda3.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)
# eveluvate = eval

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
