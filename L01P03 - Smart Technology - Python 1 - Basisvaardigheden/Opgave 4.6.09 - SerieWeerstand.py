print("Serie weerstanden optellen..")

rVervanging = 0
rNew = 42.0

while rNew != 0.0: 
    rNew = float(input("Geef de waarde de weerstand : "))
    if rNew != 0.0: 
        rVervanging = rVervanging + rNew
        
print(rVervanging)


