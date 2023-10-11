herhaal = 0
while herhaal < 3:
    regel = 0
    while regel < 3:
        teller = 0
        while teller < 2:
            teller = teller + 1 #teller += 1
            print( 3 *" ", end="")
            print("|", end="")
        print()
        regel = regel + 1
    if herhaal < 2:
        print( 11 * "-")
    herhaal = herhaal + 1