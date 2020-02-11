from __future__ import unicode_literals
from flask import request, jsonify, send_from_directory, current_app
import flask
import youtube_dl
from os import walk
import os


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

@app.route('/upload/', methods=['GET'])
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

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, 'downloads')
    print(uploads)
    return send_from_directory(directory=uploads, filename=filename)

app.run()