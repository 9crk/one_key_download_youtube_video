import socket
from pytube import YouTube

def exe(argv1):
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
	stream.download(filename=url.split('v=')[-1].split('&')[0])



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
	while True:
		data=tcpCliSock.recv(2048)
		if not data:
			break
		url = data.decode()
		print(url)
		exe(url)
		#udp中是udpSerSock.sendto(msg.encode(),client_addr),tcp这里直接用客户端sock对象直接发送即可
		tcpCliSock.send("added successfully".encode())
		tcpCliSock.close()
		break
tcpSerSock.close()


import sys
#sys.setdefaultencoding( "utf-8" )



