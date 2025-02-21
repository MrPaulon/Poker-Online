# coding: utf-8

import socket, threading, poker

clientConnus = {}
gameConnus = []
logs = [["game01", ""]]


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port,))
        while True:
            r = self.clientsocket.recv(2048)
            r = r.decode("utf8")
            if r == "partieouverte":
                data = []
                for game in gameConnus:
                    data.append([game[0].nom, game[1], game[0].nbJoueurs])
                data = str(data)
                data = data.encode("utf8")
                self.clientsocket.sendall(data)
            else:
                r = eval(r)
                if r[0] == "Break":
                    game = r[2]
                    id_joueur = r[3]
                    for y in range(len(gameConnus)):
                        if game == gameConnus[y][0].nom:
                            gameConnus[y][1] -= 1
                            print("NbJoueurs:", gameConnus[y][0].nom, gameConnus[y][1])
                            gameConnus[y][0].retirerJoueur(id_joueur)
                            for i in range(len(logs)):
                                if logs[i][0] == gameConnus[y][0].nom:
                                    logs[i][1] = "" + str(joueur.nom) + " vient de partir de la partie"
                    data = "" + str(joueur.main) + ""
                    data = data.encode("utf8")
                    self.clientsocket.sendall(data)
                    break
                else:
                    if r[1] == "creerPartie":
                        game_name = r[2]
                        nbjoueurs = r[3]
                        game = poker.Game(game_name, nbjoueurs)
                        gameConnus.append([game, 0])
                        data = "Game crée"
                        data = data.encode("utf8")
                        self.clientsocket.sendall(data)
                        logs.append([game.nom, ""])
                    elif r[1] == "ajoutJoueur":
                        game = r[2]
                        joueur = r[3]
                        joueur = poker.Joueur(joueur, 1)
                        joueur.distribution()
                        for y in range(len(gameConnus)):
                            if game == gameConnus[y][0].nom:
                                gameConnus[y][1] += 1
                                print("NbJoueurs:", gameConnus[y][0].nom, gameConnus[y][1])
                                gameConnus[y][0].ajoutJoueur(joueur)
                                for i in range(len(logs)):
                                    if logs[i][0] == gameConnus[y][0].nom:
                                        logs[i][1] = "" + str(joueur.nom) + " vient d'arriver dans la partie"
                        data = "" + str(joueur.main) + ""
                        data = data.encode("utf8")
                        self.clientsocket.sendall(data)
                    elif r[0] == "logs":
                        game = r[1]
                        for y in range(len(gameConnus)):
                            for i in range(len(logs)):
                                if logs[i][0] == gameConnus[y][0].nom:
                                    data = logs[i][1]
                        data = data.encode("utf8")
                        self.clientsocket.sendall(data)
                    elif r[1] == "getNumberPlayer":
                        game = r[2]
                        for y in range(len(gameConnus)):
                            if game == gameConnus[y][0].nom:
                                data = gameConnus[y][1]
                        data = str(data)
                        data = data.encode("utf8")
                        self.clientsocket.sendall(data)
                    elif r[1] == "getCartesPlateau":
                        game = r[2]
                        data = ""
                        for y in range(len(gameConnus)):
                            if game == gameConnus[y][0].nom:
                                data = gameConnus[y][0].cartesPlateau
                        data = str(data)
                        data = data.encode("utf8")
                        self.clientsocket.sendall(data)
                    else:
                        data = "Recu"
                        data = data.encode("utf8")
                        self.clientsocket.sendall(data)
        print("Client déconnecté...")


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("127.0.0.1", 55555))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
