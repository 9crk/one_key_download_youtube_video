import sys
#sys.setdefaultencoding( "utf-8" )
from pytube import YouTube

def exe(argv1)
	url = argv1
	yt = YouTube(url)
	#print('Avaliable Media Formats')
	streamFormat = 0
	for stream in yt.streams.all():
	#    print(stream)
	    strMe = str(stream)
	    if( "720p" in strMe and "video/mp4" in strMe and "acodec" in strMe): 
	        streamFormat = int(stream.itag)
	    else if( "360p" in strMe and "video/mp4" in strMe and "acodec" in strMe): 
	        streamFormat = int(stream.itag)
	stream = yt.streams.get_by_itag(streamFormat)
	print('Download started. Wait... ')
	stream.download(filename=url.split('v=')[-1].split('&')[0])
