######################################################################################################################################
######################### Made by: Ayman hamdy_32022056, Youssef Waleed_320220041, Hamed Daoud_320220057##############################
######################################################################################################################################

import os
import pygame
import random
import time
from math import fabs , sqrt
from ball import Ball
from stick import Stick
from screen import Screen
from score import Score
import colors
from colors import color_list, color_names

class Game: 
    waitTime = 5

    def __init__(self):
        
        pygame.init()
        pygame.display.set_caption("collisions")
        self.idx1 = 3
        self.idx2 = 1
        self.miscellaneous = color_list[self.idx1]
        self.screen_color = color_list[self.idx2]
        self.main_screen = Screen()
        self.win = pygame.display.set_mode((self.main_screen.width, self.main_screen.height))
        self.win.fill(self.screen_color)
        self.paddle_sound = pygame.mixer.Sound('paddle.wav')
        self.button_sound = pygame.mixer.Sound('button.wav')
        self.goal_sound = pygame.mixer.Sound('goal.wav')
        self.end_game = pygame.mixer.Sound('end-game.wav')
        
        self.player1 = Stick(self.win,self.main_screen.width-30, self.main_screen.height/2 - Stick(self.win,None,None,self.miscellaneous).height/2,self.miscellaneous)
        self.player2 = Stick(self.win,15, self.main_screen.height/2 - Stick(self.win,None,None,self.miscellaneous).height/2,self.miscellaneous)

        self.ball = Ball(self.win, self.miscellaneous,self.main_screen.width/2, self.main_screen.height/2)
        self.board = Score(self.win)
        self.menu = True

    def wait(self):
        pygame.time.delay(self.waitTime)
    
    def shouldQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
            if self.menu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(pygame.mouse.get_pos()):
                        self.button_sound.play()
                        self.menu = False
                        self.board.player1_score = 0
                        self.board.player2_score = 0
                        self.player1.recenter(self.main_screen.height)
                        self.player2.recenter(self.main_screen.height)
                        self.ball.recenter(self.main_screen.width,self.main_screen.height)
                        self.ball.aim_to_player(self.player1, dir="l")
                    if self.quit_rect.collidepoint(pygame.mouse.get_pos()):
                        self.button_sound.play()
                        pygame.quit()
                        exit()
                    if self.color_rect.collidepoint(pygame.mouse.get_pos()):
                        self.button_sound.play()
                        self.idx1 += 1
                        if self.idx1 == self.idx2:
                            self.idx1+=1
                        if self.idx1 >= len(color_list):
                            self.idx1 = 0
                        
                    if self.color_rect2.collidepoint(pygame.mouse.get_pos()):
                        self.button_sound.play()
                        self.idx2 += 1
                        if self.idx1 == self.idx2:
                            self.idx2+=1
                        if self.idx2 >= len(color_list):
                            self.idx2 = 0
                        
                        
                    
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                if self.menu == False:
                    self.button_sound.play()
                if not self.ball.isslow:
                        self.ball.x_vel/=2
                        self.ball.velocity/=2
                        self.ball.isslow = True
                self.menu = True
                
        
            
    
    def play(self):
        while True:
            
            self.wait()
            self.shouldQuit()
            
            self.miscellaneous = color_list[self.idx1]
            self.screen_color = color_list[self.idx2]
            
            if not self.menu:
                # self.ball.erase()     
                
                if self.ball.isOutOfScreenRight(self.main_screen.width):
                    self.goal_sound.play()
                    if not self.ball.isslow:
                        self.ball.x_vel/=2
                        self.ball.velocity/=2
                        self.ball.isslow = True
                    
                    self.ball.reverse_direction()
                    self.ball.recenter(self.main_screen.width, self.main_screen.height)
                    self.ball.aim_to_player(self.player1, dir="l")
                    self.ball.isOutOfScreen = True
                    self.board.player2_score += 1
                    
                if self.ball.isOutOfScreenLeft():
                    self.goal_sound.play()
                    if not self.ball.isslow:
                        self.ball.x_vel/=2
                        self.ball.velocity/=2
                        self.ball.isslow = True
                    
                    self.ball.reverse_direction()
                    self.ball.recenter(self.main_screen.width, self.main_screen.height)
                    self.ball.aim_to_player(self.player2, dir="r")
                    self.ball.isOutOfScreen = True
                    self.board.player1_score += 1


                self.ball.collide_wall(self.main_screen.height)
                
                
                if self.ball.is_colliding_with_right_player(self.player1):
                    
                    if self.ball.isslow:
                        self.ball.x_vel*=2
                        self.ball.velocity*=2
                        self.ball.isslow = False
                        
                    if self.ball.is_going_right() > 0:
                        self.paddle_sound.play()
                        self.ball.x_vel *=-1
                    space_from_cinter = self.ball.ycor-fabs(self.player1.ycor + self.player1.height/2)

                    self.ball.y_vel = space_from_cinter * (self.ball.max_y_vel / ( (self.player1.height+self.ball.radius) / 2) )
                    self.ball.x_vel = -sqrt(fabs(self.ball.velocity**2 - self.ball.y_vel**2))
                    
                if self.ball.is_colliding_with_left_player(self.player2):
                    
                    if self.ball.isslow:
                        self.ball.x_vel*=2
                        self.ball.velocity*=2
                        self.ball.isslow = False
                        
                    if not self.ball.is_going_right():
                        self.paddle_sound.play()
                        self.ball.x_vel *=-1
                    space_from_cinter = self.ball.ycor-fabs(self.player2.ycor + self.player2.height/2)
                    
                    self.ball.y_vel = space_from_cinter * (self.ball.max_y_vel / ( (self.player2.height+self.ball.radius) / 2) )
                    self.ball.x_vel = sqrt(fabs(self.ball.velocity**2 - self.ball.y_vel**2))
                        
                
                key = pygame.key.get_pressed()
                
                if key[pygame.K_UP] and not self.player1.is_on_upper_edge(self.main_screen.height):
                    self.player1.erase()
                    self.player1.move_up()
                if key[pygame.K_DOWN] and not self.player1.is_on_lower_edge(self.main_screen.height):
                    self.player1.erase()
                    self.player1.move_down()
                    
                if key[pygame.K_w] and (not self.player2.is_on_upper_edge(self.main_screen.height)):
                    self.player2.erase()
                    self.player2.move_up()
                if key[pygame.K_s] and (not self.player2.is_on_lower_edge(self.main_screen.height)):
                    self.player2.erase()
                    self.player2.move_down()
                
                    
                
                
                
                
                if self.board.player1_score == 10 or self.board.player2_score == 10:
                    self.end_game.play()
                    self.menu = True
                    
                self.ball.move_ball()

                
                
                self.win.fill(self.screen_color)
                
                self.board.print_score(self.main_screen.width,self.miscellaneous)
                
                self.player1.draw(self.miscellaneous)
                self.player2.draw(self.miscellaneous)
                
                self.ball.draw(self.miscellaneous)
                
                
                # if self.ball.isOutOfScreen:
                #     # pygame.time.delay(500)
                #     self.ball.isOutOfScreen = False
                    

            if self.menu:
                self.win.fill(self.screen_color)
                
                font = pygame.font.Font("Pixeltype.ttf", 70)
                font2 = pygame.font.Font("Pixeltype.ttf", 30)
                font3 = pygame.font.Font( "Pixeltype.ttf" ,30)
                key = pygame.key.get_pressed()
                
                
                #menu
                middle_x = self.main_screen.width / 2
                middle_y = self.main_screen.height / 2
                title = font.render("Welcome to Pong",False ,self.miscellaneous)
                tit_rect = title.get_rect(center=(middle_x,middle_y - 200))
                
                #start quit and color buttons
                
                #start
                start = font.render("Start", False, self.miscellaneous)
                self.start_rect = start.get_rect(center=(middle_x - 200, middle_y + 100))
                
                #quit
                quit = font.render("Quit", False,self.miscellaneous)
                self.quit_rect = quit.get_rect(center=(middle_x + 200, middle_y + 100))
                
                #controls
                controls = font.render("Controls", False, self.miscellaneous)
                text = "left player: w, s"
                player1_controls = font2.render(text, True,self.miscellaneous)
                text = "right player: up, down"
                player2_controls = font2.render(text, True,self.miscellaneous)
                self.controls_rect = controls.get_rect(center=(middle_x, middle_y + 150))
                self.player1_controls_rect = player1_controls.get_rect(center = (middle_x, middle_y + 200))
                self.player2_controls_rect = player2_controls.get_rect(center = (middle_x, middle_y + 225))
                
                #colors
                miscellaneous_color = font2.render(f"miscellaneous color: {color_names[self.idx1]}   (press to change)", False, self.miscellaneous)
                self.color_rect = miscellaneous_color.get_rect(midleft=(middle_x - 530, middle_y + 250))
                screen_color = font2.render(f"background color: {color_names[self.idx2]}    (press to change)", False, self.miscellaneous)
                self.color_rect2 = screen_color.get_rect(midleft=(middle_x - 530,middle_y + 300))
                    
                #winner
                if self.board.player1_score or self.board.player2_score:
                    
                    self.result = font.render(f"{self.board.player2_score}      :      {self.board.player1_score}" ,False,self.miscellaneous)
                    
                    if self.board.player1_score > self.board.player2_score:
                        self.winner = font.render(f"the winner is the right player" ,False,self.miscellaneous)
                        
                    elif self.board.player1_score < self.board.player2_score:
                        self.winner = font.render(f"the winner is the left player" ,False,self.miscellaneous)
                    
                    else:
                        self.winner = font.render(f"it's a tie" ,False,self.miscellaneous)
                    
                    result_rect = self.result.get_rect(center = (middle_x,middle_y + 30))
                    self.win.blit(self.result,result_rect)
                    winner_rect = self.winner.get_rect(center = (middle_x,middle_y - 50))
                    self.win.blit(self.winner,winner_rect)
                #drawing
                
                credit = font3.render("Made by: Ayman Hamdy_320220056, Youssef Arafa_320220041, Hamed Daoud_320220057",False ,self.miscellaneous)
                credit_rect = credit.get_rect(center=(middle_x,self.main_screen.height-20))
                self.win.blit(credit, credit_rect)
                self.win.blit(quit,self.quit_rect)
                self.win.blit(quit,self.quit_rect)
                self.win.blit(start,self.start_rect)
                self.win.blit(controls,self.controls_rect)
                self.win.blit(title, tit_rect)
                self.win.blit(miscellaneous_color, self.color_rect)
                self.win.blit(screen_color,self.color_rect2)
                if self.controls_rect.collidepoint(pygame.mouse.get_pos()):
                    self.win.blit(player1_controls,self.player1_controls_rect)
                    self.win.blit(player2_controls,self.player2_controls_rect)
                    
                
            # pygame.display.update()
            pygame.display.update()  
            