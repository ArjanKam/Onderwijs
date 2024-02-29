print("De computer gaat een getal raden tusse 0 en 100")

minimum = 0
maximum = 100

while True:
    raden = (maximum + minimum )//2
    antwoord = input("Is het getal " + str(raden) + "? [j(a)/h(oger)/l(ager) :")
    if antwoord == "j":
        print("gevonden Hoepie...")
        break
    if antwoord == "l": #lager
        maximum = raden
    else: #hoger
        minimum = raden
