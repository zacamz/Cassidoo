suits = ["♠","♥","♦","♣"]

royalty = ["J","Q","K","A"]

def createDecks(number_of_decks:int):
    decks= []
    for deck in range(0,number_of_decks):
        cards = []
        for suit in enumerate(suits):
            for num in range(0,9):
                cards+= f"{num}{suit}"
        decks+= cards
    return decks

print(createDecks(1))