import shelve
print(dir())
for val in dir():
    print(val)
print(dir(shelve))
for m in dir(shelve):
    print(m)

print(dir(shelve.Shelf))
for s in dir(shelve.Shelf):
    if s[0] != "_":
        print(s)