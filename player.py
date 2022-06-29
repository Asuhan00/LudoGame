from pawn import Pawn

class Player:
    pawn_list = []

    def __init__(self,name,color,pawn1=Pawn("pawn1","color"),pawn2=Pawn("pawn2","color"),pawn3=Pawn("pawn3","color"),pawn4=Pawn("pawn1","color")):
        self.name = name
        self.color = color
        self.pawn1 = pawn1
        self.pawn2 = pawn2
        self.pawn3 = pawn3
        self.pawn4 = pawn4
        self.pawn_list.append(self.pawn1)
        self.pawn_list.append(self.pawn2)
        self.pawn_list.append(self.pawn3)
        self.pawn_list.append(self.pawn4)


