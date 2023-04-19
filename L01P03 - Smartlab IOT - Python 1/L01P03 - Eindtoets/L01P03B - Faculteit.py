# faculteit

fac = int(input("Geef faculteit : "))
if fac < 0:
    print("Onmogelijk")
else:
    result = 1
    n = fac
    while n > 1:
        result *= n
        n -= 1
    print( str(fac) + "! =", result)
        