import random

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
print(deck)
def shuffle(deck):
        copydeck = deck
        print(len(copydeck))
        half= int(len(copydeck)/2)
        print(half)
        adeck=copydeck[:half]
        bdeck=copydeck[half:]
        for card in range(0,int(len(copydeck))):
                print(random.randint(0,1))
        
        return copydeck

deck = shuffle(deck)
print(deck)