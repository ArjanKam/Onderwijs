STROMEN = (0, 5, -2, -2.5, 1.5)

def berekenKirchhoff(stromen):
    antwoord = 0
    
    for i in stromen:
        antwoord = antwoord - i
        
    return antwoord

missendeStroom = berekenKirchhoff( STROMEN )
print(missendeStroom)

