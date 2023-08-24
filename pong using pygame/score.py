######################################################################################################################################
######################### Made by: Ayman hamdy_32022056, Youssef Waleed_320220041, Hamed Daoud_320220057##############################
######################################################################################################################################

import pygame
import colors
class Score:
    def __init__(self, win ,player1_score=0,player2_score=0):
        self.player1_score = player1_score
        self.player2_score = player2_score
        self.win = win 
        
    def print_score(self, screen_width,color):
        font = pygame.font.Font("Pixeltype.ttf", 50)
        player1_score = font.render(str(self.player1_score), True, color)
        player2_score = font.render(str(self.player2_score), True, color)
        self.win.blit(player2_score,(screen_width/2 - 100 - 50, 13))
        self.win.blit(player1_score,(screen_width/2 + 100, 13))
        