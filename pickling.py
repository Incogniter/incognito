import pickle

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))
with open("imelda.pickle", 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file)

with open("imelda.pickle", 'rb') as imelda_pickled:
    imelda3 = pickle.load(imelda_pickled)
print(imelda3)

album, artist, year, title_track = imelda3
print(album)
print(artist)
print(year)
for tracks in title_track:
    track_number, track = tracks
    print(track_number, track)

print("_"*50)

imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))
even = list(range(2, 10, 2))
odd = list(range(1, 10, 2))
with open("imelda.pickle", 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol= pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol= pickle.DEFAULT_PROTOCOL)
    pickle.dump(348520, pickle_file, protocol= pickle.HIGHEST_PROTOCOL)

with open("imelda.pickle", 'rb') as imelda_pickled:
    imelda3 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)
print(imelda3)
print(even_list)
print(odd_list)
print(x)
album, artist, year, title_track = imelda3
print(album)
print(artist)
print(year)
for tracks in title_track:
    track_number, track = tracks
    print(track_number, track)

print("_"*50)

for i in odd_list:
    print(i)
print("_"*50)

for i in even_list:
    print(i)

print("_"*50)

print(x)
