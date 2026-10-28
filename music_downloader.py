# yt-dlp python
# pip install yt-dlp
import yt_dlp

video_url = "https://www.youtube.com/watch?v=L1bg_h9DI5g"

# Configuration options (mimics command-line flags)
ydl_opts = {
    "format": "bestaudio/best",
"ffmpeg_location": r"C:\ffmpeg-9.0.2-full_build\bin",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",  # You can change to '320' or '0'
        }
    ],
}
# Use a context manager to handle the download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download complete!")
