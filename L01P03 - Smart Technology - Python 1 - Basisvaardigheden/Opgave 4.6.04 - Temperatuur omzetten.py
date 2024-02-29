"""
    4.6.4	Temperatuur omzetter
    Er zijn verschillende temperatuur aanduidingen in de wereld.
    De drie bekendste zijn de Kelvin, Fahrenheit en de Celsius aanduiding.
    Deze drie waarden kunnen naar elkaar omgezet worden.
    Onderstaande stroomdiagram geeft een programma aan hoe je dat kan doen.
    Maak aan de hand van het stroomdiagram 
"""

print("Temperatuur converter - Main menu")
print("1 - Convert from Celcius to Fahrenheit.")
print("2 - Convert from Fahrenheit to Celcius.")

option = input("Geef keuze : ")
if option == "1":
    celcius = float(input("Type temperatur in Celcius : "))
    fahrenheit = (celcius * 9 / 5) + 32
    print("Temperature", fahrenheit, "degrees fahrenheit")
else:
    if option == "2":
        fahrenheit = float(input("Type temperatur in fahrenheit : "))
        celcius = (fahrenheit - 32) * 9 / 5
        print("Temperature", celcius, "degrees Celcius")
    else:
        print("Invalid option")