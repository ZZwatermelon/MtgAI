
class Player:
    def __innit__(self, starting_life, deck):
        self.hand = []
        self.life_total = starting_life
        self.library = deck
        self.graveyard = []
    
    def lose_life(self, amount):
        self.life_total -= amount
    
    def take_damage(self, amount):
        self.lose_life(amount)
