import random


class Deck:
     def __init__(self,number_of_decks:int):
            self.cards = createDecks(number_of_decks)
     def shuffle(self):
        copydeck = self.cards
        half= int(len(copydeck)/2)
        adeck=copydeck[:half]
        bdeck=copydeck[half:]
        shuffleddeck = []
        for card in range(0,half):
            try:
                shuffleddeck.append(adeck.pop(random.randint(0,1)))
            except:
                shuffleddeck.append(adeck.pop(0))
            try:
                shuffleddeck.append(bdeck.pop(random.randint(0,1)))
            except:
                shuffleddeck.append(bdeck.pop(0))
        self.cards = shuffleddeck
        return self.cards
     def draw(self,numberof_cards:int):
        try:
            drawn = []
            for card in range(numberof_cards):
                drawn.append(self.cards.pop(0))
            return drawn
        except:
            return []
suits = ["♠","♥","♦","♣"]

royalty = ["J","Q","K","A"]

def createDecks(number_of_decks:int):
    decks= []
    for loop in range(0,number_of_decks):
        cards = []
        for suit in enumerate(suits):
            for num in range(2,11):
                card = str(num)+suit[1]
                cards.append(card)
            for special in enumerate(royalty):
                card = special[1]+suit[1]
                cards.append(card)
        decks += cards
    return decks

deck = createDecks(1)
# print(deck)
def shuffle(deck):
        copydeck = deck
        # print(len(copydeck))
        half= int(len(copydeck)/2)
        # print(half)
        adeck=copydeck[:half]
        bdeck=copydeck[half:]
        shuffleddeck = []
        for card in range(0,half):
            try:
                shuffleddeck.append(adeck.pop(random.randint(0,1)))
            except:
                shuffleddeck.append(adeck.pop(0))
            try:
                shuffleddeck.append(bdeck.pop(random.randint(0,1)))
            except:
                shuffleddeck.append(bdeck.pop(0))
                 
        
        return shuffleddeck

# deck =shuffle(deck)
# deck =shuffle(deck)
# deck =shuffle(deck)
# deck =shuffle(deck)
# deck =shuffle(deck)
# print(deck)
# print(len(deck))

test = Deck(1)

print(test.draw(1))   
print(test.draw(1))   