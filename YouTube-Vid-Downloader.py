from pytube import YouTube
from colorama import Fore, Back, Style
import shutup
try:    
    shutup.please()
    url = input('Enter Link Of Video : ')
    video = YouTube(url)
    print(f'\nTitle : {video.title}')
    _stream = video.streams.all()
    list_stream = list(enumerate(_stream))
    n = 0
    for stream in video.streams:
        
        size = f'[{int(stream.filesize/(1024*1024))} MB]'
        
        if str(stream).__contains__('acodec')  and str(stream).__contains__('video'):
            print(f'\n{list_stream[n][0]}. {stream.resolution}, {stream.type}, {size}')
        
        elif str(stream).__contains__('audio'):
            print(f'\n{list_stream[n][0]}. {stream.abr}, {stream.type} {size}')
        
        else:
            None
        n = n + 1
    
    quality = int(input('\nEnter Option : '))
    print(Fore.GREEN)
    print('\nDownloading...')
    _stream[quality].download()
    print('\nSuccessfully Downloaded!')
    print(Style.RESET_ALL)
    
except:
    print('\nSomething Went Wrong!')