import random

class Deck:
    def __init__(self, cards):
        self.cards = cards
        random.shuffle(self.cards)
    
    def drawCards(self, amount):
        #for card in amount:
        pass
