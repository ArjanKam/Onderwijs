def berekenKirchhoff(stromen):
    antwoord = 0
    for i in stromen:
        antwoord = antwoord - i        
    return antwoord

def invoer():
    antwoord = []
    while True:
        stroom = input("Voeg stroom toe : ")
        if stroom == "":
            break
        
    return antwoord
    
stromen = invoer()
missendeStroom = berekenKirchhoff( stromen )
print(missendeStroom)

