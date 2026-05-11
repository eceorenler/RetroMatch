import pygame
import settings
from core.sceneManager import SceneBase
from game.board import Board


class GameScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.timeLeft = settings.GAME_DURATION
        self.lastUpdateTime = pygame.time.get_ticks()
        self.images = self.loadImages()

    def loadImages(self):
        images = []
        for i in range(1, settings.TILE_TYPES + 1):
            img = pygame.image.load(f"assets/sprites/alien{i}.png")
            img = pygame.transform.scale(img, (settings.TILE_SIZE, settings.TILE_SIZE))
            images.append(img)
        return images
        
    def processInput(self, events, pressedKeys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                col = (mx - settings.GRID_X) // (settings.TILE_SIZE + settings.SPACING)
                row = (my - settings.GRID_Y) // (settings.TILE_SIZE + settings.SPACING)
                if 0 <= row < settings.GRID_ROWS and 0 <= col < settings.GRID_COLS:
                    self.board.handleClick(row, col)

    def update(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateTime >= 1000:  
            self.timeLeft -= 1
            self.lastUpdateTime = currentTime

        if self.timeLeft <= 0:
            self.nextScene()  

    def render(self, screen):
        screen.fill(settings.GB_DARKEST)

        gameboy = pygame.image.load("assets/sprites/board.png")
        gameboy = pygame.transform.scale(gameboy, (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        screen.blit(gameboy, (0, 0))

        self.board.draw(screen, self.images)

        font_big = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf", 24)
        font_small = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf", 10)

        #score üstte büyük
        scoreText = font_big.render(f"{self.board.score}", True, settings.GB_LIGHTEST)
        screen.blit(scoreText, (settings.WINDOW_WIDTH // 2 - scoreText.get_width() // 2, 50))

        #timer siyah bara
        timerText = font_small.render(f"TIME {int(self.timeLeft)}", True, settings.GB_LIGHTEST)
        screen.blit(timerText, (138 + (156 // 2) - timerText.get_width() // 2, 543 + (45 // 2) - timerText.get_height() // 2))