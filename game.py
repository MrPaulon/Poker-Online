from random import Random, randint
import sys, time, pygame, pygame_menu, client
from pygame_menu.themes import TRANSPARENT_COLOR

FPS = 60
main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
main_menu_theme.set_background_color_opacity(0.75)  # 50% opacité
clock = pygame.time.Clock()
clock.tick(FPS)
idPlayer = "Joueur#" + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + ""

pygame.init()
infoObject = pygame.display.Info()
surface = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
WINDOW_SIZE = (1920, 1080)
FENETRE = (infoObject.current_w, infoObject.current_h)
pygame.mixer.music.load('./music/Menu.wav')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)


def set_cartes(value, a):
    pass


def start_the_game():
    pass


def creationPartie(game_name, num_players):
    for valeur in client.sendData('partieouverte'):
        if game_name == valeur[0]:
            return
    client.sendData([client.idClient, 'creerPartie', game_name, num_players])
    jeu(game_name, num_players)


# Image de fond
background_image = pygame_menu.BaseImage(
    image_path="./img/poker.jpg"
)


def main_background() -> None:
    background_image.draw(surface)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def fermeture():
    client.sendData(['Break'])
    pygame.quit()
    sys.exit()





# Jeu
def jeu(game_name, nbJoueurs):
    if game_name == "":
        game_name = "game01"
    BackGround = Background(f'./img/TableJeux/{nbJoueurs}.png', [0, 0])
    pygame.mixer.music.stop()
    pygame.mixer.music.load('./music/Game.mp3')
    pygame.mixer.music.play(loops=-1)
    mainjoueur = client.sendData([client.idClient, 'ajoutJoueur', game_name, idPlayer])
    menu.disable()
    pygame.display.update()
    pygame.font.init()
    myfont = pygame.font.SysFont('Open Sans', int(FENETRE[1] * 0.037))
    solde = myfont.render('Solde: ' + str('500') + '', True, (255, 255, 255))
    iconCoins = pygame.image.load("./img/Icons/coins.png").convert_alpha()
    carte1joueur = pygame.image.load("./img/Cartes/" + mainjoueur[0] + ".png").convert_alpha()
    carte2joueur = pygame.image.load("./img/Cartes/" + mainjoueur[1] + ".png").convert_alpha()
    textBtnRelancer = myfont.render('Relancer', True, (255, 255, 255))
    textBtnSuivre = myfont.render('Suivre', True, (255, 255, 255))
    textBtnCoucher = myfont.render('Coucher', True, (255, 255, 255))
    logs = myfont.render('En attente de + joueurs', True, (255, 255, 255))
    statut = True
    while statut:
        cartesPlateau = client.sendData([client.idClient, 'getCartesPlateau', game_name])
        if len(cartesPlateau) >= 1:
            carte1plateau = pygame.image.load("./img/Cartes/" + cartesPlateau[0] + ".png").convert_alpha()
            carte1plateau = pygame.transform.scale(carte1plateau, (47, 62))
            if len(cartesPlateau) >= 2:
                carte2plateau = pygame.image.load("./img/Cartes/" + cartesPlateau[1] + ".png").convert_alpha()
                carte2plateau = pygame.transform.scale(carte2plateau, (47, 62))
                if len(cartesPlateau) >= 3:
                    carte3plateau = pygame.image.load("./img/Cartes/" + cartesPlateau[2] + ".png").convert_alpha()
                    carte3plateau = pygame.transform.scale(carte3plateau, (47, 62))
                    if len(cartesPlateau) >= 4:
                        carte4plateau = pygame.image.load("./img/Cartes/" + cartesPlateau[3] + ".png").convert_alpha()
                        carte4plateau = pygame.transform.scale(carte4plateau, (47, 62))
                        if len(cartesPlateau) >= 5:
                            carte5plateau = pygame.image.load(
                                "./img/Cartes/" + cartesPlateau[4] + ".png").convert_alpha()
                            carte5plateau = pygame.transform.scale(carte5plateau, (47, 62))
                        else:
                            carte5plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
                            carte5plateau = pygame.transform.scale(carte5plateau, (47, 62))
                    else:
                        carte4plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
                        carte4plateau = pygame.transform.scale(carte4plateau, (47, 62))
                else:
                    carte3plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
                    carte3plateau = pygame.transform.scale(carte3plateau, (47, 62))
            else:
                carte2plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
                carte2plateau = pygame.transform.scale(carte2plateau, (47, 62))
        else:
            carte1plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
            carte1plateau = pygame.transform.scale(carte1plateau, (47, 62))
            carte2plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
            carte2plateau = pygame.transform.scale(carte2plateau, (47, 62))
            carte3plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
            carte3plateau = pygame.transform.scale(carte3plateau, (47, 62))
            carte4plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
            carte4plateau = pygame.transform.scale(carte4plateau, (47, 62))
            carte5plateau = pygame.image.load("./img/Cartes/dos.png").convert_alpha()
            carte5plateau = pygame.transform.scale(carte5plateau, (47, 62))
        nbjoueurs = client.getPlayers([client.idClient, 'getNumberPlayer', game_name])
        surface.blit(pygame.transform.scale(BackGround.image, (infoObject.current_w, infoObject.current_h)),
                     BackGround.rect)
        # Background logs
        pygame.draw.rect(surface, (16, 16, 16),
                         pygame.Rect(FENETRE[0] * 0.008, FENETRE[1] * 0.008, FENETRE[0] * 0.287, FENETRE[1] * 0.0465),
                         0)
        if nbjoueurs > 1:
            logs = myfont.render('' + client.getLogs(game_name) + '', True, (255, 255, 255))
            # Background Solde
            ##Border Back Solde
            pygame.draw.rect(surface, (239, 45, 45),
                             pygame.Rect(FENETRE[0] * 0.894, FENETRE[1] * 0.008, FENETRE[0] * 0.1, FENETRE[1] * 0.049),
                             0)
            pygame.draw.rect(surface, (16, 16, 16),
                             pygame.Rect(FENETRE[0] * 0.895, FENETRE[1] * 0.0086, FENETRE[0] * 0.098,
                                         FENETRE[1] * 0.0465), 0)
            ###################################################
            ## Boutons
            # - Btn Relancer
            pygame.draw.rect(surface, (239, 45, 45),
                             pygame.Rect(FENETRE[0] * 0.895, FENETRE[1] * 0.945, FENETRE[0] * 0.1, FENETRE[1] * 0.0465),
                             0)
            surface.blit(textBtnRelancer, (FENETRE[0] * 0.913, FENETRE[1] * 0.956))
            # - Btn Suivre
            pygame.draw.rect(surface, (239, 45, 45),
                             pygame.Rect(FENETRE[0] * 0.792, FENETRE[1] * 0.945, FENETRE[0] * 0.1, FENETRE[1] * 0.0465),
                             0)
            surface.blit(textBtnSuivre, (FENETRE[0] * 0.818, FENETRE[1] * 0.956))
            # - Btn Coucher
            pygame.draw.rect(surface, (239, 45, 45),
                             pygame.Rect(FENETRE[0] * 0.895, FENETRE[1] * 0.894, FENETRE[0] * 0.1, FENETRE[1] * 0.0465),
                             0)
            surface.blit(textBtnCoucher, (FENETRE[0] * 0.913, FENETRE[1] * 0.904))
            ###################################################
            surface.blit(logs, (FENETRE[0] * 0.02, FENETRE[1] * 0.018))
            surface.blit(solde, (FENETRE[0] * 0.918, FENETRE[1] * 0.022))
            iconCoins = pygame.transform.scale(iconCoins, (int(FENETRE[1] * 0.023), int(FENETRE[1] * 0.023)))
            surface.blit(iconCoins, (FENETRE[0] * 0.9, FENETRE[1] * 0.022))
            carte1joueur = pygame.transform.scale(carte1joueur, (int(FENETRE[0] * 0.095), int(FENETRE[1] * 0.22)))
            carte2joueur = pygame.transform.scale(carte2joueur, (int(FENETRE[0] * 0.095), int(FENETRE[1] * 0.22)))
            surface.blit(carte1joueur, (FENETRE[0] * 0.422, FENETRE[1] * 0.852))
            surface.blit(carte2joueur, (FENETRE[0] * 0.49, FENETRE[1] * 0.852))
            ##
            surface.blit(carte1plateau, (FENETRE[0] * 0.437, FENETRE[1] * 0.45))
            surface.blit(carte2plateau, (FENETRE[0] * 0.463, FENETRE[1] * 0.45))
            surface.blit(carte3plateau, (FENETRE[0] * 0.489, FENETRE[1] * 0.45))
            surface.blit(carte4plateau, (FENETRE[0] * 0.515, FENETRE[1] * 0.45))
            surface.blit(carte5plateau, (FENETRE[0] * 0.541, FENETRE[1] * 0.45))
        else:
            surface.blit(logs, (FENETRE[0] * 0.02, FENETRE[0] * 0.016))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                client.sendData(['Break'])
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('./music/Menu.wav')
                    pygame.mixer.music.play(loops=-1)
                    statut = False
                    menu.enable()
        pygame.display.flip()


# Page principal
menu = pygame_menu.Menu(
    height=WINDOW_SIZE[1] * 0.4,
    onclose=fermeture,  # Echap
    theme=main_menu_theme,
    title='Accueil',
    width=WINDOW_SIZE[0] * 0.3
)

# Page paramètres
parametres = pygame_menu.Menu(
    height=WINDOW_SIZE[1] * 0.5,
    onclose=pygame_menu.events.EXIT,  # Echap
    theme=main_menu_theme,
    title='Paramètres',
    width=WINDOW_SIZE[0] * 0.4
)
parametres.add.selector('Langue :', [('Français', 1), ('Anglais', 2), ('Espagnol', 3)])
parametres.add.selector('Région :', [('Europe', 1), ('US', 2)])
parametres.add.toggle_switch('Chat écrit')
parametres.add.toggle_switch('Musique')
parametres.add.toggle_switch('Afficher statut du réseaux')

# Page création partie
menu_creationPartie = pygame_menu.Menu(
    height=WINDOW_SIZE[1] * 0.5,
    onclose=pygame_menu.events.EXIT,  # Echap
    theme=main_menu_theme,
    title='Création d\'une partie',
    width=WINDOW_SIZE[0] * 0.4
)

game_name = ""
num_players = 2


def set_name(value):
    global game_name
    game_name = value


def set_num_players(value, num):
    global num_players
    num_players = num


def set_name_players(value):
    global idPlayer
    idPlayer = value

menu_creationPartie.add.text_input("Nom de la partie : ", default='', onchange=set_name)
items = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7)]
menu_creationPartie.add.dropselect('Nombre de joueurs', items, onchange=set_num_players)
menu_creationPartie.add.button("Créer la partie", lambda: creationPartie(game_name, num_players))

# Page navigation serveurs
menu_serveur = pygame_menu.Menu(
    height=WINDOW_SIZE[1] * 0.6,
    onclose=pygame_menu.events.EXIT,  # Echap
    theme=main_menu_theme,
    title='Serveurs',
    width=WINDOW_SIZE[0] * 0.5
)
for partie in client.sendData('partieouverte'):
    if partie[1] != partie[2]:
        menu_serveur.add.button(f'Partie de Poker {partie[0]} - {partie[1]}/{partie[2]} joueurs', lambda: jeu(partie[0], partie[2]))
menu_serveur.add.button('---')
menu_serveur.add.button('Créer une partie', menu_creationPartie)

# Boutons de la page principal
menu.add.button('Jouer', menu_serveur)
menu.add.text_input('Pseudo : ', default=idPlayer, onchange=set_name_players)
menu.add.selector('Couleur des cartes : ', [('Rouge', 1), ('Bleu', 2)], onchange=set_cartes)
menu.add.button('Paramètres', parametres)
menu.add.button('Quitter', fermeture)

menu.mainloop(surface, main_background, fps_limit=FPS)
