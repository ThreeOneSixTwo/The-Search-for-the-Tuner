import pygame
from pygame.sprite import collide_rect


#General class for walls
class Geometry(pygame.sprite.Sprite):
    #Pos and scale are tuples!
    def __init__(self, asset, pos, scale):
        super().__init__()
        self.image = pygame.image.load(asset)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.scale = scale




#Child class for invisible walls specifically
class InvisibleWall(Geometry):
    pass