import KalenderEngine

class Datum:
    __datum = None
    __dayOfWeek = None
    
    def __init__(self, dag, maand, jaar):
        self.setDatum(dag, maand, jaar)
    
     #maak een datum van een dag, maand en jaar
    def setDatum(self, dag, maand, jaar):
        if maand < 1 or maand > 12:
            raise ValueError('ongeldige maand')
        if dag < 1:
            raise ValueError('ongeldige dag')
        if dag > KalenderEngine.dagenInMaand( maand, jaar ):
            raise ValueError('ongeldige dag')
        self.__datum = (dag, maand, jaar)
        self.__dayOfWeek = KalenderEngine.weekDay(dag, maand, jaar)
        
    def getDatum(self):
        return self.__datum
    
    def getDayOfWeek(self):
        return self.__dayOfWeek[0]
    
    def getNameOfDay(self):
        return self.__dayOfWeek[1]
    
    def getShortNameOfDay(self):
        return self.__dayOfWeek[2]
    
    #return : 0 als beide gelijk zijn, -1 als self kleiner is en 1 als self groter is 
    def compare( self, other ):
        if self.__datum[2] > other.__datum[2]:
            return 1
        if self.__datum[2] < other.__datum[2]:
            return -1
        #Hetzelfde jaar
        if self.__datum[1] > other.__datum[1]:
            return 1
        if self.__datum[1] < other.__datum[1]:
            return -1
        #dezelfde maand
        if self.__datum[0] > other.__datum[0]:
            return 1
        if self.__datum[0] < other.__datum[0]:
            return -1
        return 0
    
    def __ge__(self, other): #greater or equal
        return self.compare(other) >= 0
    def __le__(self, other): # less or equal
        return self.compare(other) <= 0
    def __lt__(self, other): # less
        return self.compare(other) < 0
    def __gt__(self, other): # greater
        return self.compare(other) > 0
    def __eq__(self, other): # equal
        return self.__datum == other.__datum