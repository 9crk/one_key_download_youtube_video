import sys
import ftplib
host = '204.44.82.130'
username = 'zhouhua@disk.iloveyov.com'
password = ''
file = sys.argv[1]
f = ftplib.FTP(host)
f.login(username, password)
pwd_path = f.pwd()
print("FTP pwd:",pwd_path)
fp = open(file, 'rb')
bufsize=2048
f.storbinary('STOR ' + file, fp, bufsize)
fp.close()
