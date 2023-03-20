"""
    opgave 4.6.9
"""

print("Berekenen wet van Ohm.")
print("Wat je wilt berekenen geen <enter>.")
stroom    = input("Geef de stroom    : ")
spanning  = input("Geef de spanning  : ")
weerstand = input("Geef de weerstand : ")

u_afwezig = spanning == ""
i_afwezig = stroom == ""
r_afwezig = weerstand == ""

if (i_afwezig and u_afwezig) or (i_afwezig and r_afwezig) or (u_afwezig and r_afwezig):
    print("Te veel NIET ingevuld.")
elif i_afwezig:
    spanning = float(spanning)
    weerstand = float(weerstand)
    if weerstand == 0:
        stroom = 99999.99
    else:
        stroom = float(spanning) / float(weerstand)
elif u_afwezig:
    spanning = float(stroom) * float(weerstand)
else:
    spanning = float(spanning)
    stroom = float(stroom)
    if stroom == 0.0:
        weerstand = 9999.99
    else:
        weerstand = float(spanning) / float(stroom)

print( spanning, "V", stroom,"A", weerstand, "Ohm")
