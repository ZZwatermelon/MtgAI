import random
from card import Card

class Deck:
    def __init__(self, deckFile):
        self.card_names = []
        self.cards = []

        with open("decks\\" + deckFile, 'r') as f:
            deck_list = f.read()
            
        deck_list = deck_list.split('\n')

        for card in deck_list:
            amount = card[0:card.index('x')]

            for number in range(int(amount)):
                self.card_names.append(card[card.index('x') + 2:len(card)])
        
        for card in self.card_names:
            self.cards.append(Card(card))
        

        random.shuffle(self.cards)

        print("Initialized Deck")
    
    def drawCards(self, amount: int):
        drawn_cards = []

        if amount > len(self.cards):
            self.cards[0].owner.milled = True

        for e in range(amount):
            drawn_cards.append(self.cards[0])
            self.cards.remove(self.cards[0])
        
        return drawn_cards


#test = Deck('burn.txt')
#print(test.cards)
#drew = test.drawCards(2)
#print(f"{test.cards}, {drew}")