import pygame

#A class that contains an entire world, and handles movement of all objects therein
class MovingScene():

    def __init__(self, focusX, focusY, backgroundSource, maxX, maxY, screenMaxX, screenMaxY):
        self.focusX = focusX
        self.focusY = focusY
        self.maxX = maxX
        self.maxY = maxY
        self.minX = 0
        self.minY = 0
        self.screenMaxX = screenMaxX
        self.screenMaxY = screenMaxY
        self.backgroundSource = backgroundSource
        self.background = pygame.image.load(self.backgroundSource)
        self.background = pygame.transform.scale(self.background, (self.maxX, self.maxY))
        self.entities = []
        self.player = 0#Totally cool player
        self.geometry = []

    #This draws everything in the scene
    def draw(self, screen):
        screen.blit(self.background, (self.focusX, self.focusY))

        for geometry in self.geometry:
            geometry.draw(screen)
        for entity in self.entities:
            entity.draw(screen)
        self.player.draw(screen)
    #This method must be called or things will break!
    def setPlayer(self, player):
        self.player = player

    def addGeometry(self, geometry):
        self.geometry.append(geometry)
    def removeGeometry(self, geometry):
        self.geometry.remove(geometry)
    def addEntity(self, entity):
        self.entities.append(entity)
    def removeEntity(self, entity):
        self.entities.remove(entity)
    def moveAllSprites(self):
        for wall in self.geometry:
            pass
        for entity in self.entities:
            pass

    def getPlayerAbsCoords(self):
        return self.player.rect.center[0] - self.focusX, self.player.rect.center[1] - self.focusY

    def teleportPlayer(self, focusX, focusY, absX, absY):
        self.focusX = focusX
        self.focusY = focusY
        self.player.rect.center.x = absX
        self.player.rect.center.y = absY

    def teleportPlayer(self, absX, absY):
        self.player.rect.x = self.screenMaxX/2
        self.player.rect.y = self.screenMaxY/2
        self.focusX = absX + self.screenMaxX/2 - self.player.rect.
        self.focusY = absY + self.screenMaxY/2 #- self.player.rect.center[1]


#I know it's weird, but having the scene handling movement should work well
    # since player movement is very deeply connected to background movement, it makes sense for it to handle it


    def movePlayer(self, inputs, speed):

        #Left Movement
        if(inputs[pygame.K_LEFT] == True  ):
            #If the left side of the player is not in contact with the edge of screen
            if(self.player.rect.left > self.minX):
                self.player.rect.x -= speed
            #If the top left side of the background image is not too far
            elif(self.focusX < self.minX):
                self.focusX += speed

        self.player.updateSpriteOnMovement()

        #Right Movement
        if (inputs[pygame.K_RIGHT] == True ):
            #If the right side of the player is not in contact with the edge of screen

            if(self.player.rect.right < self.screenMaxX):
                self.player.rect.x += speed
            # If the right side of the background image is not too far

            elif(-self.focusX + self.screenMaxX < self.maxX ):
                self.focusX -= speed

        self.player.updateSpriteOnMovement()

        #Upward Movement
        if(inputs[pygame.K_UP] == True ):
            if(self.player.rect.top > self.minY):
                self.player.rect.y -= speed
            elif(self.focusY < self.minY):
                self.focusY += speed

        self.player.updateSpriteOnMovement()

        #Downward Movement
        if(inputs[pygame.K_DOWN] == True ):
            if(self.player.rect.bottom < self.screenMaxY):
                self.player.rect.y += speed


            elif (-self.focusY + self.screenMaxY < self.maxY ):
                self.focusY -= speed

        self.player.updateSpriteOnMovement()
        self.moveAllSprites()
