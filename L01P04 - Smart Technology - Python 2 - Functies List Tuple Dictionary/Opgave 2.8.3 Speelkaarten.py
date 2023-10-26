from random import choice
KLEUREN = ("Harten", "Ruiten", "Klaveren", "Schoppen")
WAARDEN = (2, 3, 4, 5, 6, 7, 8, 9, 10, "B", "V", "H", "A")
NUMBER_OF_CARDS = 52

def newCard():
    return (choice(KLEUREN), choice(WAARDEN))

def getCard(availableCards):
    return choice(availableCards)

def shuffleAllCards():
    cards = []
    x = NUMBER_OF_CARDS
    while x > 0:
        card = newCard()
        if card not in cards:
            cards.append(card)
            #print(x, card)
            x -= 1
    return cards

def removeCards(availableCards, usedCards):
    available = availableCards.copy()
    for card in usedCards:
        #print("remove >> ", card)
        available.remove(card)
    return available

#0 <= aantal <= 52
def getCards(aantal = NUMBER_OF_CARDS, usedCards = [], availableCards = []):
    maxCards = len(availableCards)
    if maxCards == 0:
        maxCards = NUMBER_OF_CARDS
        availableCards = shuffleAllCards()
    if aantal < 0:
        aantal = 0
    if aantal > maxCards - len(usedCards):
        aantal = maxCards - len(usedCards)
    
    cards = []
    while aantal > 0:
        card = getCard(availableCards)
        if card not in cards and card not in usedCards:
            cards.append(card)
            aantal -= 1
    return cards

def deal(numberOfPlayers, numberOfCards, numberOfDecks = 1):
    cards = []
    allCards = shuffleAllCards()
    while numberOfDecks > 1:
        allCards += shuffleAllCards()
        numberOfDecks -= 1
        
    while numberOfPlayers > 0:
        newCards = getCards(numberOfCards, availableCards=allCards)
#         print("PLAY>>", numberOfPlayers)
#         print("ALL >> ", allCards)
#         print("NEW >> ", newCards)
        allCards = removeCards(allCards, newCards)
        cards.append(newCards)
        numberOfPlayers -= 1
    return cards, allCards

# allCards = getCards()
# print("3 cards : ", getCards(3), end="\n\n")
# cards = getCards(51)
# print("51 cards : ", cards, end="\n\n")
# print("rest cards : ", getCards(usedCards = cards), end="\n\n")
# 
# restdeck = removeCards(allCards, cards)
# print(restdeck)
#print(shuffleAllCards())
cards = deal(4, 7, 2)
for hand in cards[0]:
    print(">>", hand)
    
print(">>Deck >> ", len(cards[1]), cards[1])