# file = open ("/Users/Abino Robilin/PycharmProjects/Input_Output/2.1 sample.txt", 'r')
# use / or \\  for mentioning a path
# file = open ("\\Users\\Abino Robilin\\PycharmProjects\\Input_Output\\2.1 sample.txt", 'r')
file = open("2.1 sample.txt", 'r')
for line in file:
     #print(line) #prints line with spaces
    if "jabberwock" in line.lower():
         #which prints the  word cointaining the line
         #end= '' removes the space between the lines
        print(line, end='')
file.close()

print("_"*50)
print("alternative method")
#alternate method
with open("2.1 sample.txt",'r') as file:
    for line in file:
        if "jabberwock" in line.lower():
            print(line, end='')
print("_"*50)
print("readline method")
#In the alt method we dont have to close the file because it is done by the with operation
#TO print the WHOLE file without spaces
with open("2.1 sample.txt", 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()
print("_"*50)
print("alternate method")
#alternate method
print("readlines method")
with open("2.1 sample.txt", 'r') as file:
    lines = file.readlines() #this readlines() creates a list of the file
print(lines)

for line in lines: #print the items in the list
    #end= '' removes the spaces between the lines
    print(line, end='')
print("_"*50)

with open("2.1 sample.txt", 'r') as file:
    lines = file.readlines()
for line in lines[::-1]:  #prints in reverse order
    print(line, end='')

print("_"*50)
print("read method")
with open("2.1 sample.txt",'r') as file:
    lines = file.read() #read() reades a single line
for line in lines[::-1]:
    print(line, end='')