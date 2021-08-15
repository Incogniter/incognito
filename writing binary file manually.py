with open("binary", 'bw') as bin_file:
    # for i in range(17):
    #     bin_file.write(bytes([i]))
    bin_file.write(bytes(range(17)))
with open("binary", 'br') as binFile:
    for b in binFile:
        print(b)
print("_"*50)
a = 65534
b = 65535
c = 65536
x = 2998302
with open("binary2", 'bw') as biNFile:
    biNFile.write(a.to_bytes(2, 'big'))
    biNFile.write(b.to_bytes(2, 'big'))
    biNFile.write(c.to_bytes(4, 'big'))
    biNFile.write(x.to_bytes(4, 'big'))
    biNFile.write(x.to_bytes(4, 'little'))
with open("binary2", 'br') as biNFile:
    a = int.from_bytes(biNFile.read(2), 'big')
    print(a)
    b = int.from_bytes(biNFile.read(2), 'big')
    print(b)
    c = int.from_bytes(biNFile.read(4), 'big')
    print(c)
    x = int.from_bytes(biNFile.read(4), 'big')
    print(x)
    x = int.from_bytes(biNFile.read(4), 'big')
    print(x)
