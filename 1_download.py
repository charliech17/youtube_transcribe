from __future__ import unicode_literals
import yt_dlp as youtube_dl  # 使用 yt-dlp
import ssl
import certifi

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ssl_context = ssl.create_default_context(cafile=certifi.where())

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'http_ssl_context': ssl_context,
    '--ffmpeg-location': '/usr/local/bin/ffmpeg',
}

youtubeVideoId = input('請輸入youtube的videoId下載影片，例如lg48Bi9DA54') # ex: lg48Bi9DA54
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([f'https://www.youtube.com/watch?v={youtubeVideoId}'])
