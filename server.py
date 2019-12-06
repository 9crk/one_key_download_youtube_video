import socket
import os
from pytube import YouTube

def exe(argv1):
	if len(argv1) < 20:
		return
	url = argv1
	yt = YouTube(url)
	streamFormat = 0
	for stream in yt.streams.all():
	#    print(stream)
		strMe = str(stream)
		if( "720p" in strMe and "video/mp4" in strMe and "acodec" in strMe):
			streamFormat = int(stream.itag)
		else:
			if( "360p" in strMe and "video/mp4" in strMe and "acodec" in strMe):
				streamFormat = int(stream.itag)
	stream = yt.streams.get_by_itag(streamFormat)
	print('Download started. Wait... ')
	stream.download(filename="tmp")        
	os.system("mv tmp.* /var/www/html/v/"+url.split('v=')[-1].split('&')[0])



host=''
port=12345
addr=(host,port)
tcpSerSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSerSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSerSock.bind(addr)
tcpSerSock.listen(5)


#上面部分除了指明的通信协议---SOCK_STREAM不同，其他相同
while True:
	print('尝试连接客户端……')

#udp中是recvfrom(buffersize),tcp这里用accept()；tcp这里接收到的是客户端的sock对象，后面接受数据时使用socket.recv()
	tcpCliSock,client_addr=tcpSerSock.accept() #等待接受连接
	print('连接成功，客户端地址为：',client_addr)
	tcpCliSock.send("\ninput password: ".encode())
	data=tcpCliSock.recv(2048)
	if not data:
		tcpCliSock.close()
		continue
	if data.decode(errors='ignore')[0:7] != "zhouhua":
		print(data.decode(errors='ignore'))
		tcpCliSock.close()
		continue
	tcpCliSock.send("\nLogin Success,input url: ".encode())
	data=tcpCliSock.recv(2048)
	if not data:
		tcpCliSock.close()
		continue
	url = data.decode(errors='ignore')
	print(url)
	exe(url)
	#udp中是udpSerSock.sendto(msg.encode(),client_addr),tcp这里直接用客户端sock对象直接发送即可
	tcpCliSock.send("\nadded successfully\n".encode())
	tcpCliSock.close()
tcpSerSock.close()


import sys
#sys.setdefaultencoding( "utf-8" )



