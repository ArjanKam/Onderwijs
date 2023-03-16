rVervanging = 0
while True: #C
    rNew = input("Geef de waarde de weerstand : ") #A
    if rNew == "" or rNew == "0": #C
        break
    rVervanging = rVervanging + (1/float(rNew)) #B
    
if rVervanging == 0:
    print("Weerstand is 0")
else:
    print(1/rVervanging) #D
