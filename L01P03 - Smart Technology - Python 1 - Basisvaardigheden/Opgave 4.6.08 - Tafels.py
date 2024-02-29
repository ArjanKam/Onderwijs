tafel = int(input("Welke tafel wil je tonen : "))

counter = 1
while counter <= 10:
    if counter < 10:
        print("",counter , "x", tafel, "=", counter * tafel)
    else:
        print(counter , "x", tafel, "=", counter * tafel)
    counter += 1
