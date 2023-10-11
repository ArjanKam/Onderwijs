class Persoon:
    __naam = ""
    __lengte = None
    def __init__(self, naam, lengte = None):
        self.__naam = naam
        self.__lengte = lengte
    def getName(self):
        return self.__naam
    def setName(self, naam):
        self.__naam = naam
    def getLength(self):
        return self.__lengte
    def getAanspreekNaam(self):
        return self.__naam
    
class Vrouw(Persoon):
    def getAanspreekNaam(self):
        return "Mevrouw " +  super().getAanspreekNaam()

class Man(Persoon):
    def getAanspreekNaam(self):
        return "Meneer " +  super().getAanspreekNaam()
q = Persoon("Frits", 183)
x = Vrouw("Els", 177)
y = Man("Arjan", 183)
print(x.getAanspreekNaam(), y.getAanspreekNaam(), q.getAanspreekNaam(), sep=", " )

#print( dir( Persoon ) )