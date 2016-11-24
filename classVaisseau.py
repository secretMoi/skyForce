from variables import *
from fonctions import dessine_rectangle
from fonctions import definitionTemps

class Vaisseau:

	def __init__(self, fenetre):
		self._id = []
		self._id.append(1)
		self._fenetre = fenetre
		self._taille = CARRE_COTE
		self._positionX = 0
		self._positionY = 0
		self._etat = True

	def genereVaisseau(self, id, positionX = 0, positionY = 0):
		self._positionX = positionX
		self._positionY = positionY
		position = [positionX, positionY]

	def afficheVaisseau(self, couleur):
		if self._etat == True:
			dessine_rectangle(self._fenetre, couleur, [self._positionX, self._positionY], self._taille)

	def deplaceVaisseau(self, nbCases):
		self._positionY += nbCases

	def changeEtat(self):
		self._etat = not self._etat



	def _getPositionX(self):
		return self._positionX

	def _setPositionX(self, position):
		self._positionX = position


	def _getPositionY(self):
		return self._positionY

	def _setPositionY(self, position):
		self._positionY = position


	def _getEtat(self):
		return self._etat

	def _setEtat(self, etat):
		self._etat = etat

	positionX = property(_getPositionX, _setPositionX)
	positionY = property(_getPositionY, _setPositionY)
	etat = property(_getEtat, _setEtat)