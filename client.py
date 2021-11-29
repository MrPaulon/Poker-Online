import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.20.35.61", 12086))

print("Le nom du fichier que vous voulez récupérer:")
data = input(">> ")
data = data.encode("utf8")
s.sendall(data)
