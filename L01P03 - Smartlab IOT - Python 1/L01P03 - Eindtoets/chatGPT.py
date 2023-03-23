# vraag de gebruiker om de hoogte van de kerstboom
hoogte = int(input("Voer de hoogte van de kerstboom in: "))

# bereken de breedte van de boom op het breedste punt
breedte = 2 * hoogte - 1

# loop over elke rij van de kerstboom
for rij in range(hoogte):
    # bereken het aantal spaties dat nodig is voor deze rij
    spaties = (breedte - (2 * rij + 1)) // 2
    # print de spaties
    print(" " * spaties, end="")
    # print de sterren voor deze rij
    print("*" * (2 * rij + 1))

# print de stam van de kerstboom
for rij in range(3):
    print(" " * (hoogte - 1), end="")
    print("**")