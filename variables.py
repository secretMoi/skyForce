import pygame
import time
from os import path as os_path

PATH = os_path.abspath(os_path.split(__file__)[0])
PATH = PATH.replace('\\', '/')

pygame.init() #Initailise pygame

"""  Déclaration Variables """
#Création des constantes pour les touches
TOUCHE_DROITE        = pygame.K_RIGHT
TOUCHE_GAUCHE        = pygame.K_LEFT
TOUCHE_HAUT          = pygame.K_UP
TOUCHE_BAS           = pygame.K_DOWN
TOUCHE_QUITTER       = pygame.K_ESCAPE

#Création des sens des vaisseaux selon la "rose"
class Sens:
	(
		RIEN,
		VERS_HAUT,
		VERS_DROITE,
		VERS_BAS,
		VERS_GAUCHE
	) = range(5)

#Définition des couleurs du jeu
ARRIERE_PLAN         = (0, 0, 0)
MOI_COULEUR          = (135, 206, 250)
ENNEMI_COULEUR       = (250, 0, 0)

#Définition de la fenêtre
FENETRE_HAUTEUR      = 720
FENETRE_LARGEUR      = 1260
fenetre_taille       = (FENETRE_LARGEUR, FENETRE_HAUTEUR)

#Définition moi
CARRE_COTE           = 50
MOI_LARGEUR          = 110 #
MOI_HAUTEUR          = 155 #
vaisseauMoi          = 0
axeX                 = 0
axeY                 = 1
vaisseauMoi          = 0


#Définition missile
TIR_LARGEUR          = 40 #Modif
TIR_LONGUEUR         = 110 #Modif


#Vagues ennemies
tempsPrecedent       = 0
spawnEnnemiPosition  = [FENETRE_LARGEUR // 10, 0]
ennemi_position      = 0
tempsActuel          = 0
vaisseauID           = 0
listeVaisseauxEnnemis= {}
ENNEMI_TAILLE         = 50

temps = pygame.time.Clock() #Lance l'horloge fps

#Variables pour le score
police = pygame.font.SysFont('monospace', FENETRE_HAUTEUR//12, True)

fenetre = pygame.display.set_mode(fenetre_taille) #Crée la fenêtre
fenetre.fill(ARRIERE_PLAN)
pygame.display.set_caption('SkyForce')

#----- Création images -----#
chemin = PATH + '/images/fauconMillenium.png'
fauconMillenium = pygame.image.load(chemin).convert_alpha(fenetre) # Création image vaisseau
fauconMillenium = pygame.transform.scale(fauconMillenium, (MOI_LARGEUR, MOI_HAUTEUR)) # Redimension vaisseau

chemin = PATH + '/images/laserShot.png'
tirLaser = pygame.image.load(chemin).convert_alpha(fenetre) # Création image laser
tirLaser = pygame.transform.scale(tirLaser, (TIR_LARGEUR, TIR_LONGUEUR)) # Redimension laser
