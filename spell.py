
class Spell:
    def __init__(self, card, trigger, targets = None):
        self.card = card
        self.trigger = trigger
        self.targets = targets
    
    def resolve(self):
        pass