WEEKAB = ('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
MAANDEN = ('Januari', "Februari", "Maart", "April", "Mei", "Juni", "Juli"
           , "Augustus", "September", "Oktober", "November", "December")
WEEK   = ('Sunday', 'Monday',  'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
 
def __weekDay(day, month, year):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]      
    afterFeb = 1
    if month > 2:
        afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365                  
    # leap year correction    
    dayOfWeek += aux // 4 - aux // 100 + (aux + 100) // 400     
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek = dayOfWeek % 7
    return dayOfWeek, WEEK[dayOfWeek], WEEKAB[dayOfWeek]

def __isSchrikkeljaar(jaar):
    if jaar % 100 == 0:
        return jaar % 400 == 0
    return jaar % 4 == 0

def __dagenInFebruari(jaar):
    if __isSchrikkeljaar(jaar):
        return 29
    return 28

def __dagenInMaand(maand, jaar):
    if maand == 2:
        return __dagenInFebruari(jaar)
    if maand < 8:
        if maand % 2 == 1:
            return 31
        else:
            return 30
    if maand >= 8:
        if maand % 2 == 0:
            return 31
        else:
            return 30

def __volgendeMaand(maand, jaar):
    if maand == 12:
        return 1, jaar + 1
    return maand + 1, jaar

#maak een datum van een dag, maand en jaar
def maakDatum(dag, maand, jaar):
    return dag, maand, jaar

#maak een datum van de 1ste van de maand
def maakMaandDatum(maand, jaar):
    return 1, maand, jaar

#maak een datum van de 1ste van Januari van een jaar
def maakJaarDatum(jaar):
    return 1, 1, jaar
    
#pre : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
def weekDay( datum):
    return __weekDay(datum[0], datum[1], datum[2])

#pre : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
def isSchrikkeljaar( datum ):
    return isSchrikkeljaar(datum[2])

#pre : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
def dagenInMaand( datum ):
    return __dagenInMaand(datum[1], datum[2])

#pre    : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
#return : geeft de eerste dag van de volgende maand terug 
def volgendeMaand( datum ):
    maand, jaar = __volgendeMaand(datum[1], datum[2])
    return 1, maand, jaar

#pre    : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
#return : geeft de laatste dag van de vorige maand terug 
def vorigeMaand( datum ):
    maand = datum[1] - 1
    jaar = datum[2]
    if maand <= 0:
        maand = 12
        jaar -= 1
    return __dagenInMaand(maand, jaar), maand, jaar

#pre    : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
#return : 0 als datums gelijk zijn, -1 als datum1 kleiner is en 1 als datum1 groter is 
def vergelijkDatums( datum1, datum2 ):
    if datum1[2] > datum2[2]:
        return 1
    if datum1[2] < datum2[2]:
        return -1
    #Hetzelfde jaar
    if datum1[1] > datum2[1]:
        return 1
    if datum1[1] < datum2[1]:
        return -1
    #dezelfde maand
    if datum1[0] > datum2[0]:
        return 1
    if datum1[0] < datum2[0]:
        return -1
    return 0

#----------------------------------------------------------------------------------
#pre    : datum is geaakt door maakDatum, maakMaandDatum of maakJaarDatum
#return : nieuwe datum waarbij het aantal dagen (>=0) is toegevoegd bij de
#         opgegeven datum
def dagenToevoegen(datum, dagen):
    # We kijken hoeveel dagen er nog in deze maand zitten
    # Als dagen >= aantal resterende dagen in maand dan naar de 1e van de volgende maand
    # Zolang het kan naar de volgende maand toegaan totdat daar niet genoeg dagen voor zijn.
    # de restdagen er dan bij optellen
    dagenEindeMaand = dagenInMaand(datum) - datum[0]
    if dagen <= dagenEindeMaand:
        return datum[0] + dagen, datum[1], datum[2]
    dagen -= dagenEindeMaand + 1
    return dagenToevoegen(volgendeMaand(datum), dagen)

#pre    : datum is geaakt door maakDatum, maakMaandDatum of maakJaarDatum
#return : nieuwe datum waarbij het aantal dagen (>=0) is afgetrokken bij de
#         opgegeven datum
def dagenAftrekken(datum, dagen):
    # Als huidige dag >= aantal resterende dagen in maand dan naar de 1e van de huidige maand
    # Zolang het kan naar de vorige maand toegaan totdat daar niet genoeg dagen voor zijn.
    # de restdagen er dan van aftrekken
    if dagen < datum[0]:
        return datum[0] - dagen, datum[1], datum[2]
    dagen -= datum[0]
    return dagenAftrekken(vorigeMaand(datum), dagen)

#----------------------------------------------------------------------------------

"""
    Bereken de degan tussen twee datums
"""
def dagen_tussen_data(begin_dag, begin_maand, begin_jaar, eind_dag, eind_maand, eind_jaar):
    if vergelijkDatums((begin_dag, begin_maand, begin_jaar), (eind_dag, eind_maand, eind_jaar)) == 1:
        return dagen_tussen_data(eind_dag, eind_maand, eind_jaar, begin_dag, begin_maand, begin_jaar)
    
    # trek begin_dag eraf, en (einde_maand-eind_dag) eraf   => 3 jan - 5 jan => 31 - ((3) - (31 - 5)) =   
    dagenBeginMaand = __dagenInMaand(begin_maand, begin_jaar) - begin_dag
    dagenEindMaand  = __dagenInMaand(eind_maand, eind_jaar) - eind_dag
    dagen = dagenBeginMaand - dagenEindMaand
    
    # loop van begin_maand + jaar naar eind_maand + jaar
    # bekijk van iedere maand hoeveel dagen erin zitten
    while vergelijkDatums((1, begin_maand, begin_jaar), (1, eind_maand, eind_jaar)) == -1:
           dagen += __dagenInMaand(begin_maand, begin_jaar)
           begin_maand, begin_jaar = __volgendeMaand(begin_maand, begin_jaar)
     
    return dagen

if __name__ == "__main__":
    print("Start tests")
    
    assert dagenToevoegen( ( 1, 12, 2020), 1) == ( 2, 12, 2020)
    assert dagenToevoegen( (31, 12, 2020), 1) == ( 1,  1, 2021)
    assert dagenToevoegen( (28,  2, 2020), 1) == (29,  2, 2020), "Dit is een schrikkeljaar"
    assert dagenToevoegen( (28,  2, 2021), 1) == ( 1,  3, 2021), "Dit is een geen schrikkeljaar"

    assert dagenAftrekken( ( 2, 12, 2020), 1) == ( 1, 12, 2020)
    assert dagenAftrekken( ( 1,  1, 2021), 1) == (31, 12, 2020)
    assert dagenAftrekken( ( 1,  3, 2020), 1) == (29,  2, 2020), "Dit is een schrikkeljaar"
    assert dagenAftrekken( ( 1,  3, 2021), 1) == (28,  2, 2021), "Dit is een geen schrikkeljaar"
    assert dagenAftrekken( ( 1,  3, 2020), 367) == (28,  2, 2019), "Dit is een schrikkeljaar"
    
    assert vergelijkDatums ((2, 1, 2020), (1, 1, 2020) ) == 1
    assert vergelijkDatums ((1, 2, 2020), (1, 1, 2020) ) == 1
    assert vergelijkDatums ((1, 1, 2021), (1, 1, 2020) ) == 1
    
    assert vergelijkDatums ((1, 1, 2020), (2, 1, 2020) ) == -1
    assert vergelijkDatums ((1, 1, 2020), (1, 2, 2020) ) == -1
    assert vergelijkDatums ((1, 1, 2020), (1, 1, 2021) ) == -1
    
    assert vergelijkDatums ((1, 1, 2020), (1, 1, 2020) ) == 0
    
    assert __volgendeMaand(2,2020) == (3, 2020), "March after feb"
    assert __volgendeMaand(12,2020) == (1, 2021), "March after feb"
    assert __isSchrikkeljaar(2019) == False, "Geen schrikkeljaar"
    assert __isSchrikkeljaar(2020) == True, "Wel schrikkeljaar"
    assert __isSchrikkeljaar(2000) == True, "Wel schrikkeljaar"
    assert __isSchrikkeljaar(1900) == False, "Geen schrikkeljaar"
    assert dagen_tussen_data( 2, 4,2020, 2, 4, 2020) ==  0, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 3, 4, 2020) ==  1, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 4, 4, 2020) ==  2, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 8, 4, 2020) ==  6, "6 dagen tussen deze data"
    assert dagen_tussen_data(30,12,2020, 2, 1, 2021) ==  3, "36 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 8, 5, 2020) == 35, "6 dagen tussen deze data"
    assert __weekDay(24,3,2020)[0] == 2, "This is a Tuesday (after fix / to //)"
    
    print("All tests OK")    