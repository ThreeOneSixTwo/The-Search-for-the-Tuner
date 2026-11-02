import pygame
from enum import Enum
class playerStates(Enum):
    STANDING = 0
    MOVING = 1
    ATTACKING = 2


class Player(pygame.sprite.Sprite):





    def __init__(self, x, y, asset):

        super().__init__()
        self.image = pygame.image.load(asset)
        self.rect = self.image.get_rect()
        #self.rect.center = (x, y)
        self.absCoords = (x, y)
        self.state = playerStates.STANDING
        self.frameCount = 0
        self.frameRollover = 60

    def makeTunerPlayer(self):
        T1 = Player(800,600, "Assets/Tuner.png")
        return T1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.frameCount += 1
        if(self.frameCount >= self.frameRollover):
            self.frameCount = 0

    def place(self, x, y):
        self.rect.center = (x, y)

    def updateSpriteOnMovement(self):
        pass


def makeTunerPlayer():
    T1 = Player(800, 600, "Assets/Tuner.png")
    return T1
