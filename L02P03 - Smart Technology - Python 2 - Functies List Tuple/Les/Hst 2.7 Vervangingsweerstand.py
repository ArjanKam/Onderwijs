def berekenSerie(weerstandenLijst):
    rVervanging = 0
    for r in weerstandenLijst:
        rVervanging += r
    return rVervanging

def berekenParallel2(r1, r2):
    if r1 == 0 and r2 == 0:
        return 0
    return (r1 * r2) / (r1 + r2)

def berekenParallel(weerstandenLijst):
    if len(weerstandenLijst) == 0:
        return 0
    rVervanging = weerstandenLijst[0]
    for r in weerstandenLijst[1:]: # [:1] betekend dat we bij element 1 beginnen ipv 0
        rVervanging = berekenParallel2(rVervanging, r)
    return rVervanging

WEERSTANDEN = ( 300
              ,(300, 300, 300)
              ,(300, 300, 300, 300)
              ,(300, 300, 300)
              ,(300, 300)
              , 300
              )
def opschonen(weerstanden):
    newList = []
    for r in weerstanden:
        if type(r) is tuple:
            r = berekenParallel(r)
        newList.append(r)
    return newList

serieLijst = opschonen(WEERSTANDEN)
vervangingsweerstand = berekenSerie(serieLijst)
uBatterij = 9
stroom = uBatterij / vervangingsweerstand
spanning_meter = stroom * berekenParallel((300, 300, 300, 300))
print(spanning_meter)

