from array import array
from card import Card
from player import Player
from random import random

from phases import Phases
from spell import Spell

import random

class Game():
    def __init__(self, players: list):
        self.players = players
        self.active_player = players[random.randint(0, len(players)-1)]
        self.priority_player = None

        self.upkeep_triggers = []
        self.death_triggers = []

        self.stack = []
        self.battlefield = []
        self.exile = []

        self.phase = Phases.BEGINNING_PHASE

        self.turn()
    
    def turn(self):
        self.phase = Phases.BEGINNING_PHASE
        print("Beginning Phase")

        self.phase = Phases.UNTAP_STEP
        print("Untap Step")
        for permanent in self.battlefield:
            if permanent.controller == self.active_player:
                permanent.tapped = False
        
        self.phase = Phases.UPKEEP_STEP
        
        #for trigger in self.upkeep_triggers:
        #    trigger.upkeepTrigger()
        #    self.stateBasedActions()
        #Avoiding triggers for now
        
        self.priority_player = self.active_player
        self.evaluateMoves(self.priority_player)

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
        

    def makeMove(self, move):
        self.stack.append(Spell(move, 'cast'))

    def getLegalMoves(self, speed, player: Player):
        legal_moves = []

        self.getAvailableMana(player)

        if speed == 'fast':
            for card in player.hand:
                if ('Instant' in card.spell_type or 'Flash' in card.card.oracle_text()) and player.canPayFor(card):
                    legal_moves.append(card)
            
            legal_moves.append('pass')
        
        return legal_moves

    
    def getAvailableMana(self, player: Player):
        for permanent in self.battlefield:
            if permanent.owner == player:
                if 'Land' in permanent.spell_type:
                    if 'Plains' in permanent.spell_type:
                        player.available_mana['W'] += 1
                    elif 'Island' in permanent.spell_type:
                        player.available_mana['U'] += 1
                    elif 'Swamp' in permanent.spell_type:
                        player.available_mana['B'] += 1
                    elif 'Mountain' in permanent.spell_type:
                        player.available_mana['R'] += 1
                    elif 'Forest' in permanent.spell_type:
                        player.available_mana['G'] += 1

test = Game([Player(20, 'burn.txt'), Player(20, 'burn.txt')])
                    