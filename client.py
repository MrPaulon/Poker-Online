import socket, random
from random import random, randint

from pygame import display
from pygame.event import wait

idClient = "Client#"+str(randint(1, 9))+str(randint(1, 9))+str(randint(1, 9))+str(randint(1, 9))+""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12086))

def sendData(data):
    data = str(data)
    message = data
    data = data.encode("utf8")
    s.sendall(data)
    if message == "['Break']":
        return
    data2 =''
    data2 = s.recv(1024)
    data2 = data2.decode("utf8")
    if data2[0] == "[":
        data2 = eval(data2)
    return(data2)

def getPlayers(data):
    data = str(data)
    message = data
    data = data.encode("utf8")
    s.sendall(data)
    data2 =''
    data2 = s.recv(1024)
    data2 = data2.decode("utf8")
    data2 = int(data2)
    return(data2)

def getLogs(game):
    data = str(['logs', game])
    message = data
    data = data.encode("utf8")
    s.sendall(data)
    data2 =''
    data2 = s.recv(1024)
    data2 = data2.decode("utf8")
    return(data2)