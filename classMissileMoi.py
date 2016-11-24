from variables import *
from fonctions import dessine_rectangle
from classVaisseau import Vaisseau
from classVaisseauMoi import VaisseauMoi
from classMissile import Missile
from classVariable import Variable

class MissileMoi(Missile):
	def __init__(self, fenetre):
		self._fenetre = fenetre
		self._tire = 0
		self._position = [0,0]


	def tir(self, vaisseauMoi):
		global score

		if(super(MissileMoi, self).collisionMissile(self._position[axeX], self._position[axeY])):
			self._tire = 0
			Variable.score += 10

		if self._position[axeY] <= 0: #SI le missile atteint le haut de l'écran
			self._tire = 0

		if self._tire == 0:       #Initialiser le missile
			self._position[axeX] = vaisseauMoi.positionX + (MOI_LARGEUR - TIR_LARGEUR) // 2 #
			self._position[axeY] = vaisseauMoi.positionY - TIR_LONGUEUR + 50
			self._tire += 1

		else:                       #Déplacer le missile
			self._position[axeY] -= 4


