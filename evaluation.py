from game import Game
from phases import Phases

import copy

class Evaluation:
    def __init__(self) -> None:
        pass

    def evaluateMoves(self, game: Game):
        if game.phase != Phases.PRE_COMBAT_MAIN_PHASE and game.phase != Phases.POST_COMBAT_MAIN_PHASE:
            legal_moves = game.getLegalMoves('fast', game.priority_player)
        
        for move in legal_moves:
            temp_copy = copy.deepcopy(game)
            temp_copy.makeMove(move)
