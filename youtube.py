import sys
#sys.setdefaultencoding( "utf-8" )
from pytube import YouTube

url = sys.argv[1]
#input('Insert the full video URL: ')

yt = YouTube(url)

#print('Avaliable Media Formats')
streamFormat = 0
for stream in yt.streams.all():
#    print(stream)
    strMe = str(stream)
#    print(len(sys.argv),sys.argv[3])
    if (len(sys.argv)>=4 and sys.argv[3]=='360'):
        if( "360p" in strMe and "video/mp4" in strMe and "acodec" in strMe): 
            streamFormat = int(stream.itag)
    else:
        if( "720p" in strMe and "video/mp4" in strMe and "acodec" in strMe): 
            streamFormat = int(stream.itag)
#print(streamFormat)

#streamFormat = int(input("Insert the itag number: "))

stream = yt.streams.get_by_itag(streamFormat)

print('Download started. Wait... ')
if len(sys.argv) >= 3:
    stream.download(filename=sys.argv[2])
else:
    stream.download(filename='output')
