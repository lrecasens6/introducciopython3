#1- Fes un programa que dibuixi aquesta finestra:
import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0)
BLANC = (255,255,255)
VERD = (0,255,0)
BLAU = (0,0,255)
pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Formes')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)

    rectangle1 = pygame.draw.rect(pantalla, NEGRE, (50,150,500,250),1)
    rectangle2 = pygame.draw.rect(pantalla, BLANC, (75,175,450,200), 1)
    rectangle3 = pygame.draw.rect(pantalla, BLAU, (100,200,400,150), 1)
    rectangle4 = pygame.draw.rect(pantalla, VERD, (125,225,350,100), 1)
    rectangle5 = pygame.draw.rect(pantalla, VERMELL, (150,250,300,50), 1)
    pygame.draw.rect(pantalla, NEGRE, rectangle1)
    pygame.draw.rect(pantalla, BLANC, rectangle2)
    pygame.draw.rect(pantalla, BLAU, rectangle3)
    pygame.draw.rect(pantalla, VERD, rectangle4)
    pygame.draw.rect(pantalla, VERMELL, rectangle5)
    pygame.display.update()
