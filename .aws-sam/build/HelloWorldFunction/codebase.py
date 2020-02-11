from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'outtmpl': 'tmp/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
def process(Url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filep = ydl.download([Url])
    return filep