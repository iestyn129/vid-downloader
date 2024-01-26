import os
from conversions import yt2mp4, yt2mp3, tt2mp4, tt2mp3, sanitize

if __name__ == "__main__":
    if not os.path.exists("./temp"):
        os.mkdir("./temp")
    platform = input("TikTok or YouTube: ")
    file_type = input("MP4 or MP3: ")
    link = input("Link: ")
    if platform == "youtube" or platform == "Youtube" or platform == "YouTube":
        if file_type == "MP4" or file_type == "Mp4" or file_type == "mp4":
            vid_path, vid_title = yt2mp4(link)
            if os.path.exists(f'{sanitize(vid_title)}.mp4'):
                os.remove(f'{sanitize(vid_title)}.mp4')
            os.rename(vid_path, f'{sanitize(vid_title)}.mp4')
            if os.path.exists(vid_path):
                os.remove(vid_path)
            print(f'Saved {vid_title}.mp4')
        elif file_type == "MP3" or file_type == "Mp3" or file_type == "mp3":
            vid_path, vid_title = yt2mp3(link)
            if os.path.exists(f'{sanitize(vid_title)}.mp3'):
                os.remove(f'{sanitize(vid_title)}.mp3')
            os.rename(vid_path, f'{sanitize(vid_title)}.mp3')
            if os.path.exists(vid_path):
                os.remove(vid_path)
            print(f'Saved {vid_title}.mp3')
    elif platform == "tiktok" or platform == "Tiktok" or platform == "TikTok":
        if file_type == "MP4" or file_type == "Mp4" or file_type == "mp4":
            vid_path, vid_title = tt2mp4(link)
            if os.path.exists(f'{sanitize(vid_title)}.mp4'):
                os.remove(f'{sanitize(vid_title)}.mp4')
            os.rename(vid_path, f'{sanitize(vid_title)}.mp4')
            if os.path.exists(vid_path):
                os.remove(vid_path)
            print(f'Saved {vid_title}.mp4')
        elif file_type == "MP3" or file_type == "Mp3" or file_type == "mp3":
            vid_path, vid_title = tt2mp3(link)
            if os.path.exists(f'{sanitize(vid_title)}.mp3'):
                os.remove(f'{sanitize(vid_title)}.mp3')
            os.rename(vid_path, f'{sanitize(vid_title)}.mp3')
            if os.path.exists(vid_path):
                os.remove(vid_path)
            print(f'Saved {vid_title}.mp3')
    if os.path.exists("./temp"):
        os.rmdir("./temp")