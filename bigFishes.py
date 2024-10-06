import random
import pygame
from resources import *

FISH_STATES = ["breathing", "attacking"]

class BigFish:
    def __init__(self) -> None:
        self.width, self.height = 200, 200
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.friction = 0.98
        self.state = FISH_STATES[1]
        self.range = 100
        self.damage = 1

    def update(self, target):
        self.attack(target)
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        self.vy += self.ay
        self.vx *= self.friction
        self.vy *= self.friction
        if self.x < 0:
            self.vx = abs(self.vx)
        if self.x > SCREEN_WIDTH - self.width:
            self.vx = -abs(self.vx)
        if self.y < 0:
            self.vy = abs(self.vy)
        if self.y > SCREEN_HEIGHT - self.height:
            self.vy = -abs(self.vy)
    
    def move(self, ax, ay):
        print("move towards " + str(ax) + ", " + str(ay))
        self.ax = ax
        self.ay = ay

    def attack(self, target):
        # if in range damage target
        if (target.x + target.width/2) - (self.x + self.width/2) < self.range:
            if (target.y + target.height/2) - (self.y + self.height/2) < self.range:
                target.health -= self.damage
        self.move(((target.x + target.width/2) - (self.x + self.width/2))/1000, ((target.y + target.height/2) - (self.y + self.height/2))/1000)
    
    def randMove(self):
        self.move((random.random() - 0.5)/2, (random.random() - 0.5)/2)


    def render(self, screen):
        if self.state == "attacking":
            BIG_FISH_ATTACKING.draw(screen, self.x, self.y, self.width, self.height)
            BIG_FISH_ATTACKING.update()

        #todo display name



