from pawn import Pawn
from player import *

class Game:
    
    def __init__(self,dice_roll = 0,player_turn_order = [],is_dice_rolled=False):
        self.player_turn_order = player_turn_order
        self.dice_roll = dice_roll
        self.is_dice_rolled = is_dice_rolled