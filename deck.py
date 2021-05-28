import random
import os

class Deck:
    def __init__(self, deckFile):
        with open("decks\\" + deckFile, 'r') as f:
            deck_list = f.read()
            
        self.cards = deck_list.split('\n')
        random.shuffle(self.cards)
    
    def drawCards(self, amount):
        drawn_cards = []

        for e in range(amount):
            drawn_cards.append(self.cards[0])
            self.cards.remove(self.cards[0])
        
        return drawn_cards


#test = Deck('burn.txt')
#print(test.cards)
#drew = test.drawCards(2)
#print(f"{test.cards}, {drew}")