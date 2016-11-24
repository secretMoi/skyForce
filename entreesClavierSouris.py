from variables import *
import pygame
from pygame.locals import *
from classVaisseauMoi import VaisseauMoi
from classVariable import Variable

def gestion_entrees(evenement, vaisseauMoi):
	if evenement.type        == pygame.QUIT:
		Variable.fini = True

	if evenement.type == MOUSEMOTION:
		vaisseauMoi.deplacementSouris(evenement.pos[0], evenement.pos[1])

	elif evenement.type      == pygame.KEYDOWN:
		if evenement.key   == K_ESCAPE:
			Variable.fini = True

		elif evenement.key     == TOUCHE_DROITE:
			vaisseauMoi.deplacementClavier(Sens.VERS_DROITE)

		elif evenement.key   == TOUCHE_GAUCHE:
			vaisseauMoi.deplacementClavier(Sens.VERS_GAUCHE)

		elif evenement.key   == TOUCHE_HAUT:
			vaisseauMoi.deplacementClavier(Sens.VERS_HAUT)

		elif evenement.key   == TOUCHE_BAS:
			vaisseauMoi.deplacementClavier(Sens.VERS_BAS)
 #[<Event(3-KeyUp {'scancode': 75, 'key': 276, 'mod': 4096})>]