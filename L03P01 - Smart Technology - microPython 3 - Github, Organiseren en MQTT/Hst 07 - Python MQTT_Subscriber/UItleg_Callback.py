def callbackDebugScherm(a, myEnd="\n"):
    print(a, end=myEnd)

def callbackDebugCSV(a):
    with open('readme.txt', 'w') as f:
        f.write(str(a))
        
def test(debug = None):
    a = 3
    if debug != None:
        debug(a)
    a = a + 1
    if debug != None:
        debug(a)
    b = 4 * a
    
    if debug != None:
        debug(b)
        
def uitvoer():  
    if __name__ == "__main__":
        test(callbackDebugScherm)
    else:
        test(callbackDebugCSV)


