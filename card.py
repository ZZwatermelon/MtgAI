import scrython
import time
import sys

from scrython.foundation import ScryfallError

class Card:
    def __init__(self, name):
        self.name = name
        try:
            time.sleep(.15)
            self.card = scrython.cards.Named(exact=self.name)
        except ScryfallError:
            print(f"{self.name} was not found")
            sys.exit()

        self.spell_type = self.card.type_line()

        self.owner = None

    def play(self):
        if 'Land' in self.spell_type:
            pass
        elif 'Creature' in self.spell_type:
            pass
        elif 'Instant' in self.spell_type:
            pass
        elif 'Sorcery' in self.spell_type:
            pass
        else:
            raise RuntimeError('A card had an unrecognized card type')
    
    def findType(self):
        time.sleep(.2)
        self.card = scrython.cards.Named(exact=self.name)
        return self.card.type_line()

#test = Card('Forest')
#print(test.spell_type)