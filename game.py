from random import random

from phases import Phases

import random

class Game():
    def __init__(self, players):
        self.players = players
        self.active_player = players[random.randint(0, len(players)-1)]
        self.priority_player = None

        self.upkeep_triggers = []
        self.death_triggers = []

        self.stack = []
        self.battlefield = []
        self.exile = []

        self.phase = Phases.BEGINNING_PHASE
    
    def turn(self):
        self.phase = Phases.UNTAP_STEP
        for permanent in self.battlefield:
            if permanent.controller == self.active_player:
                permanent.tapped = False
        
        self.phase = Phases.UPKEEP_STEP
        
        #for trigger in self.upkeep_triggers:
        #    trigger.upkeepTrigger()
        #    self.stateBasedActions()
        #Avoiding triggers for now
        
        self.priority_player = self.active_player
        self.makeMove(self.priority_player)

        self.phase = Phases.DRAW_STEP
    
    def stateBasedActions(self):
        change = False
        for player in self.players:
            if (player.life_total <= 0) or (player.milled == True) or (player.poison_counters >= 10):
                player.lost = True
                change = True
        
        for permanent in self.battlefield:
            if 'Creature' in permanent.spell_type:
                if permanent.current_toughness <= 0:
                    permanent.owner.graveyard.append(permanent)
                    self.battlefield.remove(permanent)

                    change = True

                    #for trigger in self.death_triggers:
                    #    trigger.deathTrigger(permanent.spell_type)
                    #Avoiding trigegrs for now
            
            if 'Planeswalker' in permanent.spell_type:
                if permanent.loyalty <= 0:
                    permanent.owner.graveyard.append(permanent)
                    self.battlefield.remove(permanent)

                    change = True

                    #for trigger in self.death_triggers:
                    #    trigger.deathTrigger(permanent.spell_type)
        
        if change:
            self.stateBasedActions()
        

    def makeMove(self, player):
        pass