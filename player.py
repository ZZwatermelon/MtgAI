from deck import Deck
from card import Card

class Player:
    def __init__(self, starting_life, deckFile):
        self.hand = []
        self.life_total = starting_life
        self.library = Deck(deckFile, self)
        self.graveyard = []
        
        self.available_mana = {
            'W':0,
            'U':0,
            'B':0,
            'R':0,
            'G':0,
            'generic': 0
        }

        self.lands_played = 0

        self.last_action = None

        self.lost = False

        self.milled = False

        for card in self.library.cards:
            card.owner = self

        for card in self.library.drawCards(7):
            self.hand.append(card)
    
    print("Initalized Player")
    
    def lose_life(self, amount):
        self.life_total -= amount
    
    def take_damage(self, amount):
        self.lose_life(amount)
    
    def canPayFor(self, card: Card):
        print(f"Available Mana: {self.available_mana}")
        for mana in card.mana_cost:
            if card.mana_cost[mana] > self.available_mana[mana]:
                print(card.mana_cost)
                return False
        return True