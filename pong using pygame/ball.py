######################################################################################################################################
######################### Made by: Ayman hamdy_32022056, Youssef Waleed_320220041, Hamed Daoud_320220057##############################
######################################################################################################################################

from shape import Shape
from math import sqrt
from colors import PURPLE, BLACK
import pygame
from math import fabs, sqrt


class Ball(Shape):
    def __init__(self, win, color,xcor=0, ycor=0, x_vel=4, y_vel=0, radius=12):
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.max_y_vel = 4
        self.radius = radius
        self.win = win
        self.color = color
        self.isOutOfScreen = True
        self.isslow= True
        self.wall_sound = pygame.mixer.Sound('wall.wav')
        super().__init__(xcor, ycor, color,x_vel)

    def erase(self):
        pygame.draw.circle(self.win, self.color, (self.xcor, self.ycor), self.radius)

    def isOutOfScreenRight(self, screen_width):
        
        return self.xcor+self.radius >= screen_width

    def isOutOfScreenLeft(self):
        
        return self.xcor-self.radius <= 0

    def reverse_direction(self):
        self.x_vel *= -1

    def recenter(self, screen_width, screen_height):
        self.xcor = screen_width/2
        self.ycor = screen_height/2

    def aim_to_player(self, player, dir):
        if (dir == "r"):
            self.y_vel = (fabs(self.velocity) * ((player.ycor+player.height/2) - self.ycor)) / sqrt(
                (((self.xcor - self.radius) - (player.xcor + player.width)) ** 2) + (((self.ycor) - (player.ycor + player.height/2)) ** 2))
            self.x_vel = -sqrt(fabs(self.velocity**2 - self.y_vel**2))
            
        elif (dir == 'l'):
            self.y_vel = (fabs(self.velocity) * ((player.ycor+player.height/2) - self.ycor)) / sqrt(
                (((self.xcor + self.radius) - (player.xcor)) ** 2) + (((self.ycor) - (player.ycor + player.height/2)) ** 2))
            self.x_vel = sqrt(fabs(self.velocity**2 - self.y_vel**2))

    def collide_wall(self, height):
        if self.ycor <= self.radius or self.ycor >= height-self.radius:
            if self.ycor - self.radius < 0:
                if self.y_vel < 0:
                    self.wall_sound.play()
                    self.y_vel*=-1 
            if self.ycor + self.radius > height :
                if self.y_vel > 0:
                    self.wall_sound.play()
                    self.y_vel*=-1
                    
    def is_colliding_with_right_player(self, player):
        return self.xcor + self.radius >= player.xcor and self.ycor + self.radius >= player.ycor and self.ycor - self.radius <= player.ycor + player.height
                    
    def is_colliding_with_left_player(self, player):
        return self.xcor - self.radius <= player.xcor + player.width and self.ycor + self.radius >= player.ycor and self.ycor - self.radius <= player.ycor + player.height
                    
    def is_going_right(self):
        return self.x_vel > 0
    
    def move_ball(self):
        self.xcor+=self.x_vel
        self.ycor+=self.y_vel
    
    def draw(self, color):
        pygame.draw.circle(self.win, color, (self.xcor,self.ycor), self.radius)
