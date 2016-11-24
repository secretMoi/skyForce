import pygame
from pygame.locals import *
import time
import random

from variables import *

from fonctions import *
from entreesClavierSouris import gestion_entrees

from classVaisseau import Vaisseau
from classVaisseauMoi import VaisseauMoi
from classMissile import Missile
from classMissileMoi import MissileMoi
from classVariable import Variable


pygame.key.set_repeat(200, 25) #Ecoute les touches claviers

vaisseauMoi = VaisseauMoi(fenetre)
missileMoi = MissileMoi(fenetre)

def genere_vaisseau_ennemi():
	global tempsPrecedent
	global vaisseauID
	global listeVaisseauxEnnemis
	global tempsActuel

	tempsActuel = definitionTemps()

	if tempsActuel - tempsPrecedent >= 1:
		listeVaisseauxEnnemis[vaisseauID] = Vaisseau(fenetre)

		listeVaisseauxEnnemis[vaisseauID].genereVaisseau(vaisseauID, spawnEnnemiPosition[axeX])
		spawnEnnemiPosition[axeX] =  random.randrange(100, 1150)

		tempsPrecedent = tempsActuel
		vaisseauID += 1


def traite_entrees():
	for evenement in pygame.event.get():
		gestion_entrees(evenement, vaisseauMoi)



def dessine():
	global listeVaisseauxEnnemis
	global vaisseauMoi

	genere_vaisseau_ennemi()

	for i in range(0, len(listeVaisseauxEnnemis)):
		listeVaisseauxEnnemis[i].afficheVaisseau(ENNEMI_COULEUR)

	fenetre.blit(fauconMillenium, (vaisseauMoi.positionX, vaisseauMoi.positionY))
	fenetre.blit(tirLaser, missileMoi.position)


	#Affiche le score
	marquoir = police.render(str(Variable.score), True, MOI_COULEUR)
	fenetre.blit(marquoir, (5  * FENETRE_LARGEUR // 8, FENETRE_HAUTEUR // 10))

	#Affiche le résultat et temporise
	pygame.display.flip()
	temps.tick(300)

	#Efface le score
	marquoir = police.render(str(Variable.score), True, ARRIERE_PLAN)
	fenetre.blit(marquoir, (5  * FENETRE_LARGEUR // 8, FENETRE_HAUTEUR // 10))

	vaisseauMoi.afficheVaisseau(ARRIERE_PLAN)
	missileMoi.afficheMissile(ARRIERE_PLAN)


	for i in range(0, len(listeVaisseauxEnnemis)):
		listeVaisseauxEnnemis[i].afficheVaisseau(ARRIERE_PLAN)
		listeVaisseauxEnnemis[i].deplaceVaisseau(0.5)


"""  Corps programme """
while not Variable.fini:

	traite_entrees()

	missileMoi.tir(vaisseauMoi)

	dessine()

#Quitte le programme

pygame.display.quit()
pygame.quit()
