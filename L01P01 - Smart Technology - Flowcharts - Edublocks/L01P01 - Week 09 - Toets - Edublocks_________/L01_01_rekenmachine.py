totaal = 0
operator = "+"

while operator != "=":
    operator = input("Geef de operator [+-*=] :")
    if operator != "=":
        waarde = float(input("Voer het getal in : "))
        if operator == "*":
            new = totaal * waarde
        if operator == "+":
            new = totaal + waarde
        if operator == "-":
            new = totaal - waarde
        print(80*"-")
        print(totaal, operator, waarde, "=", new)
        totaal = new
                