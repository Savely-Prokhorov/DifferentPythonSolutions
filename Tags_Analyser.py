from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
import matplotlib.pyplot as plt
import os
import pandas as pd
from pandas import ExcelWriter
import xlsxwriter

# creating empty lists which will store all info about tracks
artists_array, titles_array, albums_array, lengths_array = [], [], [], []

# creating a list with all tracks in directory
input_path = r"G:\Music\Music (24.07.17)"
output_path = input_path + r"\AnalysisInfo\Results.xlsx"
tracks = os.listdir(input_path)
try:
    os.mkdir(input_path + r"\AnalysisInfo")
except FileExistsError:
    pass
print("Подождите. Идет обработка... \n")

# iterating through the list with tracks
for elem in tracks:
    path_to_track = input_path + "\\" + elem   # creating a path to track
    if path_to_track.endswith(".mp3"):  # checking that the elem is an mp3 file
        try:
            track = EasyID3(path_to_track)
        except ID3NoHeaderError:
            print(path_to_track, ": Невозможно преобразовать")
        else:
            track_for_length = MP3(path_to_track)   # creating an mp3 model of track to get a length of mp3 file
            try:
                title = track["title"][0]
                artist = track["artist"][0]
            except KeyError:
                print(path_to_track, ": нет названия или исполнителя")
            else:
                try:
                    album = track["album"][0]
                except KeyError:
                    print(path_to_track, ": нет названия альбома")
                    album = "No album name was found"
                else:
                    # filling track info into lists for further analysis
                    length = track_for_length.info.length
                    artists_array.append(artist)
                    titles_array.append(title)
                    albums_array.append(album)
                    lengths_array.append(length)
print("__________________________________________________________________")

# creating and filling track info into main table
main_table = pd.DataFrame({"!Artist": artists_array,
                           "!Title": titles_array,
                           "Album": albums_array,
                           "Length": lengths_array})

# getting total tracks in folder duration
all_length = 0
for elem in main_table["Length"]:
    all_length += elem

number_of_all_songs = len(main_table.index.get_values())  # calculating number of songs in folder
average_duration = all_length / number_of_all_songs  # calculating average duration of song in folder
# output of received previously info
print("Средняя продолжительность песен в медиатеке: ", round(average_duration, 2), "сек. / ",
      int(average_duration // 60), "мин", round(average_duration - (average_duration // 60) * 60, 2), "сек.")

# creating table grouped by artist, getting quantity of tracks by artist
# and total artist's tracks duration
grouped_by_artist_main_table = main_table.groupby("!Artist")
# initializing dictionaries which will store quantity of tracks by artist
# and total artist's tracks duration
length_dict, number_tracks_by_artist = {}, {}
count = 0  # initializing a variable which will store quantity of tracks by artist
# iterating through new created table
for artist, group in grouped_by_artist_main_table:
    length_column = group.groupby("Length")  # creating a table with length of artists's track
    total_artists_length = 0  # initializing a variable which will store total artist's tracks duration
    for length, len_group in length_column:
        total_artists_length += length
        count += 1
    length_dict.update({artist: total_artists_length})  # filling dictionaries with
    number_tracks_by_artist.update({artist: count})     # newly received info
    count = 0

# initializing list with total artist's track duration,
# artists' names and number of songs by artist
len_arr, artist_arr, number_of_songs = [], [], []
# these for blocks are responsible for filing just now created list
for key in length_dict.keys():
    artist_arr.append(key)
for value in length_dict.values():
    len_arr.append(value)
for value in number_tracks_by_artist.values():
    number_of_songs.append(value)

# creating and filling table which stores total duration of songs by artist
length_table = pd.DataFrame({"Artist": artist_arr,
                             "Total Length": len_arr,
                             "Quantity": number_of_songs})

# grouping previous table by total duration and quantity of songs by artist
length_table = length_table.groupby(["Artist", "Total Length", "Quantity"])
average_dur_arr = []  # initializing a list which will store average duration of artists' songs
# iterating through grouped table and getting and
# appending to list average duration of artists' songs
for name, group in length_table:
    average_duration = name[1] / name[2]
    average_dur_arr.append(average_duration)

# creating and filling table which stores
# quantity of songs by artist and average duration of song
length_table = pd.DataFrame({"Artist": artist_arr,
                            "Length": len_arr,
                             "Quantity": number_of_songs,
                             "Average Duration": average_dur_arr})

# grouping main table by album and its artist
grouped_by_album_main_table = main_table.groupby(["Album", "!Artist"])
number_tracks_in_album_dict = {}  # initializing a dict which will store quantity of tracks in album
tracks_in_album_count = 0
# iterating through previously created table
for album, group in grouped_by_album_main_table:
    tracks_in_album_count = len(group.index.get_values())  # assigning a counter the number of tracks in album
    number_tracks_in_album_dict.update({album: tracks_in_album_count})  # filling a dict with previously received info

album_arr, number_tracks_in_album_arr = [], []  # creating lists which 'll contain album name & number of tracks in it
# appending info to previously created lists
for key in number_tracks_in_album_dict.keys():
    album_arr.append(key)
for value in number_tracks_in_album_dict.values():
    number_tracks_in_album_arr.append(value)

# creating and filling a table containing album name and quantity of tracks in it
albums_table = pd.DataFrame({"Album": album_arr,
                             "Quantity": number_tracks_in_album_arr})


# sorting length table by average duration (descending)
sorted_by_aver_len_length_table = length_table.sort_values(by="Average Duration", ascending=False)
# and by quantity of tracks by artist (descending)
sorted_by_tracks_quantity_length_table = length_table.sort_values(by="Quantity", ascending=False)
# sorting album table by quantity of tracks in album
sorted_by_quantity_albums_table = albums_table.sort_values(by="Quantity", ascending=False)


# calculating quantity of artists in folder
artists_quantity = len(sorted_by_tracks_quantity_length_table.axes[0])
# calculating quantity of album in folder
albums_quantity = len(sorted_by_quantity_albums_table.axes[0])
# outputting that info
print("Всего исполнителей: ", artists_quantity)
print("Всего альбомов: ", albums_quantity)
print("______________________________")
print()


# selection by artists who has more than 10 songs
selected_tracks_by_artists_table = \
    sorted_by_tracks_quantity_length_table[sorted_by_tracks_quantity_length_table["Quantity"] > 10]


# selection by albums that have more than 6 songs
selected_albums_table = sorted_by_quantity_albums_table[sorted_by_quantity_albums_table["Quantity"] > 6]

# selection by artists who has less than 5 songs
selected_less_tracks_by_artists_table = \
    sorted_by_tracks_quantity_length_table[sorted_by_tracks_quantity_length_table["Quantity"] < 5]

with ExcelWriter(output_path) as wrt:
    main_table.to_excel(wrt, sheet_name='Main')
    sorted_by_aver_len_length_table.loc[:, ['Artist', 'Average Duration']].to_excel(wrt, sheet_name='SortedByAverLen')
    sorted_by_tracks_quantity_length_table.loc[:, ['Artist', 'Quantity']].to_excel(wrt, 'SortedBySongsNumberByArtist>6')
    sorted_by_quantity_albums_table.to_excel(wrt, sheet_name='SortedBySongsNumberInAlbum<5')
    selected_tracks_by_artists_table.loc[:, ['Artist', 'Quantity']].to_excel(wrt, sheet_name='ArtistSongs>10')
    selected_albums_table.to_excel(wrt, sheet_name='SongsInAlbum>6')
    selected_less_tracks_by_artists_table.loc[:, ['Artist', 'Quantity']].to_excel(wrt, sheet_name='ArtistSongs<5')

print("Вы можете просмотреть и проанализировать результаты анализа здесь: " + output_path)
print()
input("Нажмите Enter, чтобы выйти\n")
