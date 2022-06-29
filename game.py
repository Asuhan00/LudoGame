from pawn import Pawn
from player import *

class Game:
    
    color = ["Blue","Red","Green","Yellow"]
    turn = 0
    is_dice_rolled=False
    dice_roll = 0
    player_turn_order = []
    
    def __init__(self,player_number=4):
        if player_number == 2:
            self.player1 = Player("Player 1","Blue",Pawn("pawn1","Blue"),Pawn("pawn2","Blue"),Pawn("pawn3","Blue"),Pawn("pawn4","Blue"))
            self.player2 = Player("Player 2","Red",Pawn("pawn1","Red"),Pawn("pawn2","Red"),Pawn("pawn3","Red"),Pawn("pawn4","Red"))
            self.player_turn_order.append(self.player1)
            self.player_turn_order.append(self.player2)
        if player_number == 3:
            self.player1 = Player("Player 1","Blue",Pawn("pawn1","Blue"),Pawn("pawn2","Blue"),Pawn("pawn3","Blue"),Pawn("pawn4","Blue"))
            self.player2 = Player("Player 2","Red",Pawn("pawn1","Red"),Pawn("pawn2","Red"),Pawn("pawn3","Red"),Pawn("pawn4","Red"))
            self.player3 = Player("Player 3","Green",Pawn("pawn1","Green"),Pawn("pawn2","Green"),Pawn("pawn3","Green"),Pawn("pawn4","Green"))
            self.player_turn_order.append(self.player1)
            self.player_turn_order.append(self.player2)
            self.player_turn_order.append(self.player3)
        if player_number == 4:
            self.player1 = Player("Player 1","Blue",Pawn("pawn1","Blue"),Pawn("pawn2","Blue"),Pawn("pawn3","Blue"),Pawn("pawn4","Blue"))
            self.player2 = Player("Player 2","Red",Pawn("pawn1","Red"),Pawn("pawn2","Red"),Pawn("pawn3","Red"),Pawn("pawn4","Red"))
            self.player3 = Player("Player 3","Green",Pawn("pawn1","Green"),Pawn("pawn2","Green"),Pawn("pawn3","Green"),Pawn("pawn4","Green"))
            self.player4 = Player("Player 4","Yellow",Pawn("pawn1","Yellow"),Pawn("pawn2","Yellow"),Pawn("pawn3","Yellow"),Pawn("pawn4","Yellow"))
            self.player_turn_order.append(self.player1)
            self.player_turn_order.append(self.player2)
            self.player_turn_order.append(self.player3)
            self.player_turn_order.append(self.player4)



    def next_turn(self):
        if self.turn >=3:
            self.turn=0
        else:
            self.turn+=1
        
        