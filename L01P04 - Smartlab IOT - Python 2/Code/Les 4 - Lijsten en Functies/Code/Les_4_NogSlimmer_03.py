def berekenSerie( weerstanden ):
    totaalWeerstand = 0
    for x in weerstanden:
        totaalWeerstand = totaalWeerstand + x
    return totaalWeerstand

r = berekenSerie( [30, 20, 20, 100, 7, 875, 57, 878] )
print(r)



