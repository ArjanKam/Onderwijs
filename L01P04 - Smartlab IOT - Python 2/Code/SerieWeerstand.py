rVervanging = 0
while True: #C
    rNew = input("Geef de waarde de weerstand : ") #A
    if rNew == "": #C
        break
    rVervanging = rVervanging + (float(rNew)) #B
print(rVervanging) #D