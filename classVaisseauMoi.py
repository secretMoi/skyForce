from variables import *
from fonctions import dessine_rectangle
from classVaisseau import Vaisseau
import pygame

class VaisseauMoi(Vaisseau):

	def __init__(self, fenetre):
		self._fenetre = fenetre
		self._positionX = FENETRE_LARGEUR//2 - MOI_LARGEUR//2
		self._positionY = FENETRE_HAUTEUR - 10 - MOI_HAUTEUR

	def afficheVaisseau(self, couleur):
		dessine_rectangle(self._fenetre, couleur, [self._positionX, self._positionY], MOI_LARGEUR, MOI_HAUTEUR)

	def deplacementClavier(self, sens):
		if sens == Sens.VERS_DROITE: #Déplacement droite
			if self._positionX >= (FENETRE_LARGEUR - MOI_LARGEUR // 2):
				self._positionX = FENETRE_LARGEUR - MOI_LARGEUR // 2
			else:
				self._positionX += 40

		if sens == Sens.VERS_GAUCHE: #Déplacement gauche
			if self._positionX <= -(MOI_LARGEUR // 2):
				self._positionX = -(MOI_LARGEUR // 2)
			else:
				self._positionX -= 40

		if sens == Sens.VERS_BAS:    #Déplacement bas
			if self._positionY >= (FENETRE_HAUTEUR - MOI_HAUTEUR // 2):
				self._positionY = FENETRE_HAUTEUR - MOI_HAUTEUR // 2
			else:
				self._positionY += 40

		if sens == Sens.VERS_HAUT:   #Déplacement haut
			if self._positionY <= -(MOI_HAUTEUR // 2):
				self._positionY = -(MOI_HAUTEUR // 2)
			else:
				self._positionY -= 40

	def deplacementSouris(self, sourisX, sourisY):
		self._positionX = sourisX - 55
		self._positionY = sourisY - 90


	def _getPositionX(self):
		return self._positionX

	def _setPositionX(self, position):
		self._positionX = position


	def _getPositionY(self):
		return self._positionY

	def _setPositionY(self, position):
		self._positionY = position



	positionX = property(_getPositionX, _setPositionX)
	positionY = property(_getPositionY, _setPositionY)
