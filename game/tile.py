import pygame
import settings

class Tile:
    def __init__(self, tileType, row, col):
        self.type = tileType
        self.row = row
        self.col = col

        self.is_popping = False
        self.pop_frame = 0
        self.pop_duration = 10

        self.updatePosition()

    def updatePosition(self):
        self.x = settings.GRID_X + self.col * (settings.TILE_SIZE + settings.SPACING)
        self.y = settings.GRID_Y + self.row * (settings.TILE_SIZE + settings.SPACING)
        self.rect = pygame.Rect(self.x, self.y, settings.TILE_SIZE, settings.TILE_SIZE)

    def startPop(self):
        self.is_popping = True
        self.pop_frame = 0

    def update(self):
        if self.is_popping:
            self.pop_frame += 1

    def isFinished(self):
        return self.pop_frame >= self.pop_duration

    def draw(self, screen, image):
        if self.is_popping:
            progress = self.pop_frame / self.pop_duration
            size = int(settings.TILE_SIZE * (1 - progress))

            if size > 0:
                small = pygame.transform.scale(image, (size, size))
                offset = (settings.TILE_SIZE - size) // 2
                screen.blit(small, (self.x + offset, self.y + offset))
        else:
            screen.blit(image, (self.x, self.y))