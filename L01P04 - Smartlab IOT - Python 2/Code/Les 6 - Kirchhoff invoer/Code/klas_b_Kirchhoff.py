def berekenKirchhoff( stromen ):
    resultaat = 0
    for i in stromen:
        resultaat = resultaat - i
    return resultaat

def maakLijstFloat():
    stromen = []
    while True:
        i = input("Geef de stroom : ")
        if i != "":
            stromen.append(float(i))
        else:
            break
    return stromen

stromen = maakLijstFloat()
missendeStroom = berekenKirchhoff(stromen)
print("De missende stroom is :", missendeStroom )




