U = 9
R = 10000

def berekenSerieWeerstand(weerstanden):
    rv = 0
    for r in weerstanden:
        rv  = rv + r
    return rv

def berekenParallelWeerstand(weerstanden):
    rv = 0
    for r in weerstanden:
        rv  = rv + 1/r
    return 1/rv

def invoerIntegers(invoertekst):
    lijstje = []
    while True:
        invoer = input(invoertekst)
        if invoer == "":
            break
        lijstje.append(int(invoer))
    return lijstje

weerstanden = invoerIntegers("Geef de weerstand : ")
rp = berekenParallelWeerstand(weerstanden)
print(rp)
