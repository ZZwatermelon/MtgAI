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
        self.mana_cost = self.getManaCost()

        self.owner = None
        self.tapped = False
        self.controller = None

        if 'Creature' in self.spell_type:
            self.base_power = self.card.power()
            self.base_toughness = self.card.toughness()

            self.current_power = self.base_power
            self.current_toughness = self.base_toughness
        
        if 'Planeswalker' in self.spell_type:
            self.loyalty = self.card.loyalty()

    def play(self, X = 0):
        if 'Land' in self.spell_type:
            pass
        elif 'Creature' in self.spell_type:
            pass
        elif 'Instant' in self.spell_type:
            pass
        elif 'Sorcery' in self.spell_type:
            pass
        elif 'Planeswalker' in self.spell_type:
            pass
        else:
            print(self.spell_type)
            raise RuntimeError('A card had an unrecognized or unsupported card type')

    def getManaCost(self):
        cost = self.card.mana_cost()
        cost = cost.split('}')

        for value in cost:
            cost[cost.index(value)] = value.lstrip("{")
        cost.remove('')
        
        mana_cost = {
            'W':0,
            'U':0,
            'B':0,
            'R':0,
            'G':0,
            'generic':0
        }

        for symbol in cost:
            if symbol == 'W':
                mana_cost['W'] += 1
            elif symbol == 'U':
                mana_cost['U'] += 1
            elif symbol == 'B':
                mana_cost['B'] += 1
            elif symbol == 'R':
                mana_cost['R'] += 1
            elif symbol == 'G':
                mana_cost['G'] += 1
            else:
                try:
                    mana_cost['generic'] += int(symbol)
                except ValueError:
                    print('Unsupported mana value')
        
        return mana_cost
    
#    def upkeepTrigger(self):
#        if 'Land' in self.spell_type:
#            pass
#        elif 'Creature' in self.spell_type:
#            pass
#        elif 'Instant' in self.spell_type:
#            pass
#        elif 'Sorcery' in self.spell_type:
#           pass
#        else:
#            raise RuntimeError('A card had an unrecognized card type')
#    
#   def deathTrigger(self, death_type = None):
#        if 'Land' in self.spell_type:
#           pass
#       elif 'Creature' in self.spell_type:
#           pass
#        elif 'Instant' in self.spell_type:
#            pass
#        elif 'Sorcery' in self.spell_type:
#           pass
#        else:
#            raise RuntimeError('A card had an unrecognized card type')

#test = Card('Mountain')
#print(test.getManaCost())