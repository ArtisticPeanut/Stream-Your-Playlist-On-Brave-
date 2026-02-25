# Stream-Your-Playlist-On-Brave-
# myTune - Automated YouTube Playlist Player

A Python-based automation tool that plays songs from a playlist on YouTube and manages browser instances seamlessly.

## Features

- 🎵 **Automated Playlist Playback** - Read songs from a text file and play them sequentially on YouTube
- ⏱️ **Smart Duration Handling** - Automatically detects song duration and waits for playback to complete
- 🔄 **Tab Management** - Closes Brave browser tabs after each song and opens a new one for the next track
- 📝 **Metadata Logging** - Stores song information (link, title, duration) in JSON format
- 🎯 **Lightweight** - Uses system-level browser automation for minimal overhead

## How It Works

1. Reads song titles from `songlist.txt`
2. Searches and plays each song on YouTube using `pywhatkit`
3. Gets accurate song duration using `pytubefix`
4. Waits for the song to finish playing
5. Closes the browser tab and moves to the next song
6. Logs all song data to `playlist_infor.json`

## Requirements

- Python 3.7+
- Brave Browser

## Installation

```bash
pip install pywhatkit pytubefix
```
## Recommended
go to Brave settings and Enable On Startup - Open the New Tab page
## Usage

1. Create a `songlist.txt` file with songs in format:
   ```
   1. Song Name 1
   2. Song Name 2
   3. Song Name 3
   ```

2. Run the player:
   ```bash
   python read_songs.py
   ```

3. Check `playlist_infor.json` for playback history

## Files

- `read_songs.py` - Main playlist player script
- `songlist.txt` - Input file with song names
- `playlist_infor.json` - Output log with song metadata
- `get_song_details.py` - YouTube search utility
- `length_pytube.py` - Song duration retriever

## Notes

- Make sure Brave browser is installed
- The script uses `pkill brave` to close browser instances
- Default wait time is song duration + 5 seconds buffer
# myTune - Automated YouTube Playlist Player

A Python-based automation tool that plays songs from a playlist on YouTube and manages browser instances seamlessly.

## Features

- 🎵 **Automated Playlist Playback** - Read songs from a text file and play them sequentially on YouTube
- ⏱️ **Smart Duration Handling** - Automatically detects song duration and waits for playback to complete
- 🔄 **Tab Management** - Closes Brave browser tabs after each song and opens a new one for the next track
- 📝 **Metadata Logging** - Stores song information (link, title, duration) in JSON format
- 🎯 **Lightweight** - Uses system-level browser automation for minimal overhead

## How It Works

1. Reads song titles from `songlist.txt`
2. Searches and plays each song on YouTube using `pywhatkit`
3. Gets accurate song duration using `pytubefix`
4. Waits for the song to finish playing
5. Closes the browser tab and moves to the next song
6. Logs all song data to `playlist_infor.json`

## Requirements

- Python 3.7+
- Brave Browser

## Installation

```bash
pip install pywhatkit pytubefix
```

## Usage

1. Create a `songlist.txt` file with songs in format:
   ```
   1. Song Name 1
   2. Song Name 2
   3. Song Name 3
   ```

2. Run the player:
   ```bash
   python read_songs.py
   ```

3. Check `playlist_infor.json` for playback history

## Files

- `read_songs.py` - Main playlist player script
- `songlist.txt` - Input file with song names
- `playlist_infor.json` - Output log with song metadata
- `get_song_details.py` - YouTube search utility
- `length_pytube.py` - Song duration retriever

## Notes

- Make sure Brave browser is installed
- The script uses `pkill brave` to close browser instances
- Default wait time is song duration + 5 seconds buffer
