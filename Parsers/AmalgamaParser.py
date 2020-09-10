from bs4 import BeautifulSoup
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.error import HTTPError
import os
import sys
import MySQLdb as MySQL
import pandas as pd
from pandas import ExcelWriter

Amalgama_URL = "http://www.amalgama-lab.com/songs/"

input_path = r"G:\Music\Test"
output_path = input_path + "\Output"
covers_path = output_path + "\\Covers\\"
excel_file_path = output_path + "\Errors.xlsx"

try:
    os.mkdir(output_path)
except FileExistsError:
    pass

try:
    os.mkdir(covers_path)
except FileExistsError:
    pass
print("Подождите. Идет обработка... \n")

tracks = os.listdir(input_path)
errors = []
done_counter, number_of_tracks, skipped_counter = 0, 0, 0

# MySQL configurations
host = "localhost"
user = "root"
user_passwd = "1234"
db_name = "Music"
ini = r""


def get_url(artist, title):
    # artists
    parts = artist.split()
    if parts[0] == "The":
        artist = " ".join(parts[1:])

    slash_pos = artist.find("/")
    if slash_pos >= 0:
        artist_arr = list(artist)
        artist_arr.pop(slash_pos)
        artist_arr.insert(slash_pos, "_")
        artist = "".join(artist_arr)

    ampersand_pos = artist.find("&")
    if ampersand_pos >= 0:
        artist = artist.replace("&", "and")

    if artist.find(",") >= 0:
        artist = artist.replace(",", "")

    has_dash = artist.find("-")
    while has_dash >= 0:
        artist = artist.replace("-", "_")
        has_dash = artist.find("-")

    apostrophe_pos = artist.find("'")
    while apostrophe_pos >= 0:
        artist_arr = list(artist)
        artist_arr.pop(apostrophe_pos)
        artist_arr.insert(apostrophe_pos, "_")
        artist = "".join(artist_arr)
        apostrophe_pos = artist.find("'")

    quotes_pos = artist.find('"')
    while quotes_pos >= 0:
        artist_arr = list(artist)
        artist_arr.pop(quotes_pos)
        artist_arr.insert(quotes_pos, "_")
        artist = "".join(artist_arr)
        quotes_pos = artist.find('"')

    full_stop_pos = artist.find(".")
    while full_stop_pos >= 0:
        artist_arr = list(artist)
        artist_arr.pop(full_stop_pos)
        artist_arr.insert(full_stop_pos, "_")
        artist = "".join(artist_arr)
        full_stop_pos = artist.find(".")

    # _________________________________________________
    # titles

    apostrophe_pos = title.find("'")
    while apostrophe_pos >= 0:
        title_arr = list(title)
        title_arr.pop(apostrophe_pos)
        title_arr.insert(apostrophe_pos, "_")
        title = "".join(title_arr)
        apostrophe_pos = title.find("'")

    full_stop_pos = title.find(".")
    while full_stop_pos >= 0:
        title_arr = list(title)
        title_arr.pop(full_stop_pos)
        title = "".join(title_arr)
        full_stop_pos = title.find(".")

    comma_pos = title.find(",")
    while comma_pos >= 0:
        title_arr = list(title)
        title_arr.pop(comma_pos)
        title = "".join(title_arr)
        comma_pos = title.find(",")

    has_dash = title.find("-")
    while has_dash >= 0:
        title = title.replace("-", "_")
        has_dash = title.find("-")

    if title.find("(") >= 0 or title.find(")") >= 0:
        title = title.strip(")")
        title = title.strip("(")
        title_arr = list(title)
        try:
            title_arr.remove("(")
        except ValueError:
            pass
        try:
            title_arr.remove(")")
        except ValueError:
            pass
        title = "".join(title_arr)

    if title.find("[") >= 0 or title.find("]") >= 0:
        title = title.strip("]")
        title = title.strip("[")
        title_arr = list(title)
        try:
            title_arr.remove("[")
        except ValueError:
            pass
        try:
            title_arr.remove("]")
        except ValueError:
            pass
        title = "".join(title_arr)

    if title.find("?") >= 0:
        title_arr = list(title)
        title_arr.remove("?")
        title = "".join(title_arr)

    ampersand_pos = title.find("&")
    if ampersand_pos >= 0:
        title = title.replace("&", "and")

    if title.find("!") >= 0:
        title_arr = list(title)
        title_arr.remove("!")
        title = "".join(title_arr)

    if title.find(":") >= 0:
        title_arr = list(title)
        title_arr.remove(":")
        title = "".join(title_arr)

    if title.find("*") >= 0:
        title_arr = list(title)
        title_arr.remove("*")
        title = "".join(title_arr)

    artist_arr = artist.split()
    artist = "_".join(artist_arr)
    title_arr = title.split()
    title = "_".join(title_arr)

    if title.find("_Live") >= 0:
        title_arr = list(title)
        title_arr = title_arr[:-5]
        title = "".join(title_arr)

    if title.find("_Album_Version") >= 0:
        title_arr = list(title)
        title_arr = title_arr[:-14]
        title = "".join(title_arr)

    if title.find("_Acoustic_Version") >= 0:
        title_arr = list(title)
        title_arr = title_arr[:-17]
        title = "".join(title_arr)

    if title.endswith("_"):
        title = title[:-1]

    has_2_underscore = title.find("__")
    while has_2_underscore >= 0:
        title = title.replace("__", "_")
        has_2_underscore = title.find("__")

    has_2_underscore = artist.find("__")
    while has_2_underscore >= 0:
        artist = artist.replace("__", "_")
        has_2_underscore = artist.find("__")

    end_artist = artist.lower()
    end_title = title.lower()

    url = Amalgama_URL + end_artist[0] + "/" + end_artist + "/" + end_title + ".html"

    return url


def parser(url, original_artist, original_title):
    # _________________________________________________________________________________
    # parser
    try:
        res = urlopen(url)
    except (HTTPError, UnicodeEncodeError) as err:
        track_name = original_artist + " - " + original_title
        errors.append(track_name)

    else:
        result = res.read()
        soup = BeautifulSoup(result, 'html.parser')

        original_soup = soup.find_all("div", class_="original")

        original = []
        for elem in original_soup:
            tag = elem
            text = tag.get_text()
            original.append(text)

        translate_soup = soup.find_all("div", class_="translate")

        translated = []
        for elem in translate_soup:
            tag = elem
            text = tag.get_text()
            if text.startswith("\n"):
                text = text.replace("\n", "")
            translated.append(text)

        original_title_soup = soup.find("h2", class_="original")
        original_title = original_title_soup.get_text()

        translated_title_soup = soup.find("h2", class_="translate")
        translated_title = translated_title_soup.get_text()

        original_lyrics = "<br>".join(original)
        translated_lyrics = "<br>".join(translated)

        return original_lyrics, translated_lyrics, original_title, translated_title


def special_symbols_deleter(album_name):
    title = album_name
    right_title = title

    if title.find(":") >= 0:
        title_arr = list(title)
        title_arr.remove(":")
        right_title = "".join(title_arr)

    if right_title.find('"') >= 0:
        title_arr = list(title)
        title_arr.remove("'")
        right_title = "".join(title_arr)

    if right_title.find('/') >= 0:
        title_arr = list(title)
        title_arr.remove("/")
        right_title = "".join(title_arr)

    if right_title.find('\\') >= 0:
        title_arr = list(title)
        title_arr.remove("\\")
        right_title = "".join(title_arr)

    if right_title.find('?') >= 0:
        title_arr = list(title)
        title_arr.remove("?")
        right_title = "".join(title_arr)

    if right_title.find('*') >= 0:
        title_arr = list(title)
        title_arr.remove("*")
        right_title = "".join(title_arr)

    if right_title.find('&') >= 0:
        right_title = right_title.replace("&", "and")

    if right_title.find('<') >= 0:
        right_title = right_title.replace("<", " ")

    if right_title.find('>') >= 0:
        right_title = right_title.replace(">", " ")

    if right_title.find('|') >= 0:
        right_title = right_title.replace("|", " ")

    return right_title


def get_cover(path_to_track, album):
    title = album
    track = MP3(path_to_track)
    img = track.tags["APIC:"].data
    title = special_symbols_deleter(title)
    path_to_cover = covers_path + title + ".jpg"
    with open(path_to_cover, 'wb') as file:
        file.write(img)

    return path_to_cover


# ____________________________________________________________
# working with the database
def fill_into_db(sql_artist, sql_title, sql_album, sql_original_lyrics, sql_translated_lyrics,
                 sql_original_title, aql_translated_title, sql_path_to_cover, sql_path_to_track):

    artist, title, album, original_lyrics, translated_lyrics,\
    original_title, translated_title, path_to_cover, path_to_track = sql_artist, sql_title, sql_album,\
                                                                     sql_original_lyrics, sql_translated_lyrics,\
                                                                     sql_original_title, aql_translated_title, \
                                                                     sql_path_to_cover, sql_path_to_track

    connection = MySQL.connect(host=host, user=user, db=db_name, charset="cp1251")
    connection.autocommit(True)
    cursor = connection.cursor()
    sql = """INSERT INTO music (Artist, Title, Album, OriginalLyrics, TranslatedLyrics, OriginalTitle, TranslatedTitle,
 PathToCover, PathToTrack) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    try:
        cursor.executemany(sql, [(artist, title, album, original_lyrics, translated_lyrics,
                                  original_title, translated_title, path_to_cover, path_to_track)])
    except UnicodeEncodeError:
        track_name = sql_artist + " - " + sql_title
        errors.append(track_name)
        artist, title, album, original_lyrics, translated_lyrics, path_to_cover, path_to_track = 0, 0, 0, 0, 0, 0, 0


for elem in tracks:
    path_to_track = input_path + "\\" + elem

    if path_to_track.endswith(".mp3"):
        number_of_tracks += 1

# iterating through the list with tracks
for elem in tracks:
    path_to_track = input_path + "\\" + elem   # creating a path to track

    if path_to_track.endswith(".mp3"):  # checking that the elem is an mp3 file
            track = EasyID3(path_to_track)
            title = track["title"][0]
            artist = track["artist"][0]
            album = track["album"][0]

            # не трогаем песни на русском
            if ord(artist[0]) in range(1040, 1072) or ord(title[0]) in range(1040, 1072):
                skipped_counter += 1
                done_counter += 1
                continue
            else:
                url = get_url(artist, title)

                path_to_cover = get_cover(path_to_track, album)

                parser(url, artist, title)
                if parser(url, artist, title) is not None:
                    original_lyrics, translated_lyrics, original_title, translated_title = parser(url, artist, title)
                    fill_into_db(artist, title, album, original_lyrics, translated_lyrics,
                                 original_title, translated_title, path_to_cover, path_to_track)

                done_counter += 1

                counter_str = str(done_counter) + "/" + str(number_of_tracks)
                print(counter_str)

errors = set(errors)
errors = list(errors)

table = pd.DataFrame({"Track_Name": errors})
with ExcelWriter(excel_file_path) as wrt:
    table.to_excel(wrt, sheet_name='Errors')

print("Добавлено записей в БД: ", number_of_tracks - skipped_counter - len(errors))
print("Отсутсвуют переводы: ", len(errors))
print("Песен на русском языке: ", skipped_counter)
print()
print("Вы можете посмотреть недобавленные переводы здесь: ", excel_file_path)
print()
print("Готово")
