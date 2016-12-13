import socket

url = "www.naver.com"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((url,port))
s.send("GET / HTTP/1.1\r\nHost: naver.com\r\n\r\n")
data = s.recv(1024*8)
print data