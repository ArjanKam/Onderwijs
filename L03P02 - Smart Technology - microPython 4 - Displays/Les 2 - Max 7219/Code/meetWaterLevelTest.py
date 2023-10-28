#level1, level2, level2Up
def getWaterLevel():
    while True:
        for level2 in range(1, 100):
            yield 100-level2, level2, True
        for level2 in range(99, 0, -1):
            yield 100-level2, level2, False

if __name__ == "__main__":
    for level1, level2, level2Up in getWaterLevel():
        print("{:02d}".format(level1), "{:02d}".format(level2), level2Up)