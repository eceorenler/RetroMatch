import pygame
import settings

class Tile:
    def __init__(self, tileType, row, col):
        self.type = tileType
        self.row = row
        self.col = col
        self.updatePosition()

    def updatePosition(self):
        self.x = settings.GRID_X + self.col * (settings.TILE_SIZE + settings.SPACING)
        self.y = settings.GRID_Y + self.row * (settings.TILE_SIZE + settings.SPACING)
        self.rect = pygame.Rect(self.x, self.y, settings.TILE_SIZE, settings.TILE_SIZE)

    def draw(self, screen, image):
        screen.blit(image, (self.x, self.y))