WEERSTAND_U = ( 300, 300, 300, 300 )
WEERSTANDEN = ( 300
              , (300, 300, 300)
              , WEERSTAND_U
              , (300, 300, 300)
              , (300, 300)
              , 300
              )
U_BATTERIJ = 9

#weerstanden can be float, int, tuple of list
def berekenSerie(weerstanden):
    t = type(weerstanden)
    if t in (int, float):
        return weerstanden
    if t in (tuple, list):
        rVervanging = 0
        for r in weerstanden:
            if type(r) is tuple:
                rVervanging += berekenParallel(r)
            else:
                rVervanging += r
        return rVervanging
    return 0

def berekenParallel2(r1, r2):
    if r1 == 0 and r2 == 0:
        return 0
    return (r1 * r2) / (r1 + r2)

def berekenParallel(weerstandenLijst):
    if len(weerstandenLijst) == 0:
        return 0
    
    rVervanging = berekenSerie(weerstandenLijst[0])   
    for r in weerstandenLijst[1:]: # [:1] betekend dat we bij element 1 beginnen ipv 0
        rVervanging = berekenParallel2(rVervanging, berekenSerie(r))
    return rVervanging

def berekenSpanning(uBatterij, allWeerstanden, weerstand):
    vervangingsweerstand = berekenSerie(allWeerstanden)
    if vervangingsweerstand != 0:
        stroom = uBatterij / vervangingsweerstand
    else:
        stroom = 0
    spanning_meter = stroom * berekenParallel(weerstand)
    return spanning_meter

print(berekenSpanning(U_BATTERIJ, WEERSTANDEN, WEERSTAND_U))

