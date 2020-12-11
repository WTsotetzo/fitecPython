import Adresse
class Personne:
	#constructeur
	def __init__(self,nom,prenom,adresse):
		self.nom = nom
		self.prenom = prenom
		self.adresses = []
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self.nom,self.prenom,self.adresse)
	@property
	def nom(self):
		return self._nom

	@nom.setter
	def nomPerso(self,n):
		self._nom = n
	@property
	def prenom(self):
		return self._prenom

	@nomBat.setter
	def prenomPerso(self,p):
		self._prenom = p

	def getAdresse():
            return self._adresses
            
	
