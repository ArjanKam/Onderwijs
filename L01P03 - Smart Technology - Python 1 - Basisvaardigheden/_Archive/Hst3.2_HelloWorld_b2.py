"""
    Programma dat poppetje op scherm toont met gegeven naam erin
    gemaakt door : Arjan Kamberg
    datum        : 8 feb 2023
    bron : 
"""
MAX_SPATIES = 23 

name = input("Geef je naam : ")
lengte_naam = len(name)
aantal_spaties = MAX_SPATIES - lengte_naam
spaties_ervoor = aantal_spaties // 2 # resultaat is een int
spaties_erachter = aantal_spaties - spaties_ervoor
s_ervoor = spaties_ervoor * " " 
s_erachter = spaties_erachter * " "

# vanaf hier wordt het poppetje getekend
print("                        ")
print("        \\\\|||||//     ")
print("        ( o   o )       ")
print("|--ooO-----(_)----------|")
print("|                       |")
print("|", s_ervoor, name, s_erachter, "|", sep="")
print("|                       |")
print("|------------------Ooo--|")
print("         |__||__|        ")
print("          ||  ||         ")
print("         ooO  Ooo")