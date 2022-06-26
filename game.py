from pawn import Pawn
from player import *

class Game:
    
    color = ["Blue","Red","Green","Yellow"]
    turn = 0
    is_dice_rolled=False
    dice_roll = 0
    player_turn_order = []
    
    def next_turn(self):
        if self.turn >=3:
            self.turn=0
        else:
            self.turn+=1
        
        