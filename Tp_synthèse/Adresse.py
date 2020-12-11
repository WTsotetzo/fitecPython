class Adresse:
	def __init__(self,rue,code_postal,ville):
		assert len(rue) > 3 and len(rue) < 25, "la rue doit contenir entre 3 et 25 caractères"
		self.rue = rue
		self.codePostal = codePostal
		self.ville = ville
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}".format(self.rue,self.code_postal,self.ville)
	@property
	def rue(self):
		return self._rue

	@nom.setter
	def rueAd(self,r):
		self._rue = r
		
	@property
	def codePostal(self):
		return self._codePostal

	@nom.setter
	def codeP(self,p):
		self._codePostal = p

	@property
	def ville(self):
		return self._ville

	@nom.setter
	def villeAd(self,v):
		self._ville = v
