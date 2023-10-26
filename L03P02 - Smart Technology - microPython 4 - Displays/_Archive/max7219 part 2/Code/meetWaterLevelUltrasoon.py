#level1, level2, level2Up
values = range(1, 100)
def getWaterLevel():
    while True:
        for level2 in values:
            yield 100-level2, level2, True
        values = values.reverse()

if __name__ == "__main__":
    for level1, level2, level2Up in getWaterLevel():
        print(level1, level2, level2Up)