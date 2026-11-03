import pygame

#from camera import camera


#A class that contains an entire world, and handles movement of all objects therein
#If
class MovingScene():

    def __init__(self, focusX, focusY, backgroundSource, maxX, maxY, screenMaxX, screenMaxY, cam):
        #self.camera = Camera.__init__()
        self.focusX = focusX
        self.focusY = focusY
        self.maxX = maxX
        self.maxY = maxY
        self.minX = 0
        self.minY = 0
        self.screenMaxX = screenMaxX
        self.screenMaxY = screenMaxY
        self.camera = cam
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

    def moveCamera(self, direction):
        self.camera = self.camera[0] + direction[0], self.camera[1] - direction[1]

    def teleportCamera(self, absCoords):
        self.camera = absCoords

    def updateScreenLocations(self):
        for entity in self.entities:
            pass
        for geometry in self.geometry:
            pass
        self.player.x = self.player.absCoords[0] + self.camera[0]
        self.player.y = self.player.absCoords[1] + self.camera[1]
        print(self.camera)
        self.focusX = -self.camera[0]
        self.focusY = -self.camera[1]

    #This one teleports the player to coordinates on the screen, and moves the scene to any location
    #Surely I'll test is someday
    def teleportPlayer(self, focusX, focusY, absX, absY):
        self.focusX = focusX
        self.focusY = focusY
        self.player.rect.center.x = absX
        self.player.rect.center.y = absY

    #This one teleports the player to coordinates on the scene
    def teleportPlayer(self, absX, absY):
        self.player.rect.x = self.screenMaxX/2
        self.player.rect.y = self.screenMaxY/2
        self.focusX = absX + self.screenMaxX/2 - (self.player.rect.left - self.player.rect.right)/2
        self.focusY = absY + self.screenMaxY/2 - (self.player.rect.top - self.player.rect.bottom)/2




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
                self.moveCamera((-speed, 0))
                #self.focusX += speed

        #self.player.updateSpriteOnMovement()

        #Right Movement
        if (inputs[pygame.K_RIGHT] == True ):
            #If the right side of the player is not in contact with the edge of screen

            if(self.player.rect.right < self.screenMaxX):
                self.player.rect.x += speed
            # If the right side of the background image is not too far

            elif(-self.focusX + self.screenMaxX < self.maxX ):
                self.moveCamera((speed, 0))

                #self.focusX -= speed

        #self.player.updateSpriteOnMovement()

        #Upward Movement
        if(inputs[pygame.K_UP] == True ):
            if(self.player.rect.top > self.minY):
                self.player.rect.y -= speed
            elif(self.focusY < self.minY):
                self.moveCamera((0, speed))

                #self.focusY += speed

        #self.player.updateSpriteOnMovement()

        #Downward Movement
        if(inputs[pygame.K_DOWN] == True ):
            if(self.player.rect.bottom < self.screenMaxY):
                self.player.rect.y += speed


            elif (-self.focusY + self.screenMaxY < self.maxY ):
                self.moveCamera((0, -speed))
                #self.focusY -= speed

        #self.player.updateSpriteOnMovement()
        self.updateScreenLocations()


