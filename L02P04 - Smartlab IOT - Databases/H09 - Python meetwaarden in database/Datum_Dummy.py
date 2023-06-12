class Datum:
    __datum = None
    __weekDay = None
    
    def __init__(self, dag, maand, jaar):
        self.maakDatum(dag, maand, jaar)

     #maak een datum van een dag, maand en jaar
    def maakDatum(self, dag, maand, jaar):
        if maand < 1 or maand > 12:
            raise ValueError('ongeldige maand')
        if dag < 1:
            raise ValueError('ongeldige dag')
        if dag > self.__dagenInMaand( maand, jaar ):
            raise ValueError('ongeldige dag')
        self.__datum = (dag, maand, jaar)
        __weekDay = self.__weekDay(dag, maand, jaar)
        
    #maak een datum van de 1ste van de maand
    def maakMaandDatum(self, maand, jaar):
        self.maakDatum(1, maand, jaar)

    #maak een datum van de 1ste van Januari van een jaar
    def maakJaarDatum(self, jaar):
        self.maakDatum(1, 1, jaar)

    #geef de module datum terug als tuple (dag, maand, jaar) 
    def geefDatum(self):
        return self.__datum
    
    def geefMaand(self):
        return self.__MAANDEN(self.__datum[2] - 1)
    
    def geefDag(self):
        return self.__WEEK[self.__weekDay]
    
    def geefDagAb(self):
        return self.__WEEKAB[self.__weekDay]
    
     #pre : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
    def weekDay( self):
        return self.__weekDay

    #pre : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
    def isSchrikkeljaar( self):
        return isSchrikkeljaar(self.__datum[2])

    #pre : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
    def dagenInMaand( self ):
        return dagenInMaand(self.__datum[1], self.__datum[2])
