import socket

url = "www.google.com"
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("HIHI", (url, port))
print "send"

data, addr = s.recvfrom(4096)

print "recv"
print data