#Import library to download videos
import yt_dlp
from flask import Flask, render_template, request
app = Flask(__name__)

#Uses Chocolatey and FFMPEG to separate audio and ensure it is in the best quality
def DownloadAudio(url):
    ydl_opts = {'format': 'bestaudio/best','postprocessors':[{'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 'preferredquality':'192'}],
                }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/', methods = ['GET', 'POST'])
def main():
    url = ""
    if request.method == "POST":
        url = request.form.get("url")
    DownloadAudio(url)

main()