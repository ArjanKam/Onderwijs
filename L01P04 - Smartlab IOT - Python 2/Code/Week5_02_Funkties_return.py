def serieWeerstand(weerstanden):
    rVervanging = 0
    for item in weerstanden:
        rVervanging = rVervanging + item
    return rVervanging

def parallelWeerstand(weerstand):
    rVervanging = 0
    for item in weerstanden:
        rVervanging = rVervanging + 1/item
    return 1/rVervanging

myList = []
while True:
    rNew = input("Geef de waarde : ")
    if rNew == "" or rNew == "0":
        break
    myList.append(float(rNew))

print( serieWeerstand(myList) )
print( parallelWeerstand(myList) )

