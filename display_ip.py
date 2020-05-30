import socket

hostname = socket.gethostname()
print(hostname)

IP = socket.gethostbyname(hostname)
print(IP)
