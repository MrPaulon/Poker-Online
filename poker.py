# Créé par paul, le 30/11/2021 en Python 3.7
#import
import random
from random import *

#fonctions
cartes = [[["1trefle", (14, "T")], ["1pique", (14, "P")], ["1coeur", (14, "C")], ["1carreaux", (14, "K")]], [["2trefle", (2, "T")], ["2pique", (2, "P")], ["2coeur", (2, "C")], ["2carreaux", (2, "K")]], [["3trefle", (3, "T")], ["3pique", (3, "P")], ["3coeur", (3, "C")], ["3carreaux", (3, "K")]], [["4trefle", (4, "T")], ["4pique", (4, "P")], ["4coeur", (4, "C")], ["4carreaux", (4, "K")]], [["5trefle", (5, "T")], ["5pique", (5, "P")], ["5coeur", (5, "C")], ["5carreaux", (5, "K")]],[["6trefle", (6, "T")], ["6pique", (6, "P")], ["6coeur", (6, "C")], ["6carreaux", (6, "K")]], [["7trefle", (7, "T")], ["7pique", (7, "P")], ["7coeur", (7, "C")], ["7carreaux", (7, "K")]], [["8trefle", (8, "T")], ["8pique", (8, "P")], ["8coeur", (8, "C")], ["8carreaux", (8, "K")]], [["9trefle", (9, "T")], ["9pique", (9, "P")], ["9coeur", (9, "C")], ["9carreaux", (9, "K")]], [["10trefle", (10, "T")], ["10pique", (10, "P")], ["10coeur", (10, "C")], ["10carreaux", (10, "K")]], [["Vtrefle", (11, "T")], ["Vpique", (11, "P")], ["Vcoeur", (11, "C")], ["Vcarreaux", (11, "K")]], [["Qtrefle", (12, "T")], ["Qpique", (12, "P")], ["Qcoeur", (12, "C")], ["Qcarreaux", (12, "K")]], [["Rtrefle", (13, "T")], ["Rpique", (13, "P")], ["Rcoeur", (13, "C")], ["Rcarreaux", (13, "K")]]]

combi = {"quinteFlushRoyale": ["10coeur", "Vcoeur", "Qcoeur", "Rcoeur", "1coeur"], "quinteFlush": ["8coeur", "9coeur", "10coeur", "Vcoeur", "Qcoeur"], "carre": ["8coeur", "9coeur", "10coeur", "Vcoeur", "Qcoeur"]}

cartesPasDispo = []

class Game():
    def __init__(self, nbJoueurs):
        self.mise = {"mise": 20, "derniereMise": 30}
        self.nbJoueurs = nbJoueurs
        self.joueurs = []
        self.cartesPlateau = []
        self.nbManches = 0
        self.derniereAction = 0

    def ajoutJoueur(self, id , variable):
        self.joueurs.append(variable)

class Joueur():
    """Class pour le joueur"""
    def __init__(self, nom, id, solde = 500):
        self.nom = nom
        self.solde = solde
        self.main = []
        self.id = id
        self.blind = 0

    def distribution(self):
        if len(self.main) == 2:
            print(self.main)
            return
        nb = randint(0, 12)
        sy = randint(0, 3)
        if cartes[nb][sy][0] not in cartesPasDispo:
            cartesPasDispo.append(cartes[nb][sy][0])
            self.main.append(cartes[nb][sy][0])
            self.distribution()
        else:
            self.distribution()

def jouer(joueur, game):
    print("\n##- \n ", joueur.nom, "c'est à vous de jouer ! \n-##")
    print("La mise actuelle du plateau est de:", game.mise["derniereMise"])
    choix = int(input("Que voulez vous faire ? \n [1] Vous couchez \n [2] Suivre la mise\n [3] Relancer \n"))
    if choix == 1:
        print("Vous vous êtes couchez")
        changementTour(game, joueur)
    elif choix == 2:
        joueur.solde -= game.mise["derniereMise"]
        print("Vous avez suivis, votre solde est actuellement de", joueur.solde)
        changementTour(game, joueur)
    elif choix == 3:
        montant = int(input("De combien voulez-vous relancez: "))
        joueur.solde -= montant
        game.mise["derniereMise"] = montant
        game.mise["mise"] = montant
        print("Vous avez relancez avec", montant, "\nvotre solde est actuellement de", joueur.solde)
        game.derniereAction = 3
        changementTour(game, joueur)
    else:
        print("Aucune action ne correspond, veuillez réessayer !")
        jouer(joueur, game)


def revelationCartes(game, cmpt=0):
    if game.nbManches == 0:
        if cmpt == 3:
            return
        revelationCartes(game, cmpt+1)
    nb = randint(0, 13)
    sy = randint(0, 3)
    if cartes[nb][sy][0] not in cartesPasDispo:
        cartesPasDispo.append(cartes[nb][sy][0])
        game.cartesPlateau.append(cartes[nb][sy][0])
        print("\n###############################################\n# La nouvelle carte sur le plateau est",cartes[nb][sy][0],"#\n###############################################")
    else:
        revelationCartes(game)

def finPartie(game):
    print("Fin de la partie")
    for i in range(len(game.joueurs)):
        joueur = game.joueurs[i-1]
        liste = []
        for y in range(len(game.cartesPlateau)):
            liste.append(game.cartesPlateau[y])
        for j in range(len(joueur.main)):
            liste.append(joueur.main[j])
        for cle,valeur in combi.items():
            print("Valeur de la clé:", valeur,"\nListe:", liste)
            if valeur in liste:
                print("ok")
                if cle == "quinteFlushRoyale":
                    print("Okok")
            else:
                print(joueur.nom, "salade")


def changementManche(game):
    revelationCartes(game)
    game.nbManches += 1

def changementTour(game, ancienJoueur):
    if ancienJoueur.id < game.nbJoueurs-1:
        jouer(game.joueurs[ancienJoueur.id+1], game)
    else:
        if len(game.cartesPlateau) == 5:
            finPartie(game)
        else:
            changementManche(game)
            jouer(game.joueurs[0], game)


game1 = Game(2)
mrpaulon = Joueur("MrPaulon", 0)
mrpaulon.distribution()
maxgp78 = Joueur("Maxgp78", 1)
maxgp78.distribution()
game1.ajoutJoueur(0, mrpaulon)
game1.ajoutJoueur(1, maxgp78)
jouer(mrpaulon, game1)