def serieWeerstand(weerstanden):
    rVervanging = 0
    for item in weerstanden:
        rVervanging = rVervanging + item
    print("Serieweerstand = ", rVervanging)

def parallelWeerstand(weerstand):
    rVervanging = 0
    for item in weerstanden:
        rVervanging = rVervanging + 1/item
    print("Parallel weerstand =", 1/rVervanging)

myList = []
while True:
    rNew = input("Geef de waarde : ")
    if rNew == "" or rNew == "0":
        break
    myList.append(float(rNew))

serieWeerstand(myList)
parallelWeerstand(myList)