import pygame
import random
import settings

from game.tile import Tile

class Board:
    def __init__(self):
        self.grid = []
        self.selected = None
        self.score = 0
        self.fillBoard()

    def fillBoard(self):
        self.grid = []

        for row in range(settings.GRID_ROWS):
            currentRow = []

            for col in range(settings.GRID_COLS):
                tileType = random.randint(0, settings.TILE_TYPES-1)
                currentRow.append(Tile(tileType, row, col))

            self.grid.append(currentRow)


    def swap(self, r1, c1, r2, c2):
        
        self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1] #swap

        #update the info for each tile
        self.grid[r1][c1].row, self.grid[r1][c1].col = r1,c1
        self.grid[r2][c2].row, self.grid[r2][c2].col = r2,c2

        #update the position of the tiles
        self.grid[r1][c1].updatePosition()
        self.grid[r2][c2].updatePosition()


    def findMatches(self):
        matched = set()

        # Check rows for matches
        for row in range(settings.GRID_ROWS):
            for col in range(settings.GRID_COLS-2):
                if self.grid[row][col].type == self.grid[row][col+1].type == self.grid[row][col+2].type:
                    matched.add((row, col))
                    matched.add((row, col+1))
                    matched.add((row, col+2))

        for row in range(settings.GRID_ROWS - 2):
            for col in range(settings.GRID_COLS):
                if self.grid[row][col].type == self.grid[row+1][col].type == self.grid[row+2][col].type:
                    matched.add((row, col))
                    matched.add((row+1, col))
                    matched.add((row+2, col))

        return matched

#to be continued
