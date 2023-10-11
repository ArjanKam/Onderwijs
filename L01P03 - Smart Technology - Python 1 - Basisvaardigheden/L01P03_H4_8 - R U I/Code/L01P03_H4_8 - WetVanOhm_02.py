print("Geef enter als je die waarde wilt weten !!!!")
uString = input("Wat is de spannning (int): ")
iString = input("Wat is de stroom    (int): ")
rString = input("Wat is de weerstand (int): ")

if uString != "" and iString != "":
    u = float(uString)
    i = float(iString)
    r = u / i  
elif iString == "" and rString == "":
    i = float(iString)
    r = float(rString)
    u = r * i
elif uString != "" and rString != "":
    u = float(uString)
    r = float(rString)
    i = r / u
else:
    print("Te veel niet ingevuld")

print("u=",u, "i=", i, "r=", r)