import os
import random
import requests
from pytube import YouTube
from moviepy.editor import VideoFileClip
from bs4 import BeautifulSoup
from urllib.request import urlopen
from iestyn import *


def yt2mp4(link):
    output_path = "./temp"
    title = random.randint(100000, 999999)

    yt = YouTube(link)
    try:
        tester(yt.length)
    except Exception as e:
        return print("Invalid link!", e)

    streams = yt.streams.filter(file_extension='mp4', progressive=True)
    video_stream = max(streams, key=lambda x: int(x.resolution[:-1]))

    print(f"Downloading {yt.title}")
    try:
        video_stream.download(output_path, f'{title}.mp4')
        file_path = os.path.join(output_path, f'{title}.mp4')
    except Exception as e:
        return print("Error while downloading video!", e)

    return file_path, yt.title


def yt2mp3(link):
    output_path = "./temp"
    title = random.randint(100000, 999999)
    title2 = random.randint(100000, 999999)

    yt = YouTube(link)
    try:
        tester(yt.length)
    except Exception as e:
        return print("Invalid link!", e)

    video_stream = yt.streams.filter(res="720p",
                                     file_extension="mp4",
                                     progressive=True,
                                     adaptive=False).first()
    print(f"Downloading {yt.title}")
    try:
        video_stream.download(output_path, f'{title}.mp4')
        file_path = os.path.join(output_path, f'{title}.mp4')
        audio_path = os.path.join(output_path, f'{title2}.mp3')
    except Exception as e:
        return print("Error while downloading video!", e)

    video_clip = VideoFileClip(file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()

    while os.path.exists(file_path):
        os.remove(file_path)

    return audio_path, yt.title


def tt2mp4(link):
    data = {
        'id': link,
        'locale': 'en',
        'tt': 'YVoyUUhi',
    }
    filename = f'temp/{random.randint(1000, 9999)}.mp4'
    response = requests.post('https://ssstik.io/abc', params=params, headers=headers, data=data)
    downloadsoup = BeautifulSoup(response.text, "html.parser")
    video_name = downloadsoup.find('p', class_='maintext').text
    print(f"Downloading {video_name}")
    dlink = downloadsoup.a["href"]
    mp4file = urlopen(dlink)
    with open(filename, 'wb') as file:
        file.write(mp4file.read())

    return filename, video_name


def tt2mp3(link):
    data = {
        'id': link,
        'locale': 'en',
        'tt': 'YVoyUUhi',
    }
    filename = f'temp/{random.randint(1000, 9999)}.mp4'
    audio_path = f'temp/{random.randint(1000, 9999)}.mp3'
    response = requests.post('https://ssstik.io/abc', params=params, headers=headers, data=data)
    downloadsoup = BeautifulSoup(response.text, "html.parser")
    video_name = downloadsoup.find('p', class_='maintext').text
    print(f"Downloading {video_name}")
    dlink = downloadsoup.a["href"]
    mp4file = urlopen(dlink)
    with open(filename, 'wb') as file:
        while True:
            data = mp4file.read()
            if data:
                file.write(data)
            else:
                break

    video_clip = VideoFileClip(filename)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()

    while os.path.exists(filename):
        os.remove(filename)

    return audio_path, video_name


def sanitize(filename):
    # Define a set of invalid characters for Windows file names
    invalid_chars = '<>:"/\\|?*'

    # Replace invalid characters with underscores
    sanitized_filename = ''.join('_' if c in invalid_chars else c for c in filename)

    return sanitized_filename


def tester(thing):
    if thing:
        return thing