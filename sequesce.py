even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))
print("---------------------------------------------------------------")
even.extend(odd)
print(even)

anotherEven = even
print(anotherEven)

even.sort()
print(even)

even.reverse()
print(even)
print(anotherEven)

even.sort(reverse= True)
print(even)

print('--------------------------------------------------------------------------')
print("mississippi".count("s"))
print("mississippi".count("is"))
print("mississippi".count("iss"))
print("mississippi".count("issi"))

print("-"*50)

#appending a list
your_choise = " "
lists = []
while your_choise != "0":
    if your_choise in "123456780":
        print("your choise {} is added".format(your_choise))
        if your_choise == "1":
            lists.append("nose")
        elif your_choise == "2":
            lists.append("converse")
        elif your_choise == "3":
            lists.append("neck")
        elif your_choise == "4":
            lists.append("lips")
        elif your_choise =="5":
            lists.append("meow_moew")
        elif your_choise =="6":
            lists.append("thighs")
        elif your_choise =="7":
            lists.append("legs")
        elif your_choise =="8":
            lists.append("hips")
        elif your_choise =="12345678" :
            print("Better you try her Sheryl priscilla")
            lists.append("nose,converse,neck,lips,meow_meow,thighs,legs,hips")
            break
    else:
        print("pick your choise:")
        print("1:nose")
        print("2:converse")
        print("3:neck")
        print("4:lips")
        print("5:meow_meow")
        print("6:thighs")
        print("7:legs")
        print("8:hips")
    your_choise = input("Make your own choise:")
print(lists)


print("_"*30)


#appending a list
#updated
available_choises = ["nose",
                     "converse",
                     "neck",
                     "lips",
                     "meow_meow",
                     "thighs",
                     "legs",
                     "hips"
                     ]
your_choise = " "
lists = []
while your_choise != "0":
    if your_choise in "123456780":
        print("your choise {} is added".format(your_choise))
        if your_choise == "1":
            lists.append("nose")
        elif your_choise == "2":
            lists.append("converse")
        elif your_choise == "3":
            lists.append("neck")
        elif your_choise == "4":
            lists.append("lips")
        elif your_choise =="5":
            lists.append("meow_moew")
        elif your_choise =="6":
            lists.append("thighs")
        elif your_choise =="7":
            lists.append("legs")
        elif your_choise =="8":
            lists.append("hips")
        elif your_choise =="12345678" :
            print("Better you try her Sheryl priscilla")
            lists.append("nose,converse,neck,lips,meow_meow,thighs,legs,hips")
            break
    else:
        print("pick your choise:")
        for index,your_choisec in enumerate(available_choises):
            #enumerate is a builtin function (example:)
            #for index,character in enumerate("Abino"):
            #print(index,character)
            print("{0}: {1}".format(index + 1,your_choisec) )
    your_choise = input("Make your own choise:")
print(lists)



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

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = odd + even
print(numbers)

sorted_numbers =sorted(numbers)
print(sorted_numbers)
print(numbers)

digits_sorted = sorted("123657894")
print(digits_sorted)
digits =list("126543798")
print(digits)

#more_numbers = list(numbers)
#more_numbers = numbers[:]
#more_numbers = numbers.copy()
more_numbers = numbers
print(more_numbers)

print(more_numbers is numbers)
print(more_numbers == numbers)




