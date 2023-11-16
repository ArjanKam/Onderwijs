from math import sqrt

def afstand(pos1, pos2):
    x = pos2[0] - pos1[0]
    y = pos2[1] - pos1[1]
    return sqrt(x * x + y * y)
    
if __name__ == "__main__":
    assert afstand((1,1), (2,2)) == 1.4142135623730951