'''# 1.0.4 v
.4 > updated yt-dlp to fix security errors
.3 > fixed/bypassed security and botting issue
.3 > made a prompt pop up when an error has occured to help debugging
'''
import yt_dlp,sys
from pathlib import Path
path = str(Path(__file__).resolve().parent)

def download_audio(url, output_path='downloads', ffmpeg_location=None):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'extractor_args': {'youtube': {'player_client': ['android']}},
        'noprogress': True,
    }
    if ffmpeg_location:
            ydl_opts['ffmpeg_location'] = ffmpeg_location

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download successful!")
    except yt_dlp.utils.DownloadError as e:
        input(f"Download failed: {e}")
    except Exception as e:
        input(f"Error downloading audio: {e}")
    pass

if __name__ == '__main__':
    print("YoutubeAudioExtractor v1.0.4")
    youtube_url = input("Enter the YouTube URL: ")
    download_audio(youtube_url,f"{path}/output", ffmpeg_location=f'{path}/ffmpeg/ffmpeg-2024-09-12-git-504c1ffcd8-full_build/bin')