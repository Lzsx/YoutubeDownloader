from pytube import YouTube, Playlist
import os
import json
import pyperclip
from rich.console import Console
from rich import print
from rich.prompt import IntPrompt

class Downloader:
    def __init__(self, video: str, path="./"):
        self.video = YouTube(video)
        self.streams = self.video.streams
        self.path = path
        self.title = self.video.title
        self.description = self.video.description
        self.thumb = self.video.thumbnail_url

    def get_max(self):
        yt = self.streams.get_highest_resolution()
        yt.download(output_path=self.path)

    def get_lowest(self):
        yt = self.streams.get_lowest_resolution()
        yt.download(output_path=self.path)

    def get_audio(self):
        yt = self.streams.filter(only_audio=True).first()
        vid = yt.download(output_path=self.path)
        base, ext = os.path.splitext(vid)
        new_file = base + ".mp3"
        os.rename(vid, new_file)

def CheckPaths(paths: list) -> list:
    ex = []
    for p in range(len(paths)):
        if os.path.exists(paths[p]):
            ex.append(paths[p])
        else:
            print(f"[bold red]{paths[p]} doesn't exists")
    return ex

def ShowOptions(options: list):
    for opt in range(len(options)):
        print(f"    {opt} | {options[opt]}")
