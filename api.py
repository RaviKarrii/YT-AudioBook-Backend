from __future__ import unicode_literals
from flask import request, jsonify
import flask
import youtube_dl
from os import walk


ydl_opts = {
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def process(Url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filep = ydl.download([Url])
    print(filep)
    return "Succesfull"

@app.route('/download/', methods=['GET'])
def home():
    if 'url' in request.args:
        url = str(request.args['url'])
    else:
        return "Error: No id field provided. Please specify an id."
    return process(url)

@app.route('/list/', methods=['GET'])
def list():
    f = []
    for (dirpath, dirnames, filenames) in walk("downloads"):
        f.extend(filenames)
    return ", ".join(f)

app.run()