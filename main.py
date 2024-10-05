import pygame, sys
from pygame.locals import *
from resources import *
from view import View
from axolotl import Axolotl


class Game:
    def __init__(self):
        self.hasDied = False
        self.highScore = 0
        self.reset()
        

    def reset(self):
        self.score = 0
        self.money = 0
        self.view = View()
        self.step = 0
        self.axolotls = [Axolotl()]
        

    def update(self):
        self.score = len(self.axolotls)

        keys = pygame.key.get_pressed()
        if not self.hasStarted:
            if keys[pygame.K_RETURN]:
                self.step += 1

        if self.hasDied:
            if keys[pygame.K_RETURN]:
                self.reset()
                self.hasDied = False

    def introText(self):
        pass

    def displayScore(self):
        #todo: display self.score, and self.money
        pass


    def render(self, DISPLAYSURF):
        self.view.render(DISPLAYSURF)

    def onPlayerDead(self):
        self.hasDied = True
        self.highScore = max(self.score, self.highScore)


game = Game()

pygame.init()
pygame.mixer.init()

# audio.playMusic()

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Axolotl Scantuary')
pygame.display.set_icon(IMAGE_AX)

clock = pygame.time.Clock()

while True: # main game loop
    dt = clock.tick(60)
    # Clear the screen
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    game.update()
    game.render(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()