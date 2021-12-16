# Créé par nantou, le 30/11/2021 en Python 3.7
#import
import random
from random import *

#fonctions
cartes = [["1trefle", "1pique", "1coeur", "1careaux"], ["2trefle", "2pique", "2coeur", "2carreaux"], ["3trefle", "3pique", "3coeur", "3carreaux"], ["4trefle", "4pique", "4coeur", "4carreaux"], ["4trefle", "4pique", "4coeur", "4carreaux"], ["5trefle", "5pique", "5coeur", "5carreaux"], ["6trefle", "6pique", "6coeur", "6carreaux"], ["7trefle", "7pique", "7coeur", "7carreaux"], ["8trefle", "8pique", "8coeur", "8carreaux"], ["9trefle", "9pique", "9coeur", "9carreaux"], ["10trefle", "10pique", "10coeur", "10carreaux"], ["Vtrefle", "Vpique", "Vcoeur", "Vcarreaux"], ["Qtrefle", "Qpique", "Qcoeur", "Qcarreaux"], ["Rtrefle", "Rpique", "Rcoeur", "Rcarreaux"]]

cartesPasDispo = []

class Game():
    def __init__(self, nbJoueurs):
        self.mise = {"mise": 20, "derniereMise": 30}
        self.nbJoueurs = nbJoueurs
        self.joueurs = []
        self.cartesPalteau = []
        self.nbManches = 0

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
        nb = randint(0, 13)
        sy = randint(0, 3)
        if cartes[nb][sy] not in cartesPasDispo:
            cartesPasDispo.append(cartes[nb][sy])
            self.main.append(cartes[nb][sy])
            self.distribution()
        else:
            self.distribution()

def jouer(joueur, game):
    print("\n##- \n ", joueur.nom, "c'est à vous de jouer ! \n-##")
    print("La mise actuelle du plateau est de:", game.mise["derniereMise"])
    manche = int(input("Que voulez vous faire ? \n [1] Vous couchez \n [2] Suivre la mise\n [3] Relancer \n"))
    if manche == 1:
        print("Vous vous êtes couchez")
        changementManche(game, joueur)
    elif manche == 2:
        joueur.solde -= 200
        print("Vous avez suivis, votre solde est actuellement de", joueur.solde)
        changementManche(game, joueur)
    elif manche == 3:
        montant = int(input("De combien voulez-vous relancez: "))
        joueur.solde -= montant
        game.mise["derniereMise"] = montant
        game.mise["mise"] = montant
        print("Vous avez relancez avec", montant, "\nvotre solde est actuellement de", joueur.solde)
        changementManche(game, joueur)
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
    if cartes[nb][sy] not in cartesPasDispo:
        cartesPasDispo.append(cartes[nb][sy])
        game.cartesPalteau.append(cartes[nb][sy])
        print("\n###############################################\n# La nouvelle carte sur le plateau est",cartes[nb][sy],"#\n###############################################")
    else:
        revelationCartes(game)

def changementManche(game, ancienJoueur):
    revelationCartes(game)
    game.nbManches += 1
    if ancienJoueur.id < game.nbJoueurs-1:
        jouer(game.joueurs[ancienJoueur.id+1], game)
    else:
        jouer(game.joueurs[0], game)


game1 = Game(2)
joueur1 = Joueur("MrPaulon", 0)
joueur2 = Joueur("Max", 1)
game1.ajoutJoueur(0, joueur1)
game1.ajoutJoueur(1, joueur2)
jouer(joueur1, game1)