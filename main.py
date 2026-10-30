import pygame
from sys import exit
import movingScene
import Player
import math
import time


white = (255, 255, 255)
TOP_EDGE = 0
BOTTM_EDGE = 1000
LEFT_EDGE = 0
RIGHT_EDGE = 1200


black = 0, 0, 0


from pygame import event, camera


def runGame():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        textSurface = font.render(str(currentScene.focusX) + ' ' + str(currentScene.focusY), False, white)
        screen.fill(black)
        currentScene.draw(screen)
        currentScene.movePlayer(pygame.key.get_pressed(), 20)

        if(pygame.key.get_pressed()[pygame.K_t] == True):
            currentScene.teleportPlayer(0,0)




        pygame.display.update()
        clock.tick(60)



'''class Tuner(pygame.sprite.Sprite):
    def __init__(self, x, y):

        super().__init__()
        self.image = pygame.image.load("Tuner.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def factoryMethod():
        T1 = Tuner(800,600)
        return T1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def place(self, x, y):
        self.rect.center = (x, y)

    def move(self, key, background):
        global backgroundFocalX, backgroundFocalY
        if(key[pygame.K_a] == True  ):
            if(self.rect.left > LEFT_EDGE):
                self.rect.x -= 10
            else:
                backgroundFocalX += 10
        if (key[pygame.K_d] == True ):
            if(self.rect.right < RIGHT_EDGE):
                self.rect.x += 10
            else:
                backgroundFocalX -= 10
        if(key[pygame.K_w] == True ):
            if(self.rect.top > TOP_EDGE):
                self.rect.y -= 10
            else:
                backgroundFocalY += 10
        if(key[pygame.K_s] == True ):
            if(self.rect.bottom < BOTTM_EDGE):
                self.rect.y += 10
            else:
                backgroundFocalY-= 10


    def calcAngle(self, freq, aStandard):
        cents = 1200*math.log(freq/aStandard, 2)
        angle = cents%60 + 60
        return angle'''

'''
calculusSurface = Tuner.factoryMethod()
background = pygame.image.load("Assets/Screenshot_2025-12-24_13-10-57.png")
background = pygame.transform.scale(background, (5000, 5000))
'''
pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((RIGHT_EDGE, BOTTM_EDGE))
font = pygame.font.Font(None, 50)
textSurface = font.render("Calculus", True, (0, 0, 0))

pygame.display.set_caption("The Search for the Tuner")
pygame.display.set_icon(pygame.image.load("Assets/Tuner.png"))

#Fair use!!!!!!!!!!!!!11
currentScene = movingScene.MovingScene(0,0, "Assets/Screenshot_2025-12-24_13-10-57.png", 5000, 5000, RIGHT_EDGE, BOTTM_EDGE)
currentScene.setPlayer(Player.makeTunerPlayer())
runGame()



