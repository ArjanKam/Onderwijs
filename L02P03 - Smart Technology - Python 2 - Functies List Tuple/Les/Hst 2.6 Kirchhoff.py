def invoer():
    lijst = []
    while True:
        i = input("Geef waarde +is naar knooppunt, -is vanaf knooppunt: ")
        if i == "":
            return lijst
        lijst.append(int(i))
        
def berekenKirchhoff(lijst):
    ontbrekende = 0
    for x in lijst:
        ontbrekende -= x
    return ontbrekende

lijst = (10, -20, 5)#invoer()
ontbrekende = berekenKirchhoff(lijst)
print(lijst, ontbrekende)
