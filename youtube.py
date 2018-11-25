from pytube import YouTube

url = input('Insert the full video URL: ')

yt = YouTube(url)

print('Avaliable Media Formats')

for stream in yt.streams.all():
    print(stream)

streamFormat = int(input("Insert the itag number: "))

stream = yt.streams.get_by_itag(streamFormat)

print('Download started. Wait... ')

stream.download()
