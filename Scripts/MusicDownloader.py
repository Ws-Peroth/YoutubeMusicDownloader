from pytube import YouTube
from pytube import Playlist
import glob
import os

defaultPath = "C:/Users/User/OneDrive/바탕 화면/Files/music"

class Downloader():

    # 파일 경로에 들어갈 수 없는 문자 리스트
    banlist = ['/', '\\', '*', '.', '?', '%', ':', '|', '"', "'", ]

    def __init__(self):
        self.link = ''
  
    def Start(self, link):
        self.link = link

        print("Start")

        # 플레이리스트 링크
        if( '/playlist?list=' in self.link):
            print("플레이 리스트 전체 다운로드")

            # 플레이 리스트 정보 생성
            playlist = Playlist(self.link)
            videolist = playlist.videos
            length = len(videolist)

            # 길이가 0인 플레이 리스트에 대한 예외처리
            if length == 0:
                print('Playelist does not exist\n')
                return

            # 플레이리스트 다운로드 실행
            for i in range(0, length):
                self.Download(videolist[i])
                print(f"Downloading... ({i + 1}/{length})")

        else:   # 단일 영상 다운로드
            video = None
            try:
                # 영상 정보 파일 생성
                video = YouTube(self.link)
            except:
                print('This link is invalid.\n')
                return

            # 다운로드 실행
            self.Download(video)

        print("Download Finish\n")

    def Download(self, video, onlyAudio = True):
        # 영상업로더의 이름을 가져옴
        auth = video.author

        # 만약 업로더의 이름에 파일에 들어갈 수 없는 문자가 있다면 - 로 바꿔줌
        for i in Downloader.banlist:
            if i in auth:
                auth = auth.replace(i, '-')

        # 경로 생성
        path = f"{defaultPath}/{auth}/"
        print(path)

        # 다운로드 함수
        video.streams.filter(only_audio=onlyAudio).first().download(path)
        self.ChangeFileType(path)

    def ChangeFileType(self, filePath):
        # 저장할 경로의 폴더 내의 mp4파일 목록
        # 파일 저장 타입은 mp3임으로 mp4 파일이 있다면 다운 받은 파일이라는 의미
        files = glob.glob(filePath + "*.mp4")

        for x in files:
            # 경로가 아니다, 즉 파일일 경우
            if not os.path.isdir(x):

                # 파일의 확장자를 제외한 부분을 가져옴
                filename = os.path.splitext(x)

                try:
                    # mp4 부분을 지우고 mp3 부분을 넣어 이름 변경함 (rename)
                    os.rename(x,filename[0] + '.mp3')
                    print(f"Download Success : {filename[0]}")
                except:
                    # 이미 존재하는 파일일 경우에 예외처리
                    print(f"The file is already Exists : {filename[0]}")
                    os.remove(x)

    # 프로그램 종료
    def Finish(self):
        input('press any key...')
        exit()