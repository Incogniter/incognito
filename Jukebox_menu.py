from nested_data import albums
SONGLIST_INDEX =3
SONGTITLE_INDEX=1
while True:
    print("please choose the album you would like to play")
    for index,(title,artist,year,song) in enumerate(albums):
        print("{}:{}".format(index+1,title))
#    for index,value in enumerate(albums):
#        title,artist,year,song =value
#        print(index+1,title,artist,year,song)
    choise = int(input("Enter your choise:"))
    if 1 <= choise <= len(albums):
        songList = albums[choise-1][SONGLIST_INDEX]
    else:
        break
    print()
    print("please enter your choise")
    for index,(track_number,song) in enumerate(songList):
        print("{}:{}".format(index+1,song))

    song_choice = int(input("Choose a song you wanna play:"))
    if 1 <= song_choice <=len(songList):
        title=songList[song_choice -1][SONGTITLE_INDEX]
        print("Playing song {}.........".format(title))
    print("="*40)
