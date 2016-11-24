import pygame
from variables import *

def dessine_rectangle(fenetre, couleur, position, largeur, longueur=0):
	if longueur == 0:
		longueur = largeur
	pygame.draw.rect(fenetre, couleur, (position, (largeur, longueur)))

def definitionTemps():
	return int(round(time.time()))