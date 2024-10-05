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
        self.text = ""
        self.score = 0
        self.money = 0
        self.view = View()
        self.step = 0
        self.axolotls = []
        

    def update(self):
        self.introSequence()
        self.score = len(self.axolotls)

        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.step < 4:
                self.step += 1
            keydown = True
            while keydown:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            keydown = False

        if self.hasDied:
            if keys[pygame.K_RETURN]:
                self.reset()
                self.hasDied = False

    def clickAxolotl(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0] == 1:
            mp = pygame.mouse.get_pos()
            if self.axolotls[0].x < mp[0] < self.axolotls[0].x + self.axolotls[0].width:
                if self.axolotls[0].y < mp[1] < self.axolotls[0].y + self.axolotls[0].height:
                    self.step += 1

    def fishAttack(self):
        #run attack sequence at start
        pass

    def clickFish(self):
        #click the fish to stop it eating the axolotl
        pass

    def introSequence(self):
        s = self.step
        if s == 0:
            self.text = "Welcome to Mexico City"
        elif s == 1:
            self.text = "Mexico City is home to a\nlake called \"Lake Xochimilco\""
        elif s == 2:
            self.text = "This lake is the last remaining\nnatural habitat of the Axolotl"
        elif s == 3:
            self.text = "It is your task to capture\nand raise these Axolotls,\nprotecting them from extinction"
        elif s == 4:
            self.axolotls.append(Axolotl())
            self.text = "Quick there’s one now!"
            # screen blit here so it shows text and axolotl
            self.clickAxolotl()
        elif s == 5:
            # self.text = "Now that you have your first Axolotl, you need to give them a name"
            # keys = pygame.key.get_pressed()

            # if keys[pygame.K_RETURN]:
            self.text = "Now let's take our new Axolotl friend home"
            self.view.moveToPond()
            self.fishAttack()
        elif s == 6:
            self.text = "Watch out!  a large fish is coming"
        elif s == 7:
            self.text = "You need to protect [name] from predators"
        elif s == 8:
            self.text = "Scare off the larger fish by clicking on them"
            self.clickFish()

        
        

    def displayScore(self):
        #todo: display self.score, and self.money
        pass


    def render(self, DISPLAYSURF):
        self.view.render(DISPLAYSURF)
        if self.text != "":
            text = self.text.split("\n")
            newline = 0
            for t in text:
                # img = SMALLER_FONT.render(t, True, (95, 205, 228))
                img = FONT.render(t, True, (95, 205, 228))
                rect = pygame.Rect(SCREEN_WIDTH/2 - img.get_width()/2, SCREEN_HEIGHT/2 - img.get_height()/2 + img.get_height() * newline, img.get_width(), img.get_height())
                shape_surf = pygame.Surface(rect.size, pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, (0,0,0,180), shape_surf.get_rect())
                DISPLAYSURF.blit(shape_surf, rect)
                DISPLAYSURF.blit(img, (SCREEN_WIDTH/2 - img.get_width()/2, SCREEN_HEIGHT/2 - img.get_height()/2 + img.get_height() * newline))
                newline += 1
        for ax in self.axolotls:
            ax.render(DISPLAYSURF)

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
    # pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    game.update()
    game.render(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()