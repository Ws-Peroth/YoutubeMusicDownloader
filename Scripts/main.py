import MusicDownloader as md

print('프로그램을 종료하려면 exit 를 입력하세요')

while(True):
    link = input('영상 링크를 입력하시오 : ')
    video = md.Downloader()
    
    if(link == 'exit'): video.Finish()
    video.Start(link)
    
