import yt_dlp

def DownloadAudio(url):
    ydl_opts = {'format': 'bestaudio/best','postprocessors':[{'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 'preferredquality':'192'}],
                }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    url = "https://youtu.be/QmbIrBrCozA"
    DownloadAudio(url)

main()