locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = {"QUIT":  "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST":  "E",
              "WEST":  "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}
# print(locations[0].split())
# print(locations[3].split(","))
# print(''.join(locations[0].split()))
default_location = 1
while True:
    available_location = ",".join(exits[default_location].keys())
#    for direction in exits[default_location].keys():
#        available_location += direction + ","
    print(locations[default_location])

    if default_location == 0:
        break
    else:
        all_exits = exits[default_location].copy()
        all_exits.update(namedExits[default_location])
    direction = input(" Available exits are " + available_location + ":").upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
    if direction in all_exits:
        default_location = all_exits[direction]
    else:
        print("You cant go in that direction")
