import pygame
from pygame import *
#Pygame
###Fennetre
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Poker Online')

# Background / Icon
background_image = pygame.image.load("img/Table.png").convert()
icon = pygame.image.load("img/Logo.png").convert()
pygame.display.set_icon(icon)

#Variables
font = pygame.font.Font(None, 36)
text = font.render("Hello There", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background_image.get_rect().centerx
background_image.blit(text, textpos)
screen.blit(background_image, (0, 0))
pygame.display.flip()

# Events
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    screen.blit(background_image, [0, 0])
    pygame.display.flip()
