from variables import *
from fonctions import dessine_rectangle
from classVaisseau import Vaisseau
from classVaisseauMoi import VaisseauMoi

class Missile():
	def __init__(self, fenetre):
		self._fenetre = fenetre
		self._tire = 0
		self._position = [0,0]
		
	def collisionMissile(self, positionMissileX, positionMissileY):
		global listeVaisseauxEnnemis
		global spawnEnnemiPosition
		global score

		for i in range(0, len(listeVaisseauxEnnemis)):
			if listeVaisseauxEnnemis[i].etat == True:
				if positionMissileX + TIR_LARGEUR >= listeVaisseauxEnnemis[i].positionX and positionMissileX <= listeVaisseauxEnnemis[i].positionX + ENNEMI_TAILLE:
					if positionMissileY >= listeVaisseauxEnnemis[i].positionY and positionMissileY <= listeVaisseauxEnnemis[i].positionY + ENNEMI_TAILLE:
						listeVaisseauxEnnemis[i].changeEtat()
						ennemi_position = [listeVaisseauxEnnemis[i].positionX, listeVaisseauxEnnemis[i].positionY]
						spawnEnnemiPosition = [listeVaisseauxEnnemis[i].positionX, 0]

						dessine_rectangle(self._fenetre, ARRIERE_PLAN, ennemi_position, ENNEMI_TAILLE)

						return True


	def afficheMissile(self, couleur):
		dessine_rectangle(self._fenetre, couleur, self._position, TIR_LARGEUR, TIR_LONGUEUR)


	def _getPosition(self):
		return self._position

	def _setPosition(self, position):
		self._position = position

	position = property(_getPosition, _setPosition)