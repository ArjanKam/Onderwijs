i0 = 0
while True: #C
    i1 = input("Geef de waarde van stroom : ") #A
    if i1 == "": #C
        break
    i0 = i0 -(float(i1)) #B
print(i0) #D