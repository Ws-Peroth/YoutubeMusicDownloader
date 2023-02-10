from pytube import YouTube
from pytube import Playlist
import glob
import os

defaultPath = "C:/Users/User/OneDrive/바탕 화면/Files/music"

class Downloader():

    banlist = ['/', '\\', '*', '.', '?', '%', ':', '|', '"', "'", ]

    def __init__(self):
        self.link = ''
  
    def Start(self, link):
        self.link = link

        print("Start")
        if( '/playlist?list=' in self.link):
            print("플레이 리스트 전체 다운로드")

            playlist = Playlist(self.link)
            videolist = playlist.videos
            length = len(videolist)

            if length == 0:
                print('Playelist does not exist\n')
                return

            for i in range(0, length):
                self.Download(videolist[i])
                print(f"Downloading... ({i + 1}/{length})")
        else:
            video = None
            try:
                video = YouTube(self.link)
            except:
                print('This link is invalid.\n')
                return
            self.Download(video)

        print("Download Finish\n")

    def ChangeFileType(self, filePath):
        files = glob.glob(filePath + "*.mp4")

        for x in files:
            if not os.path.isdir(x):
                filename = os.path.splitext(x)
                try:
                    os.rename(x,filename[0] + '.mp3')
                    print(f"Download Success : {filename[0]}")
                except:
                    print(f"The file is already Exists : {filename[0]}")
                    os.remove(x)

    def Download(self, video, onlyAudio = True):
        auth = video.author
        for i in Downloader.banlist:
            if i in auth:
                auth = auth.replace(i, '-')

        path = f"{defaultPath}/{auth}/"
        print(path)
        video.streams.filter(only_audio=onlyAudio).first().download(path)
        self.ChangeFileType(path)

    def Finish(self):
        input('press any key...')
        exit()