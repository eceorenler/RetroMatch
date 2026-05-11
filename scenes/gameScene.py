import pygame
import settings
from core.sceneManager import SceneBase
from game.board import Board


class GameScene(SceneBase):
    def __init__(self):
        super().__init__()

        self.board = Board()
        self.timeLeft = settings.GAME_DURATION

        self.images = self.loadImages()

        self.timerStarted = False
        self.lastTick = pygame.time.get_ticks()

        self.countdownSound = pygame.mixer.Sound("assets/sounds/countdown.mp3")
        self.countdownPlayed = False
        pygame.mixer.stop()

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

            elapsed = (now - self.lastTick) / 1000
            self.lastTick = now

            self.timeLeft -= elapsed

            if self.timeLeft <= 3 and not self.countdownPlayed:
                self.countdownSound.play()
                self.countdownPlayed = True

            if self.timeLeft <= 0:
                self.timeLeft = 0

                from scenes.gameOver import GameOver
                self.switchToScene(GameOver(self.board.score))

    def render(self, screen):
        screen.fill(settings.GB_DARKEST)

        gameboy = pygame.image.load("assets/sprites/board.png")
        gameboy = pygame.transform.scale(
            gameboy,
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        )

        screen.blit(gameboy, (0, 0))

        self.board.draw(screen, self.images)

        font_big = pygame.font.Font(
            "assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf",
            24
        )

        font_small = pygame.font.Font(
            "assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf",
            14
        )

        scoreText = font_big.render(
            f"{self.board.score}",
            True,
            settings.GB_LIGHTEST
        )

        screen.blit(
            scoreText,
            (
                settings.WINDOW_WIDTH // 2 - scoreText.get_width() // 2,
                50
            )
        )

        timerText = font_small.render(
            f"TIME {int(self.timeLeft)}",
            True,
            settings.GB_LIGHTEST
        )

        screen.blit(
            timerText,
            (
                138 + (156 // 2) - timerText.get_width() // 2,
                543 + (45 // 2) - timerText.get_height() // 2
            )
        )

        infoText = font_small.render(
            "GET THE HIGHEST SCORE",
            True,
            settings.GB_LIGHT
        )

        screen.blit(
            infoText,
            (
                settings.WINDOW_WIDTH // 2 - infoText.get_width() // 2,
                100
            )
        )