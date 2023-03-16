print("Bereken serie-weerstand. Stop als 0 wordt ingevoerd !!!")

weerstandTotaal = 0

while True:
    weerstand = int(input("Geef de waarde van weerstand : "))
    
    if weerstand == 0:
        print("Totale weerstand = ", weerstandTotaal)
        exit()
    else:
        weerstandTotaal = weerstandTotaal + weerstand
