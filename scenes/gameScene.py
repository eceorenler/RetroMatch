#defines the main game scene where the player interacts with the game board, matches tiles and scores points.

import pygame
import settings
from core.sceneManager import SceneBase
from game.board import Board


class GameScene(SceneBase): #game scene class inherits from SceneBase -> provides basic scene management
    
    def __init__(self):
        super().__init__()

        self.board = Board() #initialize the game board
        self.timeLeft = settings.GAME_DURATION

        self.images = self.loadImages()

        self.timerStarted = False
        self.lastTick = pygame.time.get_ticks() #used to track time for the countdown timer

        self.countdownSound = pygame.mixer.Sound("assets/sounds/countdown.mp3")
        self.countdownPlayed = False

    def loadImages(self): #load tile images based on the number of tile types defined in settings
        
        images = [] #list to hold the loaded images

        for i in range(1, settings.TILE_TYPES + 1):
            img = pygame.image.load(f"assets/sprites/alien{i}.png")
            img = pygame.transform.scale(img, (settings.TILE_SIZE, settings.TILE_SIZE))
            images.append(img)

        return images

    def processInput(self, events, pressedKeys): #handle user input in this scene
        
        for event in events: #check for key presses in the frame
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos #get mouse position on click

                col = (mx - settings.GRID_X) // (settings.TILE_SIZE + settings.SPACING)
                row = (my - settings.GRID_Y) // (settings.TILE_SIZE + settings.SPACING)
                
                #checks if the clicked position is on the grid -> starts the timer
                if 0 <= row < settings.GRID_ROWS and 0 <= col < settings.GRID_COLS:
                    self.timerStarted = True
                    self.board.handleClick(row, col)

    def update(self):
        
        if not self.board.isAnimating:
            matched = self.board.findMatches()

            if matched:
                self.board.popMatches(matched)

        self.board.update()

        if self.timerStarted:
            now = pygame.time.get_ticks()

            elapsed = (now - self.lastTick) / 1000 #convert miliseconds to seconds
            self.lastTick = now #updates the last take current time

            self.timeLeft -= elapsed 

            if self.timeLeft <= 3 and not self.countdownPlayed:
                self.countdownSound.play()
                self.countdownPlayed = True

            if self.timeLeft <= 0:
                self.timeLeft = 0

                from scenes.gameOver import GameOver
                pygame.mixer.stop()
                self.switchToScene(GameOver(self.board.score))

    def render(self, screen): #creates the game screent with bg, grid and score etc.
        
        screen.fill(settings.GB_DARKEST)

        gameboy = pygame.image.load("assets/sprites/board.png")
        gameboy = pygame.transform.scale(gameboy,(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

        screen.blit(gameboy, (0, 0))

        self.board.draw(screen, self.images)

        font_big = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf",24)
        font_small = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf",14)

        scoreText = font_big.render(f"{self.board.score}",True, settings.GB_LIGHTEST)
        screen.blit(scoreText,(settings.WINDOW_WIDTH // 2 - scoreText.get_width() // 2,50))

        timerText = font_small.render(f"TIME {int(self.timeLeft)}",True,settings.GB_LIGHTEST)
        screen.blit(timerText,(138 + (156 // 2) - timerText.get_width() // 2, 543 + (45 // 2) - timerText.get_height() // 2))

        infoText = font_small.render("GET THE HIGHEST SCORE", True, settings.GB_LIGHT)
        screen.blit(infoText,(settings.WINDOW_WIDTH // 2 - infoText.get_width() // 2, 100))