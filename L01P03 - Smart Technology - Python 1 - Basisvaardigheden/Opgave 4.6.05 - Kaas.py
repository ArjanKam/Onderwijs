"""
    Kaas Kaas Kaas
"""

geel = input("Is de kaas geel? [j/n] : ")
if geel == 'j':
    gaten = input("Zitten er gaten in? [j/n] : ")
    if gaten == 'j':
        duur = input("Is de kaas belachelijk duur? [j/n] : ")
        if duur == 'j':
            print("Dit is een emmentaler")
        else:
            print("Dit is een leerdammer")
    else:
        steen = input("Is de kaas hard als steen? [j/n] : ")
        if steen == 'j':
            print("Dit is een Parmigiano Reggiano")
        else:
            print("Dit is een Goudse kaas")
    
else:
    blauw = input("Heeft de kaas blauwe schimmel? [j/n] : ")
    
    # etc etc etc
    