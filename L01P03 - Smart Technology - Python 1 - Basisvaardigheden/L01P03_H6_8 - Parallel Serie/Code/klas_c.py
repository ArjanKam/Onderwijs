print("Bereken de vervangende serie weerstand. Eindig met invoer van het cijfer 0.")
weerstandTotaal = 0
while True:
    weerstand = float(input("Geef weerstand : "))

    if weerstand != 0:
        weerstandTotaal = weerstandTotaal + weerstand
    else:
        break

print("De totale vervangingsweerstand is : ", weerstandTotaal)
