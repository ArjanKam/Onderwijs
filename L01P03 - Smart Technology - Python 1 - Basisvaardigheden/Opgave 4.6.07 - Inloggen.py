WW = "1234"
GEBR = "Piet"

while True:
    gebruiker  = input("Geef je gebruikersnaam : ")
    wachtwoord = input("Geef je wachtwoord     : ")

    if BEGR == gebruiker and WW == wachtwoord:
        break
    else:
        print("Incorrect gebruiker en of wachtwoord")

print("U bent ingelogd!!!")