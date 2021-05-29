from deck import Deck

class Player:
    def __init__(self, starting_life, deck):
        self.hand = []
        self.life_total = starting_life
        self.library = Deck(deck)
        self.graveyard = []

        self.lost = False

        self.milled = False

        for card in self.library.cards:
            card.owner = self

        for card in self.library.drawCards(7):
            self.hand.append(card)
    
    def lose_life(self, amount):
        self.life_total -= amount
    
    def take_damage(self, amount):
        self.lose_life(amount)