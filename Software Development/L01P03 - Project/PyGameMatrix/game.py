COLOUR_RED        = (255,   0,   0)

teller = 0
def playGame(events, isPosAllowed = None):
    global teller
    print(teller)
    teller += 1
    return [(10, 10, COLOUR_RED)]
    
    