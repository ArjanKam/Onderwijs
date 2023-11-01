#listOfChars is a list of dot_matrix chars
#returns a matrix with all the characters
def setCompleteList( listOfChars ):
    allCharacters = []
    if len(listOfChars) == 0:
        return allCharacters
    y = 0
    while y < len(listOfChars[0]):
        line = []
        for c in listOfChars:
            line = line + list(c[y])
        allCharacters.append(list(line))
        y = y + 1            
    return allCharacters

#framebuffer is an instance of frameBuf
def setByteArray(framebuffer, allCharacters):
    yMax = len(allCharacters)
    if yMax == 0:
        return
    xMax = len(allCharacters[0])
    
    for y in range(yMax):
        for x in range(xMax):
            if allCharacters[y][x] == 0:
                framebuffer.pixel(x,y, 0)
            else:
                framebuffer.pixel(x,y, 1)

#convert h=15 m=43 s=32 to tuple (1, 5, 4, 3)
#seconds are for the sepetator
def getTimeList(hours, minutes, seconds):
    if seconds % 2 == 0:
        seperator = "|"
    else:
        seperator = ";"
    return (hours // 10, hours % 10, seperator
            , minutes // 10, minutes % 10)

def getTempList(temp):
    tempList = []
    negative = temp < 0
    if negative:
        tempList.append("-")
        temp = temp * -1
    
    if temp >= 100:
        honderds = temp // 100
        temp = temp - (honderds * 100)
        tempList.append(honderds // 10)
        tempList.append(temp // 10)
        tempList.append(temp % 10)
    else:
        if not negative:
            tempList.append(" ")
        if temp > 10:
            tempList.append(temp // 10)
            tempList.append(temp % 10)
        else:
             tempList.append(" ")
             tempList.append(temp % 10)
          
    tempList.append("|")
    tempList.append("C")
    return tuple(tempList)

def getHumidityList(humidity):
    if humidity >= 100:
        return (1, 0, 0, "%")
    return (" ", humidity // 10, humidity % 10, " ", "%")

#list of elements to convert to matrix
def elementsToMatrix(ls):
    matrix = []
    for element in ls:
        matrix.append(dotMatrix.MATRIX6x8[element])
    return matrix 

def showSeconds(seconds):
    position = 1 + (seconds % 60 // 2)
    matrixDisplay.display.pixel(position, 7, 1)
    
def showTime(hours, minutes, seconds):
    lst = getTimeList(hours, minutes, seconds)
    showList(lst, seconds)
    
def showTemp(temp, seconds):
    lst = getTempList(temp)
    showList(lst, seconds)

def showHumidity(humidity, seconds):
    lst = getHumidityList(humidity)
    showList(lst, seconds)
    
def showList(lst, seconds):
    timeMatrix = elementsToMatrix(lst)
    cl = matrixBuffer.setCompleteList(timeMatrix)
    matrixDisplay.display.fill( matrixDisplay.CLEAR_SCREEN )
    matrixBuffer.setByteArray(matrixDisplay.display.framebuf, cl)
    showSeconds(seconds)
    matrixDisplay.display.show()
    
if __name__ == "__main__":
    import dotMatrix
    
    listOfChars1 = []
    listOfChars1.append(dotMatrix.ONE)
    listOfChars1.append(dotMatrix.CC_TOP)
    listOfChars1.append(dotMatrix.SEVEN)
    
    listOfChars2 = []
    listOfChars2.append(dotMatrix.ONE)
    listOfChars2.append(dotMatrix.CC_BTTM)
    listOfChars2.append(dotMatrix.SEVEN)
    print(listOfChars2)
    list1 = setCompleteList(listOfChars1)
    print(list1)
    dotMatrix.printMatrix(list1)
    dotMatrix.printMatrix(setCompleteList(listOfChars2))