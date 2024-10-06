import os.path
import pygame
from spritesheet import SpriteSheet
from animation import Animation

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 650, 650

IMAGE_AX = pygame.image.load(os.path.join("Graphics", "ax.png"))

IMAGE_BACK = pygame.image.load(os.path.join("Graphics", "backButton.png"))


IMAGE_MEXICO = pygame.image.load(os.path.join("Graphics", "mexico.png"))
IMAGE_POND = pygame.image.load(os.path.join("Graphics", "pond.png"))
IMAGE_STORE = SpriteSheet(pygame.image.load(os.path.join("Graphics", "storeMenu.png")), 6, 1)
IMAGE_GROUND = pygame.image.load(os.path.join("Graphics", "ground.png"))

STORE_SHEET = Animation(IMAGE_STORE, 0, 0)

FONT = pygame.font.Font(os.path.join("Graphics", "SparkyStonesRegular.ttf"), 44)
SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "SparkyStonesRegular.ttf"), 36)
EVEN_SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "SparkyStonesRegular.ttf"), 28)


AX_SHEET = SpriteSheet(pygame.image.load(os.path.join("Graphics", "axolotl1.png")), 4, 1)
AX_BREATHING = Animation(AX_SHEET, 0, 0.06)
# AX_DANCING = Animation(AX_SHEET, 1, 0.2)

BIG_FISH_SHEET = SpriteSheet(pygame.image.load(os.path.join("Graphics", "bigFish.png")), 4, 1)
BIG_FISH_ATTACKING = Animation(BIG_FISH_SHEET, 0, 0.06)

WORM_SHEET = SpriteSheet(pygame.image.load(os.path.join("Graphics", "worm.png")), 4, 1)
WORM_WIGGLE = Animation(WORM_SHEET, 0, 0.1)

BACKGROUND_VOLUME = 0
MAIN_VOLUME = 0.3

# SOUND_BIP = pygame.mixer.Sound(os.path.join("Audio", "bip.ogg"))
# SOUND_BIP.set_volume(MAIN_VOLUME)

# SOUND_SMOT = pygame.mixer.Sound(os.path.join("Audio", "smot.ogg"))
# SOUND_SMOT.set_volume(MAIN_VOLUME)

# SOUND_FOOTSTEP = pygame.mixer.Sound(os.path.join("Audio", "footstep.ogg"))
# SOUND_FOOTSTEP.set_volume(MAIN_VOLUME)

# SOUND_HIT = pygame.mixer.Sound(os.path.join("Audio", "bleurf.ogg"))
# SOUND_HIT.set_volume(MAIN_VOLUME)

# SOUND_HIT2 = pygame.mixer.Sound(os.path.join("Audio", "hit.ogg"))
# SOUND_HIT2.set_volume(MAIN_VOLUME)

# SOUND_HIT3 = pygame.mixer.Sound(os.path.join("Audio", "hit2.ogg"))
# SOUND_HIT3.set_volume(MAIN_VOLUME)

# SOUND_HIT4 = pygame.mixer.Sound(os.path.join("Audio", "hit3.ogg"))
# SOUND_HIT4.set_volume(MAIN_VOLUME)

# SOUND_POINT = pygame.mixer.Sound(os.path.join("Audio", "point.ogg"))
# SOUND_POINT.set_volume(MAIN_VOLUME)


# class Audio():
#     def playMusic(self):
#         return;
#         # pygame.mixer.music.load(os.path.join("Audio", "background2.ogg")) 
#         # pygame.mixer.music.set_volume(BACKGROUND_VOLUME)     
#         # pygame.mixer.music.play(-1,0.0)  

#     def onRockHit(self):
#         SOUND_SMOT.play()
    
#     def onRockBreak(self):
#         SOUND_SMOT.play()

#     def onOreHit(self):
#         SOUND_SMOT.play()
    
#     def onOreBreak(self):
#         SOUND_SMOT.play()
#         SOUND_POINT.play()
        
#     def onSlimeHit(self):
#         SOUND_HIT2.play()

#     def onSlimeDead(self):
#         SOUND_HIT.play()
    
#     def onPlayerHit(self):
#         SOUND_HIT2.play()

#     def onPlayerDead(self):
#         SOUND_HIT.play()

#     def onBuy(self):
#         SOUND_POINT.play()

#     def onStep(self):
#         SOUND_FOOTSTEP.play()

#     def onJump(self):
#         SOUND_FOOTSTEP.play()
    
#     def onDrop(self):
#         SOUND_FOOTSTEP.play()



# audio = Audio()

