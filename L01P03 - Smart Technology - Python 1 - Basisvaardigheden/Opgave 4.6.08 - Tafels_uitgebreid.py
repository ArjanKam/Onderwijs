tafel = int(input("Welke tafel : "))
teller = 1
while teller <= 20:
    antwoord = str(teller * tafel)
    digits = len(antwoord)
    spaces = 5 - digits
    antwoord = spaces * " " + antwoord
    if teller < 10:
        print(" "+str(teller) + " x " + str(tafel) + " = "+ antwoord)
    else:
        print(str(teller) + " x " + str(tafel) + " = "+ antwoord)
    
    teller = teller + 1