import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("141.94.98.66", 12086))

print("message à envoyer:")
data = input(">> ")
data = data.encode("utf8")
s.sendall(data)