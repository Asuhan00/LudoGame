from cmath import rect
from tkinter import font
import pygame
import random
from game import Game

#Dice Roll function
def dice_roll():
    roll = random.randint(1,6)
    return roll

game = Game()

for player in game.player_turn_order:
    
    for pawn in player.pawn_list:
        print(player.name)
        print(pawn.color + " " + pawn.name)
       
#Intialize the pygame
pygame.init()

#Window Settings
screen = pygame.display.set_mode((968,768))
pygame.display.set_caption("Ludo Game")
icon = pygame.image.load("Pic/icon.png")
pygame.display.set_icon(icon)

#Board
board_surface = pygame.image.load("Pic/board.png")
board_surface = pygame.transform.scale(board_surface,(768,768))
board_rect = board_surface.get_rect(topleft = (0,0))


#Font
font = pygame.font.Font("Font/Roboto-Regular.ttf",25)
font_bold = font = pygame.font.Font("Font/Roboto-Bold.ttf",25)

#Turn Box
turn_surface = font_bold.render(game.color[game.turn]+"'s Turn",False,"Black")
turn_rect = turn_surface.get_rect(midtop=(868,10))

#Dice Box
dice_surface = font_bold.render("Dice",False,"Black")
dice_rect = dice_surface.get_rect(midtop=(868,turn_rect.bottom+10))
dice_roll_surface = font.render("0",False,"Black")
dice_roll_rect = dice_roll_surface.get_rect(midtop=(dice_rect.center[0],dice_rect.bottom +10))
dice_button_surface = font.render("  Roll  ",False,"Black")
dice_button_rect = dice_button_surface.get_rect(midtop=(dice_roll_rect.center[0],dice_roll_rect.bottom +5))



#End Turn Button
end_turn_button_surface = font.render(" End Turn ",False,"Black")
end_turn_button_rect = end_turn_button_surface.get_rect(midbottom=(868,758))

#Pawn 
yellow_pawn1 = pygame.image.load("Pic/Pawns/yellow_pawn.png")
yellow_pawn1 = pygame.transform.scale(yellow_pawn1,(42.5,42.5))
yellow_pawn1_rect = yellow_pawn1.get_rect(center = (65,640))


#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            print(pygame.mouse.get_pos())
            #Dice Roll Button Collision Detection
            if dice_button_rect.collidepoint(pygame.mouse.get_pos()) and not game.is_dice_rolled:
                game.dice_roll = dice_roll()
                game.is_dice_rolled = True
            #End Turn Button Collision  Detection
            if end_turn_button_rect.collidepoint(pygame.mouse.get_pos()):
                game.is_dice_rolled = False
                game.next_turn()


    #Background and board Update
    screen.fill("White")
    screen.blit(board_surface,board_rect)
    
    #Dice Box Update
    pygame.draw.rect(screen, "Black", pygame.Rect(768, dice_rect.top-10, 200,dice_button_rect.bottom+30-dice_rect.top),10)
    pygame.draw.line(screen,"Black",(768,dice_rect.bottom+5),(968,dice_rect.bottom+5))
    screen.blit(dice_surface,dice_rect)
    dice_roll_surface = font.render(str(game.dice_roll),False,"Black")
    screen.blit(dice_roll_surface,dice_roll_rect)
    screen.blit(dice_button_surface,dice_button_rect)
    pygame.draw.rect(screen, "Black", dice_button_rect,1)
    
    #Turn
    pygame.draw.rect(screen,"Black",pygame.Rect(768,turn_rect.top-10,200,turn_rect.bottom+20-turn_rect.top),10)
    turn_surface = font_bold.render(game.color[game.turn]+"'s Turn",False,"Black")
    screen.blit(turn_surface,turn_rect)

    #End Turn Button
    screen.blit(end_turn_button_surface,end_turn_button_rect)
    pygame.draw.rect(screen,"Black",end_turn_button_rect,1)

    screen.blit(yellow_pawn1,yellow_pawn1_rect)
    pygame.display.update()
         
