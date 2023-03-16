def berekenKirchhoff(stromen):
    resultaat = 0
    for i in stromen:
        resultaat = resultaat - i
    return resultaat

def invoerIntegers(invoertekst):
    lijstje = []
    while True:
        invoer = input(invoertekst)
        if invoer == "":
            break
        lijstje.append(int(invoer))
    return stromen

stromen = invoerIntegers("Geef een stroom : ")
i = berekenKirchhoff(stromen)
print("resultaat", i)