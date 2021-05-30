from card import Card
from player import Player
from random import random

from phases import Phases
from spell import Spell

import random
import copy

class Game():
    def __init__(self, players: list):
        self.players = players
        self.active_player: Player = players[random.randint(0, len(players)-1)]
        self.priority_player: Player = None

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
        self.active_player.lands_played = 0

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
        self.startChain()

        self.phase = Phases.DRAW_STEP
        
        for card in self.active_player.library.drawCards(1):
            self.active_player.hand.append(card)

        self.priority_player = self.active_player
        self.startChain()

        self.phase = Phases.PRE_COMBAT_MAIN_PHASE

        self.priority_player = self.active_player
        self.startChain()
    
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
        
    def playersPassed(self):
        for player in self.players:
            if player.last_action != 'pass':
                return False
        return True

    def makeMove(self, move):
        if move == 'pass':
            self.priority_player.last_action = 'pass'
        else:
            self.stack.append(move)
            self.priority_player.last_action = move

    def getLegalMoves(self, speed, player: Player):
        legal_moves = []

        self.getAvailableMana(player)

        if speed == 'fast':
            for card in player.hand:
                if ('Instant' in card.spell_type or 'Flash' in card.card.oracle_text()) and player.canPayFor(card):
                    legal_moves.append(card)
            
            legal_moves.append('pass')
        
        elif speed == 'slow':
            card: Card
            for card in player.hand:
                if ('Land' in card.spell_type and player.lands_played < 1):
                    legal_moves.append(card)
                elif player.canPayFor(card):
                    legal_moves.append(card)
        
        return legal_moves

    
    def getAvailableMana(self, player: Player):
        for permanent in self.battlefield:
            if permanent.owner == player and not permanent.tapped:
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
    
    def resolveStack(self):
        for spell in self.stack:
            spell.resolve()
    
    def evaluateMoves(self):
        if self.phase != Phases.PRE_COMBAT_MAIN_PHASE and self.phase != Phases.POST_COMBAT_MAIN_PHASE:
            legal_moves = self.getLegalMoves('fast', self.priority_player)

        elif (self.phase == Phases.PRE_COMBAT_MAIN_PHASE or self.phase == Phases.POST_COMBAT_MAIN_PHASE) and self.stack == []:
            legal_moves = self.getLegalMoves('slow', self.priority_player)

        elif (self.phase == Phases.PRE_COMBAT_MAIN_PHASE or self.phase == Phases.POST_COMBAT_MAIN_PHASE) and self.stack != []:
            legal_moves = self.getLegalMoves('fast', self.priority_player)
        
        for move in legal_moves:
            temp_copy = copy.deepcopy(self)
            if move == 'pass':
                temp_copy.makeMove('pass')
            else:
                temp_copy.makeMove(Spell(move, 'cast'))
            
            temp_copy.resolveStack()
    
    def startChain(self):
        while not self.playersPassed():
            self.evaluateMoves()
            try:
                self.priority_player =  self.players[self.players.index(self.priority_player) + 1]
            except IndexError:
                self.priority_player = self.players[0]
        
        self.resolveStack()
        
        for player in self.players:
            player.last_action = None





test = Game([Player(20, 'burn.txt'), Player(20, 'burn.txt')])
                   