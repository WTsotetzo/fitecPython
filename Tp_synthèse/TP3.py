class Alphabet():
    def _init_(self,mot):
        self._mot=mot

    def info(self):
        print("Je suis une lettre de l'alphabet")
        
    def test1(self):
        print("Fonc test1 de la classe Alphabet")

    def test2(self):
        print("Fonc test2 de la classe Alphabet")


class Mot():
    def _init_(self):
        pass
    
    def info(self):
        print("Je suis un mot")
        
    def test1(self):
        print("Fonc test1 de la classe Mot")

    def test3(self):
        print("Fonc test 3 de la classe Mot")

class A(Alphabet):
    def _init_(self):
        Alphabet.__init__(self,mot)
        self.mot=mot
        
    def info(self):
        print("Je suis une lettre")
        
    def test1(self):
        print("Fonc test1 de la classe A")
        
class Accent:
    def _init_(self):
        pass

    def info(self):
        print("Je suis un accent")
        
    def test3(self):
        print("Fonc test3 de la classe Accent")

    def test2(self):
        print("Fonc test2 de la classe Accent")
        
class Abracadabra(Mot):
    def _init_(self):
        Mot.__init__(self)
    
    def test1(self):
        print("Fonc test1 de la classe Alphabet")

class AGrave(A,Accent,Abracadabra):
    def _init_(self):
        A.__init__(self)
        Accent.__init__(self)
        Abracadabra.__init__(self)

    def test4(self):
        print("Fonc test4 de la classe AGRAVE")

aAccentGrave = AGrave("à")
aAccentGrave.nom
aAccentGrave.test1()
aAccentGrave.test2()
aAccentGrave.test3()
aAccentGrave.test4()
