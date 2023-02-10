import MusicDownloader as md

try:
    print('프로그램을 종료하려면 exit 를 입력하세요')

    while(True):
        link = input('영상 링크를 입력하시오 : ')
        video = md.Downloader()
    
        if(link == 'exit'): video.Finish()
        video.Start(link)
except Exception as e:
    print(f"ERROR: {e}")
    print('프로그램을 종료하려면 아무 키나 누르시오...')
    input()
