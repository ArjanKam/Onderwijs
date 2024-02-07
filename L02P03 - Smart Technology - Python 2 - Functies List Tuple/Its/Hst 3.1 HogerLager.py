"""
    datum : 23-02-2023
    Arjan Kamberg
"""
import random
MIN_GETAL = 1
MAX_GETAL = 20
MAX_AANTAL_POGINGEN = 5
poging = 0
name = input("Wat is je naam : ")
randomGetal = random.randrange(MIN_GETAL, MAX_GETAL + 1)
print(randomGetal)

while poging < MAX_AANTAL_POGINGEN:
    poging = poging + 1  #pogingen += 1
    getal = int(input("Geef getal (tussen 1 en 20) : "))

    if getal == randomGetal:
        print("Je hebt het getal geraden in "+ str(poging) + "poging(en).")
        break
    else:
        if getal > randomGetal :
            print("Getal te hoog.")
        else:
            print("Getal te laag.")
        if poging >= MAX_AANTAL_POGINGEN:
            print("Verloren!! getal niet geraden binnnen", MAX_AANTAL_POGINGEN, "Pogingen")





