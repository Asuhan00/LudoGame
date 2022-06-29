from pawn import Pawn
from player import *

class Game:
    
    color = ["Blue","Red","Green","Yellow"]
    turn_index = 0
    is_dice_rolled=False
    dice_roll = 0
    player_turn_order = []
    
    def __init__(self,player_count):
        self.player_count = player_count
    

    def next_turn(self):
        if self.turn_index >=3:
            self.turn_index=0
        else:
            self.turn_index+=1
        
        