from random import Random, randint
import sys, time, pygame, pygame_menu, poker, client
from pygame_menu.themes import TRANSPARENT_COLOR

FPS = 60
WINDOW_SIZE = (1920, 1080)

main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
main_menu_theme.set_background_color_opacity(0.75)  # 50% opacité
clock = pygame.time.Clock()
clock.tick(FPS)
idPlayer = "Joueur#"+str(randint(1, 9))+str(randint(1, 9))+str(randint(1, 9))+str(randint(1, 9))+""

pygame.init()
surface = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.mixer.music.load('./music/Menu.wav')
#pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

def set_cartes(value, a):
    pass

def start_the_game():
    pass

def creationPartie():
    client.sendData([client.idClient, 'creerPartie', 'game01', 2])
    jeu() 

# Image de fond
background_image = pygame_menu.BaseImage(
    image_path="./img/poker.jpg"
)
def main_background() -> None:
    background_image.draw(surface)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('./img/TableJeux/7.png', [0,0])
# Jeu
def jeu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('./music/Game.mp3')
    pygame.mixer.music.play(loops=-1)
    mainjoueur = client.sendData([client.idClient, 'ajoutJoueur', 'game01', idPlayer])
    menu.disable()
    pygame.display.update()
    pygame.font.init()
    myfont = pygame.font.SysFont('Open Sans', 40)
    solde = myfont.render('Solde: '+str('500')+'', True, (255, 255, 255))
    iconCoins = pygame.image.load("./img/Icons/coins.png").convert_alpha()
    carte1joueur = pygame.image.load("./img/Cartes/" + mainjoueur[0] +".png").convert_alpha()
    carte2joueur = pygame.image.load("./img/Cartes/" + mainjoueur[1] +".png").convert_alpha()
    textBtnRelancer = myfont.render('Relancer' , True , (255, 255, 255))
    textBtnSuivre = myfont.render('Suivre' , True , (255, 255, 255))
    textBtnCoucher = myfont.render('Coucher' , True , (255, 255, 255))
    logs = myfont.render('En attente de + joueurs' , True , (255, 255, 255))
    statut = True
    while statut:
        surface.blit(pygame.transform.scale(BackGround.image, (1920, 1080)), BackGround.rect)
        #Background logs
        pygame.draw.rect(surface, (16, 16, 16), pygame.Rect(10, 10, 550, 50), 0, 15)    
        if client.getPlayers([client.idClient, 'getNumberPlayer', 'game01']) > 1:
            #if client.getPlayers([client.idClient, 'getNumberPlayer', 'game01']) > 1:
            logs = myfont.render(''+client.getLogs('game01')+'' , True , (255, 255, 255))
            #Background Solde
            ##Border Back Solde
            pygame.draw.rect(surface, (239, 45, 45), pygame.Rect(1709, 9, 193, 52), 0, 15)
            pygame.draw.rect(surface, (16, 16, 16), pygame.Rect(1710, 10, 190, 50), 0, 15)
            ###################################################
            ## Boutons
            #- Btn Relancer
            pygame.draw.rect(surface, (239, 45, 45), pygame.Rect(1720, 1020, 193, 52), 0, 10)
            surface.blit(textBtnRelancer, (1752, 1032))
            #- Btn Suivre
            pygame.draw.rect(surface, (239, 45, 45), pygame.Rect(1524, 1020, 193, 52), 0, 10)
            surface.blit(textBtnSuivre, (1570, 1032))
            #- Btn Coucher
            pygame.draw.rect(surface, (239, 45, 45), pygame.Rect(1720, 965, 193, 52), 0, 10)
            surface.blit(textBtnCoucher,(1755, 977))
            ###################################################
            surface.blit(logs, (25,20))
            surface.blit(solde, (1750,23))
            surface.blit(iconCoins, (1720,23))
            surface.blit(carte1joueur, (810, 922))
            surface.blit(carte2joueur, (940, 922))
        else:
            surface.blit(logs, (25,20))

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
        onclose=pygame_menu.events.EXIT,  # Echap
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
menu_creationPartie = pygame_menu.Menu (
    height=WINDOW_SIZE[1] * 0.5,
    onclose=pygame_menu.events.EXIT,  # Echap
    theme=main_menu_theme,
    title='Création d\'une partie',
    width=WINDOW_SIZE[0] * 0.4
)

menu_creationPartie.add.text_input("Nom de la partie : ", default='')
items = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7)]
menu_creationPartie.add.dropselect('Nombre de joueurs', items, dropselect_id='test')
menu_creationPartie.add.button("Créer la partie", creationPartie)

# Page navigation serveurs
menu_serveur = pygame_menu.Menu (
        height=WINDOW_SIZE[1] * 0.6,
        onclose=pygame_menu.events.EXIT,  # Echap
        theme=main_menu_theme,
        title='Serveurs',
        width=WINDOW_SIZE[0] * 0.5
)
menu_serveur.add.button('Partie de Poker - 3/6 joueurs - 10ms', jeu)
menu_serveur.add.button('---')
menu_serveur.add.button('Créer une partie', menu_creationPartie)

# Boutons de la page principal
menu.add.button('Jouer', menu_serveur)
menu.add.text_input('Pseudo : ', default=idPlayer)
menu.add.selector('Couleur des cartes : ', [('Rouge', 1), ('Bleu', 2)], onchange=set_cartes)
menu.add.button('Paramètres', parametres)
menu.add.button('Quitter', pygame_menu.events.EXIT)

menu.mainloop(surface, main_background, fps_limit=FPS)