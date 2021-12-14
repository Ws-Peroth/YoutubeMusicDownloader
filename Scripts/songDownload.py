from pytube import YouTube
from pytube import Playlist
import glob
import os

defaultPath = "C:/Users/User/OneDrive/바탕 화면/Files/music"

def ChangeFileType(filePath):
    files = glob.glob(filePath + "*.mp4")
    
    for x in files:
        if not os.path.isdir(x):
            filename = os.path.splitext(x)
            try:
                os.rename(x,filename[0] + '.mp3')
            except:
                print(f"The file is already Exists : {filename[0]}")
                os.remove(x)

def Download(video):
    path = f"{defaultPath}/{video.author}/"
    video.streams.filter(only_audio=True).first().download(path)
    ChangeFileType(path)
    print(f"Download Success : {video.title}")


link = input('영상 링크를 입력하시오 : ')
print("Start")

if( '/playlist?list=' in link):
    print("플레이 리스트 전체 다운로드")
    
    playlist = Playlist(link)
    videolist = playlist.videos
    length = len(videolist)
    
    for i in range(0, length):
        Download(videolist[i])
        print(f"Downloading... ({i + 1}/{length})")
        
else:
    Download(YouTube(link))

print("Download Finish")
