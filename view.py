from resources import *

class View:
    def __init__(self) -> None:
        self.backgrounds = [IMAGE_MEXICO, IMAGE_POND, STORE_SHEET]
        self.view = self.backgrounds[0]
    
    def moveToMexico(self):
        self.view = self.backgrounds[0]
    
    def moveToPond(self):
        self.view = self.backgrounds[1]
    
    def moveToStore(self):
        self.view = self.backgrounds[2]
    
    def render(self, screen):
        if self.view == STORE_SHEET:
            STORE_SHEET.update()
        scaledImage = pygame.transform.scale(self.view, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaledImage, (0,0))