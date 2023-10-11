MAX_SPATIES = 23
username = input("Wat is je naam : ")
lengte = len(username)
aantal_spaties = MAX_SPATIES - lengte
begin_spaties = aantal_spaties // 2
einde_spaties = aantal_spaties - begin_spaties 
print("        \\|||||||/     ")
print("        ( o   o )       ")
print("|--ooO-----(_)----------|")
print("|                       |")
print("|"+ begin_spaties * " "
      +username + einde_spaties * " " + "|")
print("|                       |")
print("|------------------Ooo--|")
print("         |__||__|        ")
print("          ||  ||         ")
print("         ooO  Ooo")