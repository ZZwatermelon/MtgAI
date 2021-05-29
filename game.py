from random import random
from player import Player
from phases import Phases

import random

class Game():
    def __init__(self, players):
        self.players = players
        self.active_player = players[random.randint(0, len(players)-1)]

        self.stack = []
        self.battlefield = []
        self.exile = []

        self.phase = Phases.BEGINNING_PHASE
    
    def turn(self, player):
        self.active_player = player

