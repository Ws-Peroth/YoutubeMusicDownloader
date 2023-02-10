import MusicDownloader as md

try:
    print('프로그램을 종료하려면 exit 를 입력하세요')

    while(True):
        link = input('영상 링크를 입력하시오 : ')
        
        # 다운로드 모듈 생성
        video = md.Downloader()
    
        # exit면 종료
        if(link == 'exit'): video.Finish()

        # 다운로드 시작
        video.Start(link)

except Exception as e:
    print(f"ERROR: {e}")
    print('프로그램을 종료하려면 아무 키나 누르시오...')
    input()

