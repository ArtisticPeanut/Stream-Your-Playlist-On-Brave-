import pywhatkit
import json
import re
from pytubefix import YouTube
import time
import os 


with open("songlist.txt","r") as songList:
    songs = songList.readlines()
print(songs)

playlist = []
for song in songs:
    # print(song[:2])
    try:
        if song[:2].isnumeric():
            song = song[3:]
            playlist.append(song.strip())
            
    except IndexError:
        pass

print(playlist)
song_links = []
def play_song(song):
    song_link = pywhatkit.playonyt(song)
    # print(song_link)
    yt = YouTube(song_link)
    duration_seconds = yt.length
    song_links.append(song_link)
    print(f"Paying {song} for {duration_seconds//60}:{duration_seconds%60:02d}")
    return song,song_link, duration_seconds
#     json.dump(song_links, json_file, indent=4)

# play_song(playlist[1])
for song in playlist:
    # os.system('brave-browser')
    # open brave on new terminal
    song, song_link, duration_seconds = play_song(song)
    time.sleep(duration_seconds+5)
    # close the browser after the song finishes
    os.system('pkill brave')
    with open("playlist_infor.json","a") as json_file:
        json.dump((song_link, song, duration_seconds), json_file, indent=4)

