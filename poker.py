# Créé par paul, le 30/11/2021 en Python 3.7
# import
import random
from random import *

# fonctions
cartes = [[["1trefle", (14, "T")], ["1pique", (14, "P")], ["1coeur", (14, "C")], ["1carreaux", (14, "K")]],
          [["2trefle", (2, "T")], ["2pique", (2, "P")], ["2coeur", (2, "C")], ["2carreaux", (2, "K")]],
          [["3trefle", (3, "T")], ["3pique", (3, "P")], ["3coeur", (3, "C")], ["3carreaux", (3, "K")]],
          [["4trefle", (4, "T")], ["4pique", (4, "P")], ["4coeur", (4, "C")], ["4carreaux", (4, "K")]],
          [["5trefle", (5, "T")], ["5pique", (5, "P")], ["5coeur", (5, "C")], ["5carreaux", (5, "K")]],
          [["6trefle", (6, "T")], ["6pique", (6, "P")], ["6coeur", (6, "C")], ["6carreaux", (6, "K")]],
          [["7trefle", (7, "T")], ["7pique", (7, "P")], ["7coeur", (7, "C")], ["7carreaux", (7, "K")]],
          [["8trefle", (8, "T")], ["8pique", (8, "P")], ["8coeur", (8, "C")], ["8carreaux", (8, "K")]],
          [["9trefle", (9, "T")], ["9pique", (9, "P")], ["9coeur", (9, "C")], ["9carreaux", (9, "K")]],
          [["10trefle", (10, "T")], ["10pique", (10, "P")], ["10coeur", (10, "C")], ["10carreaux", (10, "K")]],
          [["Vtrefle", (11, "T")], ["Vpique", (11, "P")], ["Vcoeur", (11, "C")], ["Vcarreaux", (11, "K")]],
          [["Qtrefle", (12, "T")], ["Qpique", (12, "P")], ["Qcoeur", (12, "C")], ["Qcarreaux", (12, "K")]],
          [["Rtrefle", (13, "T")], ["Rpique", (13, "P")], ["Rcoeur", (13, "C")], ["Rcarreaux", (13, "K")]]]

cartesPasDispo = []


class Game():
    def __init__(self, nom, nbJoueurs):
        self.nom = nom
        self.mise = {"mise": 0, "derniereMise": 20}
        self.nbJoueurs = nbJoueurs
        self.joueurs = []
        self.joueursPasCoucher = []
        self.cartesPlateau = []
        self.nbManches = 0
        self.derniereAction = 0

    def ajoutJoueur(self, variable):
        self.joueurs.append(variable)
        self.joueursPasCoucher.append(variable)

    def enleverJoueur(self, variable):
        for joueur in self.joueurs:
            if joueur.id == variable:
                self.joueurs.remove(joueur)
                self.joueursPasCoucher.remove(joueur)


def ajoutJoueur(joueur, game):
    game.ajoutJoueur(0, joueur)


def retirerJoueur(joueur, game):
    game.enleverJoueur(0, joueur)


class Joueur():
    """Class pour le joueur"""

    def __init__(self, nom, id, solde=500):
        self.nom = nom
        self.solde = solde
        self.main = []
        self.id = id
        self.blind = 0

    ######################################################
    ## Cette méthode donner des cartes à chaque joueur ##
    ######################################################

    def distribution(self):
        if len(self.main) == 2:
            print(self.nom, self.main)
            return
        nb = randint(0, 12)
        sy = randint(0, 3)
        if cartes[nb][sy][0] not in cartesPasDispo:
            cartesPasDispo.append(cartes[nb][sy][0])
            self.main.append(cartes[nb][sy][0])
            self.distribution()
        else:
            self.distribution()


###############################################################################
## Cette fonction sert à effectuer les différentes ations possibles au poker ##
###############################################################################

def jouer(joueur, game):
    print("\n##- \n ", joueur.nom, "c'est à vous de jouer ! \n-##")
    print("La mise actuelle du plateau est de:", game.mise["derniereMise"])
    choix = int(input("Que voulez vous faire ? \n [1] Vous couchez \n [2] Suivre la mise\n [3] Relancer \n"))
    if choix == 1:
        print("Vous vous êtes couchez")
        game.joueursPasCoucher.remove(joueur)
        print(game.joueursPasCoucher)
        changementTour(game, joueur)
    elif choix == 2:
        joueur.solde -= game.mise["derniereMise"]
        game.mise["mise"] += game.mise["derniereMise"]
        print("Vous avez suivi, votre solde est actuellement de", joueur.solde)
        changementTour(game, joueur)
    elif choix == 3:
        montant = int(input("De combien voulez-vous relancez: "))
        joueur.solde -= montant
        game.mise["derniereMise"] = montant
        game.mise["mise"] += montant
        print("Vous avez relancez avec", montant, "\nvotre solde est actuellement de", joueur.solde)
        game.derniereAction = 3
        changementTour(game, joueur)
    else:
        print("Aucune action ne correspond, veuillez réessayer !")
        jouer(joueur, game)


####################################################################
## Cette fonction sert à révéler les cartes posées sur le plateau ##
####################################################################

def revelationCartes(game, cmpt=0):
    if game.nbManches == 0:
        if cmpt == 3:
            return
        revelationCartes(game, cmpt + 1)
    nb = randint(0, 12)
    sy = randint(0, 3)
    if cartes[nb][sy][0] not in cartesPasDispo:
        cartesPasDispo.append(cartes[nb][sy][0])
        game.cartesPlateau.append(cartes[nb][sy][0])
        print("\n###############################################\n# La nouvelle carte sur le plateau est",
              cartes[nb][sy][0], "#\n###############################################")
    else:
        revelationCartes(game)


###############################################################################################################################################################################
## Dans cette partie nous regardons chaque main avec les cartes sur le plateau afin de chercher les combinaisons pour chaque joueur et ensuite nous définissons le vainqueur ##
###############################################################################################################################################################################


def finPartie(game):
    print("Fin de la partie")
    gagnant = {'joueur': [], 'points': 0}
    for i in range(len(game.joueursPasCoucher)):
        joueur = game.joueursPasCoucher[i - 1]
        liste = []
        couleurs = []
        valeurs = []
        coup = []
        suite = []
        suitepossible = [[2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10],
                         [7, 8, 9, 10, 11], [8, 9, 10, 11, 12], [9, 10, 11, 12, 13], [10, 11, 12, 13, 14]]
        T = 0
        P = 0
        K = 0
        C = 0
        quinte = 0
        brelan = 0
        paire = 0
        carré = 0
        carteforte = 0
        nbfois = 0
        temppoints = 0
        for y in range(len(cartes)):  ##met les cartes du plateau dans une liste
            for x in range(len(cartes[y])):
                if cartes[y][x][0] in game.cartesPlateau:
                    liste.append(cartes[y][x][1])
        for j in range(len(cartes)):
            for x in range(len(cartes[j])):
                if cartes[j][x][0] in joueur.main:
                    liste.append(cartes[j][x][1])
        print(liste)
        for i in range(len(cartes)):  ## met les valeurs dans une liste
            for ind in range(len(cartes[i])):
                if cartes[i][ind][1] in liste:
                    valeurs.append(cartes[i][ind][1][0])
        valeurs.sort()
        for i in range(len(cartes)):  ## met les couleurs dans une liste
            for ind in range(len(cartes[i])):
                if cartes[i][ind][1] in liste:
                    couleurs.append(cartes[i][ind][1][1])
        for i in range(len(couleurs)):  ##calcul couleurs
            if couleurs[i] == 'T':
                T += 1
            if couleurs[i] == 'P':
                P += 1
            if couleurs[i] == 'K':
                K += 1
            if couleurs[i] == 'C':
                C += 1
        for i in range(len(coup)):  ##regarde si il y a suite
            if nbfois == 0:
                if coup[i][1] == 0:
                    if len(suite) >= 5:
                        if suite in suitepossible:
                            print("Quinte")
                            nbfois = 1
                            quinte += 1
                    else:
                        coup[i][1] == 0
                        suite.clear()
                if coup[i][1] == 1 or coup[i][1] == 2 or coup[i][1] == 3:
                    suite.append(coup[i][0])
        for i in range(2, 15):  ##calcul le nombre de fois qu'un nombre apparaît
            coup.append((i, valeurs.count(i)))
        for i in range(len(coup)):
            if coup[i][1] == 2:
                paire += 1
            if coup[i][1] == 3:
                brelan += 1
            if coup[i][1] == 4:
                carré += 1
        ##Cherche la/les combinaisons##
        if paire == 0 and brelan == 0 and carré == 0 and quinte == 0:
            print("Carte Haute")
            temppoints = 1
        if paire == 1:
            print("Paire")
            temppoints = 2
        if paire == 3:
            print("Double Paire")
            temppoints = 3
        if paire == 2:
            print("Double Paire")
            temppoints = 3
        if brelan == 1:
            print("Brelan")
            temppoints = 4
        if quinte == 1:
            print("Quinte")
            temppoints = 5
        if quinte == 1:
            print("Quinte")
            temppoints = 5
        if T == 5 or P == 5 or K == 5 or C == 5:
            print("Couleur")
            temppoints = 6
        if brelan == 1 and paire == 1:
            print("Full House")
            temppoints = 7
        if brelan == 2:
            print("Full House")
            temppoints = 7
        if carré == 1:
            print("Carré")
            temppoints = 8
        if T == 5 or P == 5 or C == 5 or K == 5:
            if valeurs == [10, 11, 12, 13, 14]:
                print("Quinte Flush Royale")
                temppoints = 10
            if quinte == 1:
                print("Quinte Flush")
                temppoints = 9
        if temppoints > gagnant['points']:
            gagnant['joueur'] = []
            gagnant['joueur'].append(joueur.nom)
            gagnant['points'] = temppoints
        elif temppoints == gagnant['points']:
            gagnant['joueur'].append(joueur.nom)
    if len(gagnant['joueur']) == 1:
        pass
    print(gagnant)
    for r in range(len(gagnant['joueur'])):
        for e in range(len(game.joueursPasCoucher)):
            nombrejoueursgagnant = len(gagnant['joueur'])
            if game.joueursPasCoucher[e].nom == gagnant['joueur'][r]:
                joueurgagnant = game.joueursPasCoucher[e]
                joueurgagnant.solde += game.mise['mise'] / nombrejoueursgagnant
                print(game.mise['mise'])
                print(joueurgagnant.solde)
    game.joueursPasCoucher = []
    game.cartesPlateau = []
    game.nbManches = 0
    game.mise['derniereMise'] = 20
    for a in range(len(game.joueurs)):
        game.joueursPasCoucher.append(game.joueurs[a])
    jouer(game.joueursPasCoucher[0], game)


## fonction permettant le changement de manche ##

def changementManche(game):
    revelationCartes(game)
    game.nbManches += 1


## fonction permettant le changement de joueurs, pour que chaque joueur joue ##

def changementTour(game, ancienJoueur):
    if game.joueurs.index(ancienJoueur) < game.nbJoueurs - 1:
        if game.joueurs[game.joueurs.index(ancienJoueur)] in game.joueursPasCoucher:
            jouer(game.joueursPasCoucher[game.joueursPasCoucher.index(ancienJoueur) + 1], game)
        else:
            changementTour(game, game.joueurs[game.joueurs.index(ancienJoueur) + 1])
    else:
        if len(game.cartesPlateau) == 5:
            finPartie(game)
        else:
            changementManche(game)
            jouer(game.joueursPasCoucher[0], game)
