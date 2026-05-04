import pygame
import settings

class Tile:
    def __init__(self, tile_type, row, col):
        self.type = tile_type
        self.row = row
        self.col = col
        self.updatePosition()

    def updatePosition(self):
        # row/col'a göre ekran konumunu hesapla
        self.x = settings.GRID_X + self.col * settings.TILE_SIZE
        self.y = settings.GRID_Y + self.row * settings.TILE_SIZE
        self.rect = pygame.Rect(self.x, self.y, settings.TILE_SIZE, settings.TILE_SIZE)

    def draw(self, screen, image):
        screen.blit(image, (self.x, self.y))