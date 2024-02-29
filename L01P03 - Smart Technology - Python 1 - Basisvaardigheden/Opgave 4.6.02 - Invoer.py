aantalDeelbaar3 = 0

getal = int(input("Geef het  1ste getal : "))
laagste = getal
hoogste = getal
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1

getal = int(input("Geef het  2e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

getal = int(input("Geef het  3e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

getal = int(input("Geef het  4e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

getal = int(input("Geef het  5e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

getal = int(input("Geef het  6e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

getal = int(input("Geef het  7e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

getal = int(input("Geef het  8e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

getal = int(input("Geef het  9e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

getal = int(input("Geef het 10e getal : "))
if getal % 3 == 0:
    aantalDeelbaar3 = aantalDeelbaar3 + 1
if getal < laagste:
    laagste = getal
if getal > hoogste:
    hoogste = getal

print("Hoogste", hoogste, "laagste", laagste, "Deelbaar 3", aantalDeelbaar3)