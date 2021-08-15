#deleting items from a list
#forward and back ward
data = [4,98,99,75, 5,6, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187,1231, 188, 191, 350,351, 1000,7000,1001,1002,360]
#data = [4,98,99,75, 5,6, 104, 105, 110, 120, 130, 130, 150,160, 170, 183, 185, 187, 188, 191,]
#data = [104, 105, 110, 120, 130, 130, 150,160, 170, 183, 185, 187, 188, 191, 350,351, 1000,7000,1001,1002,360]
#data = [ 104, 105, 110, 120, 130, 130, 150,160, 170, 183, 185, 187, 188, 191,]
#data =[]

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break

print(start)  # for debugging
del data[start:]
print(data)

print("-"*50)

#deleting itens from a list backwards
data = [25,50,100,90,483,180,251,155]
minValue = 100
maxValue = 200
for index in range(len(data) -1,-1,-1):
    if data[index] < minValue or data[index] > maxValue:
        print(index,data)
        del data[index]
print(data)
print("-"*30)
#deleting items from a list
#more efficient way
#deleting backwards
data = [4,98,99,75, 5,6, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187,1231, 188, 191, 350,351, 1000,7000,1001,1002,360]
min_valid = 100
max_valid = 200
for index in range(len(data)-1,-1,-1):
    if data[index] < min_valid or data[index] > max_valid:
        #print(index,data) #for details
        del data[index]
print(data)
print("-"*30)
#deleting itens from a list backwards
#more efficient way
data = [25,50,100,90,483,180,251,155]
minValue = 100
maxValue = 200
#for index in range(len(data) -1,-1,-1):
 #   if data[index] < minValue or data[index] > maxValue:
  #      print(index,data)
   #     del data[index]
top_index = len(data) -1
for index,value in enumerate(reversed(data)):
   if value < minValue or value > maxValue:
       print(top_index - index,value)
       del data[top_index-index]

print(data)





