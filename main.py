from player import Player
from game import Game
from deck import Deck

if __name__ == "__main__":
    game = Game(Player(20, Deck('burn.txt')))
