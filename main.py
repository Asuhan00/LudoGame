from cmath import rect
from tkinter import font
import pygame

#Intialize the pygame
pygame.init()

screen = pygame.display.set_mode((968,768))
pygame.display.set_caption("Ludo Game")
icon = pygame.image.load("Pic/icon.png")
pygame.display.set_icon(icon)

board_surface = pygame.image.load("Pic/board.png")
board_surface = pygame.transform.scale(board_surface,(768,768))
board_rect = board_surface.get_rect(topleft = (0,0))

font = pygame.font.Font("Font/Roboto-Regular.ttf",25)
dice_surface = font.render("Dice",False,"Black")
dice_rect = dice_surface.get_rect(midtop=(868,10))

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
    
    screen.fill("White")
    
    screen.blit(board_surface,board_rect)
    screen.blit(dice_surface,dice_rect)
    screen.blit(yellow_pawn1,yellow_pawn1_rect)
    pygame.display.update()
         
