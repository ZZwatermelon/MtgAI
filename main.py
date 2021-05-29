from player import Player
from game import Game

if __name__ == "__main__":
    game = Game([Player(20, 'burn.txt'), Player(20, 'burn.txt')])
    for card in game.players[0].hand:
        print(card.name)
    
