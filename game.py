import sys, time, pygame, pygame_menu
from pygame_menu.themes import TRANSPARENT_COLOR

FPS = 60
WINDOW_SIZE = (1920, 1080)

main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
main_menu_theme.set_background_color_opacity(0.75)  # 50% opacité
clock = pygame.time.Clock()
clock.tick(FPS)

pygame.init()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def set_cartes(value, a):
    pass

def start_the_game():
    pass

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
    menu.disable()
    pygame.display.update()
    pygame.font.init()
    myfont = pygame.font.SysFont('Open Sans', 40)
    logs = myfont.render('Max vient de relancer avec 240 jetons' , True , (255, 255, 255))
    solde = myfont.render('Solde: 500', True, (255, 255, 255))
    carte1joueur = pygame.image.load("./img/Cartes/2Coeur.png").convert_alpha()
    carte2joueur = pygame.image.load("./img/Cartes/2Coeur.png").convert_alpha()
    statut = True
    while statut:
        surface.blit(pygame.transform.scale(BackGround.image, (1920, 1080)), BackGround.rect)
        pygame.draw.rect(surface, (16, 16, 16), pygame.Rect(10, 10, 550, 50), 0, 15)
        surface.blit(logs, (25,20))
        surface.blit(solde, (1750,0))
        surface.blit(carte1joueur, (815, 950))
        surface.blit(carte2joueur, (935, 950))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
parametres.add.toggle_switch('Afficher FPS')
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
menu_creationPartie.add.dropselect('Nombre de joueurs', items)
menu_creationPartie.add.button("Créer la partie")

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
menu.add.text_input('Pseudo : ', default='')
menu.add.selector('Couleur des cartes : ', [('Rouge', 1), ('Bleu', 2)], onchange=set_cartes)
menu.add.button('Paramètres', parametres)
menu.add.button('Quitter', pygame_menu.events.EXIT)

menu.mainloop(surface, main_background, fps_limit=FPS)