aantalDeelbaar3 = 0

getal = int(input("Geef het  1ste getal : "))
laagste = getal
hoogste = getal
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1

counter = 1
while True:
    getal = input("Geef het "+str(counter)+"e getal : ")
    if getal == "":
        break
    getal = int(getal)
    if getal % 3 == 0:
        aantalDeelbaar3 = aantalDeelbaar3 + 1
    if getal < laagste:
        laagste = getal
    if getal > hoogste:
        hoogste = getal
    counter += 1
    
print("Hoogste :", hoogste, "laagste :", laagste, "Deelbaar 3 :", aantalDeelbaar3)
