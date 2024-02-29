cijfer = float(input("Geef je nederlandse cijfer : "))

if cijfer >= 7.5:
    print("A")
else:
    if cijfer >= 7:
        print("B")
    else:
        if cijfer >= 6.5:
            print("C")            
        else:
            if cijfer >= 6:
                print("D")
            else:
                if cijfer >= 5.5:
                    print("E")
                else:
                    print("F")
