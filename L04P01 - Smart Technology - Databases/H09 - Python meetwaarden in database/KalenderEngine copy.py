WEEKAB = ('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
MAANDEN = ('Januari', "Februari", "Maart", "April", "Mei", "Juni", "Juli"
           , "Augustus", "September", "Oktober", "November", "December")
WEEK   = ('Sunday', 'Monday',  'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
 
def weekDay(day, month, year):
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

def isSchrikkeljaar(jaar):
    if jaar % 100 == 0:
        return jaar % 400 == 0
    return jaar % 4 == 0

def dagenInFebruari(jaar):
    if isSchrikkeljaar(jaar):
        return 29
    return 28

def dagenInMaand(maand, jaar):
    if maand == 2:
        return dagenInFebruari(jaar)
    if maand < 8:
        if maand % 2 == 1:
            return 31
        return 30
    if maand % 2 == 0:
        return 31
    return 30

#return : 0 als datums gelijk zijn, -1 als datum1 kleiner is en 1 als datum1 groter is 
def vergelijkDatums( dag, maand, jaar, dag2, maand2, jaar2 ):
    if jaar > jaar2:
        return 1
    if jaar < jaar2:
        return -1
    #Hetzelfde jaar
    if maand > maand2:
        return 1
    if maand < maand2:
        return -1
    #dezelfde maand
    if dag > dag2:
        return 1
    if dag < dag2:
        return -1
    return 0

def volgendeMaand(maand, jaar):
    if maand == 12:
        return 1, jaar + 1
    return maand + 1, jaar

#pre    : datum is gemaakt door maakDatum, maakMaandDatum of maakJaarDatum
#return : geeft de laatste dag van de vorige maand terug 
def vorigeMaand( maand, jaar ):
    maand = maand - 1
    if maand <= 0:
        maand = 12
        jaar -= 1
    return maand, jaar

#----------------------------------------------------------------------------------
#pre    : datum is geaakt door maakDatum, maakMaandDatum of maakJaarDatum
#return : nieuwe datum waarbij het aantal dagen (>=0) is toegevoegd bij de
#         opgegeven datum
def dagenToevoegen(dag, maand, jaar, dagen):
    # We kijken hoeveel dagen er nog in deze maand zitten
    # Als dagen >= aantal resterende dagen in maand dan naar de 1e van de volgende maand
    # Zolang het kan naar de volgende maand toegaan totdat daar niet genoeg dagen voor zijn.
    # de restdagen er dan bij optellen
    dagenEindeMaand = dagenInMaand(maand, jaar) - dag
    if dagen <= dagenEindeMaand:
        return dag + dagen, maand, jaar
    dagen -= dagenEindeMaand + 1
    maand, jaar = volgendeMaand(maand, jaar)
    return dagenToevoegen(1, maand, jaar, dagen)

#pre    : datum is geaakt door maakDatum, maakMaandDatum of maakJaarDatum
#return : nieuwe datum waarbij het aantal dagen (>=0) is afgetrokken bij de
#         opgegeven datum
def dagenAftrekken(dag, maand, jaar, dagen):
    # Als huidige dag >= aantal resterende dagen in maand dan naar de 1e van de huidige maand
    # Zolang het kan naar de vorige maand toegaan totdat daar niet genoeg dagen voor zijn.
    # de restdagen er dan van aftrekken
    if dagen < dag:
        return dag - dagen, maand, jaar
    dagen -= dag
    maand, jaar = vorigeMaand(maand, jaar)
    aantalDagen = dagenInMaand(maand, jaar)
    return dagenAftrekken(aantalDagen, maand, jaar, dagen)

#----------------------------------------------------------------------------------
    
"""
    Bereken de degan tussen twee datums
"""
def dagen_tussen_data(begin_dag, begin_maand, begin_jaar, eind_dag, eind_maand, eind_jaar):
    if vergelijkDatums(begin_dag, begin_maand, begin_jaar, eind_dag, eind_maand, eind_jaar) == 1:
        return dagen_tussen_data(eind_dag, eind_maand, eind_jaar, begin_dag, begin_maand, begin_jaar)
    
    # trek begin_dag eraf, en (einde_maand-eind_dag) eraf   => 3 jan - 5 jan => 31 - ((3) - (31 - 5)) =   
    dagenBeginMaand = dagenInMaand(begin_maand, begin_jaar) - begin_dag
    dagenEindMaand  = dagenInMaand(eind_maand, eind_jaar) - eind_dag
    dagen = dagenBeginMaand - dagenEindMaand
    
    # loop van begin_maand + jaar naar eind_maand + jaar
    # bekijk van iedere maand hoeveel dagen erin zitten
    while vergelijkDatums(1, begin_maand, begin_jaar, 1, eind_maand, eind_jaar) < 0:
           dagen += dagenInMaand(begin_maand, begin_jaar)
           begin_maand, begin_jaar = volgendeMaand(begin_maand, begin_jaar)
     
    return dagen

if __name__ == "__main__":
    print("Start tests")
    assert volgendeMaand(2,2020) == (3, 2020), "March after feb"
    assert volgendeMaand(12,2020) == (1, 2021), "March after feb"
    assert isSchrikkeljaar(2019) == False, "Geen schrikkeljaar"
    assert isSchrikkeljaar(2020) == True, "Wel schrikkeljaar"
    assert isSchrikkeljaar(2000) == True, "Wel schrikkeljaar"
    assert isSchrikkeljaar(1900) == False, "Geen schrikkeljaar"
    assert dagen_tussen_data( 2, 4,2020, 2, 4, 2020) ==  0, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 3, 4, 2020) ==  1, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 4, 4, 2020) ==  2, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 8, 4, 2020) ==  6, "6 dagen tussen deze data"
    assert dagen_tussen_data(30,12,2020, 2, 1, 2021) ==  3, "36 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 8, 5, 2020) == 35, "6 dagen tussen deze data"
    assert weekDay(24,3,2020)[0] == 2, "This is a Tuesday (after fix / to //)"
    
    
    assert volgendeMaand(2,2020) == (3, 2020), "March after feb"
    assert volgendeMaand(12,2020) == (1, 2021), "March after feb"
    assert isSchrikkeljaar(2019) == False, "Geen schrikkeljaar"
    assert isSchrikkeljaar(2020) == True, "Wel schrikkeljaar"
    assert isSchrikkeljaar(2000) == True, "Wel schrikkeljaar"
    assert isSchrikkeljaar(1900) == False, "Geen schrikkeljaar"
    assert dagen_tussen_data( 2, 4,2020, 2, 4, 2020) ==  0, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 3, 4, 2020) ==  1, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 4, 4, 2020) ==  2, "6 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 8, 4, 2020) ==  6, "6 dagen tussen deze data"
    assert dagen_tussen_data(30,12,2020, 2, 1, 2021) ==  3, "36 dagen tussen deze data"
    assert dagen_tussen_data( 2, 4,2020, 8, 5, 2020) == 35, "6 dagen tussen deze data"
    assert weekDay(24,3,2020)[0] == 2, "This is a Tuesday (after fix / to //)"
    
    assert dagenToevoegen( 31, 12, 2020, 1) == ( 1,  1, 2021)
    assert dagenToevoegen( 28,  2, 2020, 1) == (29,  2, 2020), "Dit is een schrikkeljaar"
    assert dagenToevoegen( 28,  2, 2021, 1) == ( 1,  3, 2021), "Dit is een geen schrikkeljaar"

    assert dagenAftrekken(  2, 12, 2020, 1) == ( 1, 12, 2020)
    assert dagenAftrekken(  1,  1, 2021, 1) == (31, 12, 2020)
    assert dagenAftrekken(  1,  3, 2020, 1) == (29,  2, 2020), "Dit is een schrikkeljaar"
    assert dagenAftrekken(  1,  3, 2021, 1) == (28,  2, 2021), "Dit is een geen schrikkeljaar"
    assert dagenAftrekken(  1,  3, 2020, 367) == (28,  2, 2019), "Dit is een schrikkeljaar"
    
    assert vergelijkDatums(2, 1, 2020, 1, 1, 2020 ) == 1
    assert vergelijkDatums(1, 2, 2020, 1, 1, 2020 ) == 1
    assert vergelijkDatums(1, 1, 2021, 1, 1, 2020 ) == 1
    
    assert vergelijkDatums(1, 1, 2020, 2, 1, 2020 ) == -1
    assert vergelijkDatums(1, 1, 2020, 1, 2, 2020 ) == -1
    assert vergelijkDatums(1, 1, 2020, 1, 1, 2021 ) == -1
    
    assert vergelijkDatums(1, 1, 2020, 1, 1, 2020 ) == 0
    print("All tests OK")