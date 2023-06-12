
x = 0
while x < 9:
    y = 0
    while y < 9:
        z = 0
        while z < 0:
            som = z + 10 * y + 100 * x
            
            
            
            z = z + 1
        y = y + 1
    x = x + 1


teller = 0
while teller <= 999:
    som = 3 * teller
    
    laatste = teller % 10
    #eindAntwoord = laatste + (10* laatste) + (100 * laatste)
    eindAntwoord = int(str(laatste)+str(laatste)+str(laatste))
    
    if som == eindAntwoord and som != 0:
        print(teller, som, eindAntwoord)
        break
    
    teller = teller + 1
    
    
