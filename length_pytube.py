from pytubefix import YouTube

url = "https://www.youtube.com/watch?v=aQ84e2ftyIg"
yt = YouTube(url)

duration_seconds = yt.length
print(f"Song: {yt.title}")
print(f"Duration: {duration_seconds//60}:{duration_seconds%60:02d}")