vergroting = int(input("Hoeveel keer groter ? "))
herhaal = 0
while herhaal < 3:
    regel = 0
    while regel < 3 * vergroting:
        teller = 0
        while teller < 2:
            teller = teller + 1 #teller += 1
            print(vergroting * 3 *" ", end="")
            print("|", end="")
        print()
        regel = regel + 1
    if herhaal < 2:
        print(((vergroting * 9) + 2)* "-")
    herhaal = herhaal + 1