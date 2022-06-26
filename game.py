from Python.Ludo_Game.pawn import Pawn
from player import *

class Game:
    def __init__(self,player_turn_order = []):
        self.player_turn_order = player_turn_order