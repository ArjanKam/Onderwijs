correct = False
while not correct:
    invoer = input("Geef een getal : ")
    if invoer.isnumeric():
        getal = int(invoer)
        correct = True
print(getal, type(getal))

