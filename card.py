
class Card:
    def __init__(self, name, spell_type):
        self.name = name
        self.spell_type = spell_type
    
    def play(self):
        if self.spell_type == 'land':
            pass
        elif self.spell_type == 'creature':
            pass
        elif self.spell_type == 'instant':
            pass
        elif self.spell_type == 'sorcery':
            pass
        else:
            raise RuntimeError('A card had an unrecognized card type')
        