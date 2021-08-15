#difference between sorted and sort
#sorted
#the sorted in immutable(stores in new variable)and sort is mutable (stored in the same variable)
statement = "The quick brown fox jumps over the lazy fox"
letters = sorted(statement)
print(letters)

Number =[1,215,15,8,26,58,7,10,3,6,8]
sorted_number =sorted(Number)
print(sorted_number)

#sort
numberList = [1,5,9,7,3,4,6,45,88,74,11,99,99999,10000000,1235498,125489,125,45,65,85,58,52,25,51,15]
numberList.sort()
print(numberList)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",key=str.casefold)
#where ever using casefold in sorted function,use key=str.casefold
print(missing_letter)
print()
names = ["Abino,"
         "priscilla",
         "blesso",
         "shaju",
         "john",
         "sharmi",
         "Sheryl"
         ]
names.sort(key=str.casefold)
print(names)

print("-------------------------------------------------------------")


