print("De waarde die je wilt berekenen laat je leeg door een <enter> in te typen")
u = input("Geef spanning : ")
i = input("Geef stroom : ")
r = input("Geef weerstand : ")

if r == "":
    r = float(u) / float(i)
else:
    if u == "":
        u = float(r) * float(i)
    else:
        i = float(u) / float(r)
    
print("R=", r, "U=", u, "I=", i)