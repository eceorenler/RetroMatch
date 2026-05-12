#defines the tiles and their properties

import pygame
import settings

class Tile: #represent a single tile on the board

    def __init__(self, tileType, row, col):
        self.type = tileType
        self.row = row
        self.col = col

        self.isPopping = False
        self.popFrame = 0
        self.popDuration = settings.POP_ANIMATION_DURATION

        self.updatePosition() #pixel position of tile 

    def updatePosition(self): #calculate pixel position
        self.x = settings.GRID_X + self.col * (settings.TILE_SIZE + settings.SPACING)
        self.y = settings.GRID_Y + self.row * (settings.TILE_SIZE + settings.SPACING)
        self.rect = pygame.Rect(self.x, self.y, settings.TILE_SIZE, settings.TILE_SIZE) #hitbox forclicks

    def startPop(self): #starts the pop animation when a match is found
        self.isPopping = True
        self.popFrame = 0

    def update(self):
        if self.isPopping: #advance the pop animation frame by frame
            self.popFrame += 1

    def isFinished(self):
        return self.popFrame >= self.popDuration #check if the pop animation is finished

    def draw(self, screen, image): #draw the tile on the screen with pop animation if active
        if self.isPopping:
            progress = self.popFrame / self.popDuration #calculate animation progress
            size = int(settings.TILE_SIZE * (1 - progress)) #calculate size for shrinking effect

            if size > 0: 
                small = pygame.transform.scale(image, (size, size))
                offset = (settings.TILE_SIZE - size) // 2 #calculates offset to keep the tile at center
                screen.blit(small, (self.x + offset, self.y + offset))
        else:
            screen.blit(image, (self.x, self.y)) #draw the tile normal if not popping