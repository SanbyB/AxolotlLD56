import random
import pygame
from resources import *

AX_STATES = ["breathing", "dancing", "damaged"]

class Axolotl:
    def __init__(self) -> None:
        self.name = ""
        self.width, self.height = 200, 200
        self.x = SCREEN_WIDTH / 2 - self.width/2
        self.y = SCREEN_HEIGHT / 2 + 100
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.friction = 0.98
        self.state = AX_STATES[0]
        self.health = 100

    def update(self):
        self.randMove()
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
        self.ax = ax
        self.ay = ay
    
    def randMove(self):
        self.move((random.random() - 0.5)/2, (random.random() - 0.5)/2)


    def render(self, screen):
        if self.state == "breathing":
            AX_BREATHING.draw(screen, self.x, self.y, self.width, self.height)
            AX_BREATHING.update()

        #todo display name



