######################################################################################################################################
######################### Made by: Ayman hamdy_32022056, Youssef Waleed_320220041, Hamed Daoud_320220057##############################
######################################################################################################################################

from shape import Shape
import colors
import pygame
from screen import Screen
class Stick(Shape):
    def __init__(self, win, xcor, ycor, color, width=15, height=150,real_velocity=5):
        self.width = width
        self.height = height
        self.win = win
        self.score = 0 
        self.color = color
        super().__init__(xcor, ycor, self.color, real_velocity)
    
    def is_on_upper_edge(self,screen_height):
        return self.ycor <= 0 
    
    def is_on_lower_edge(self,screen_height):
        return self.ycor > screen_height - self.height
    
    def erase(self):
        pygame.draw.rect(self.win, self.color,(self.xcor, self.ycor, self.width, self.height))
        
    def move_up(self):
        self.ycor -= self.velocity
    
    def move_down(self):
        self.ycor += self.velocity
        
    def recenter(self,screen_height):
        self.erase()
        self.ycor = screen_height/2 - self.height/2 
        
    def draw(self,color):
          pygame.draw.rect(self.win,color,(self.xcor,self.ycor,self.width,self.height))