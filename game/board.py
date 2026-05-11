#this script handles everything related to game board
#grid management, tile swapping, match finding and popping, shuffling when no moves left and drawing the board to the screen.

import pygame
import random
import settings

from game.tile import Tile #import the tile class to create tiles for the board


class Board: #main class that manages the game board
    def __init__(self):
        self.grid = []
        self.selected = None
        self.score = 0

        self.isAnimating = False
        self.currentMatches = set() #stores the currently matched tiles

        self.shuffleFlash = 0
        self.matchSound = pygame.mixer.Sound("assets/sounds/match.mp3")

        self.fillBoard()

    def fillBoard(self): #fills the board with random tiles
        self.grid = []

        for row in range(settings.GRID_ROWS):
            currentRow = []

            for col in range(settings.GRID_COLS):

                tileType = random.randint(0, settings.TILE_TYPES - 1) #random tile type
                currentRow.append(Tile(tileType, row, col)) #generates a tile and adds it to current row

            self.grid.append(currentRow) #adds the current row to the grid

    def swap(self, r1, c1, r2, c2): #swaps two tiles and updates their positions

        self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]

        self.grid[r1][c1].row, self.grid[r1][c1].col = r1, c1 #updates the row and column of the first tile
        self.grid[r2][c2].row, self.grid[r2][c2].col = r2, c2 #updates the row and column of the second tile

        self.grid[r1][c1].updatePosition()  #updates the position of the first tile
        self.grid[r2][c2].updatePosition()  #updates the position of the second tile

    def findMatches(self): #finds all matched tiles and returns their positions
        matched = set()

        #check horizontal matches
        for row in range(settings.GRID_ROWS):
            for col in range(settings.GRID_COLS - 2): #minus 2 because in last 2 columns we can't have a match of 3
                if (
                    self.grid[row][col].type
                    == self.grid[row][col + 1].type
                    == self.grid[row][col + 2].type
                ):
                    matched.add((row, col))
                    matched.add((row, col + 1))
                    matched.add((row, col + 2))

        #check vertical matches
        for row in range(settings.GRID_ROWS - 2):
            for col in range(settings.GRID_COLS):
                if (
                    self.grid[row][col].type
                    == self.grid[row + 1][col].type
                    == self.grid[row + 2][col].type
                ):
                    matched.add((row, col))
                    matched.add((row + 1, col))
                    matched.add((row + 2, col))

        return matched

    def popMatches(self, matched): #starts the pop animation for matched tiles

        self.matchSound.play() #plays the sound effect
        self.isAnimating = True
        self.currentMatches = matched

        for row, col in matched:
            self.grid[row][col].startPop()

    def update(self): #updates the board in every frame

        if self.shuffleFlash > 0:
            self.shuffleFlash -= 1

        if self.isAnimating:
            allFinished = True #flag for checking if all popping animations are finished

            for row, col in self.currentMatches:
                tile = self.grid[row][col]
                tile.update()

                if not tile.isFinished():
                    allFinished = False

            if allFinished:
                for row, col in self.currentMatches:
                    self.grid[row][col] = Tile(
                        random.randint(0, settings.TILE_TYPES - 1),
                        row,
                        col
                    )

                self.score += len(self.currentMatches) * settings.MATCH_POINTS #updates score

                self.currentMatches = set()
                self.isAnimating = False

                if not self.moveCheck(): #if there is no valid moves left -> shuffle
                    self.shuffle()

    def handleClick(self, row, col): #handles the logic when a tile is clicked
        
        if self.isAnimating: #if the board is currently animating -> ignore clicks
            return

        if self.selected is None:
            self.selected = (row, col) #if no tile is currently selected -> select the clicked tile

        else:
            r1, c1 = self.selected 

            if abs(r1 - row) + abs(c1 - col) == 1: #check for adjacency
                self.swap(r1, c1, row, col) #swap

                matched = self.findMatches() #checks for matching

                if matched:
                    self.popMatches(matched) #match -> pop
                else:
                    self.swap(r1, c1, row, col) #no match -> swap back

            self.selected = None #deselect after handling the click

    def moveCheck(self): #checks if there is valid move left

        for row in range(settings.GRID_ROWS):
            for col in range(settings.GRID_COLS):

                if col < settings.GRID_COLS - 1:
                    self.swap(row, col, row, col + 1)

                    if self.findMatches():
                        self.swap(row, col, row, col + 1)
                        return True

                    self.swap(row, col, row, col + 1)

                if row < settings.GRID_ROWS - 1:
                    self.swap(row, col, row + 1, col)

                    if self.findMatches():
                        self.swap(row, col, row + 1, col)
                        return True

                    self.swap(row, col, row + 1, col)

        return False

    def shuffle(self): #shuffles the board when there is no valid move left

        allTiles = [
            self.grid[row][col].type
            for row in range(settings.GRID_ROWS)
            for col in range(settings.GRID_COLS)
        ]

        random.shuffle(allTiles)

        for row in range(settings.GRID_ROWS):
            for col in range(settings.GRID_COLS):
                self.grid[row][col].type = allTiles[row * settings.GRID_COLS + col]


        self.shuffleFlash = 20

    def draw(self, screen, images): #draws the board to the screen, also highlights the selected tile and adds a flash effect when shuffling
        for row in self.grid:
            for tile in row:
                if self.selected == (tile.row, tile.col):
                    pygame.draw.rect(screen, settings.GB_LIGHTEST, tile.rect, 3)

                tile.draw(screen, images[tile.type])

        if self.shuffleFlash > 0:
            overlay = pygame.Surface(
                (
                    settings.GRID_COLS * (settings.TILE_SIZE + settings.SPACING),
                    settings.GRID_ROWS * (settings.TILE_SIZE + settings.SPACING)
                )
            )

            overlay.set_alpha(90)
            overlay.fill(settings.GB_LIGHTEST)

            screen.blit(overlay,(settings.GRID_X - 4, settings.GRID_Y - 4))
                