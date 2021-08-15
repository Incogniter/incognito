#creating a list and printing it
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

print(computer_parts[0:3])
print(computer_parts[-1])

print("--------------------------------------------------")

#immutable
result = firstclass
nxtResult =result
print(id(result))
print(id(nxtResult))
#difference is down below

result =firstclass
nxtResult = fail
print(id(result))
print(id(nxtResult))

print('------------------------------------')
#mutable
lists = ["egg",
         "meat",
         "rice",
         "biscutes"]
print(lists)
another_lists = lists
print(id(lists))
print(id(another_lists))
print()
lists +=["water"]
print(lists)
print(id(lists))

a=b=c=d=lists
b.append("drugs")
print(a)

print("_"*30)

#appending a list
#updated
#nore efficient way of presenting a code
#contains removing from a list
available_choises = ["nose",
                     "converse",
                     "neck",
                     "lips",
                     "meow_meow",
                     "thighs",
                     "hips"
                     ]
valid_choices = []
for i in range(1,len( available_choises) + 1 ):
    valid_choices.append(str(i))
your_choise = " "
Wishlist = []
while your_choise != "0":
    if your_choise in valid_choices :
        index = int(your_choise)
        chosen_choise = available_choises[index]
        if chosen_choise in Wishlist:
            Wishlist.remove(chosen_choise)
            print("your choise {} is removed".format(your_choise))
        else:
            Wishlist.append(chosen_choise)
            print("your choise {} is added".format(your_choise))
            print("Your wishlist now cointains {}".format(Wishlist))
    elif your_choise =="12345678" :
            print("Better you try her Sheryl priscilla")
            Wishlist.append("nose,converse,neck,lips,meow_meow,thighs,legs,hips")
            break
    else:
        print("pick your choise:")
        for Index,your_choisec in enumerate(available_choises):
            #enumerate is a builtin function (example:)
            #for index,character in enumerate("Abino"):
            #print(index,character)
            print("{0}: {1}".format(Index + 1,your_choisec) )
    your_choise = input("Make your own choise:")
print(Wishlist)

print("_"*30)
