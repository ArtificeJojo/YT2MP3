#Import library to download videos
import yt_dlp
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#Uses Chocolatey and FFMPEG to separate audio and ensure it is in the best quality
def DownloadAudio(url):
    ydl_opts = {'format': 'bestaudio/best','postprocessors':[{'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 'preferredquality':'192'}],
                }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.download([url])

@app.route('/api/data', methods = ['GET', 'POST'])
def main():
    url = ""
    mp3 = None
    if request.method == "POST":
        url = request.form.get("url")
        mp3 = DownloadAudio(url)
        return jsonify({"success": True})

    if request.method == "GET":
        return mp3
        #Return mp3 file

    return render_template("MainPage.html")

main()