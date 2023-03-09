TEKEN = "*"
SPACE = " "
STAMHOOGTE = 2
STAMBREEDTE = 3
#invoer hoogte
aantal = 0
while aantal < 3:
    aantal = int(input("Hoe hoog moet de kerstboom zijn (>=3) : "))
#teken de kerstboom
rij = 0
while rij < aantal:
    spaties = (aantal-rij)
    tekens = (rij*2 + 1 )
    print( spaties * SPACE + tekens* TEKEN)
    rij += 1

#print de stam
rij = 0
while rij < STAMHOOGTE:
    print((aantal-1) * SPACE + STAMBREEDTE * TEKEN)
    rij += 1
