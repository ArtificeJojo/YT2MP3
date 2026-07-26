#Import library to download videos
import yt_dlp

#Uses Chocolatey and FFMPEG to separate audio and ensure it is in the best quality
def DownloadAudio(url):
    ydl_opts = {'format': 'bestaudio/best','postprocessors':[{'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 'preferredquality':'192'}],
                }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    #urlInput = " "
    url = "https://youtu.be/QmbIrBrCozA"
    DownloadAudio(url)

main()