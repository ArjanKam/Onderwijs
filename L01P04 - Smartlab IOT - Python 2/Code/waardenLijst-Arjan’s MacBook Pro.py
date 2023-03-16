myList = []
while True: #C
    rNew = input("Geef de waarde : ") #A
    if rNew == "" or rNew == "0": #C
        break
    myList.append(float(rNew)) #B
    
#bereken serieweerstand
rVervanging = 0
for item in myList:
    rVervanging = rVervanging + item
print("Serieweerstand = ", rVervanging)

#bereken parallel weerstand
rVervanging = 0
for item in myList:
    rVervanging = rVervanging + 1/item
print("Parallel weerstand =", 1/rVervanging)    
