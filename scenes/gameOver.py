#this is the game over scene script.
#it displays the final score and gives the player the option to restart or quit.

import pygame
import settings
from core.sceneManager import SceneBase

class GameOver(SceneBase): 
    def __init__(self, score):
        super().__init__()
        self.score = score

        self.font_big = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf", 34)
        self.font_small = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf", 16)

        self.gameOverSound = pygame.mixer.Sound("assets/sounds/lose.mp3")
        self.gameOverSound.play()

    

    def processInput(self, events, pressedKeys): #method for handling user inputs
        for event in events:
            if event.type == pygame.KEYDOWN:

                #restart the game when player presses R
                if event.key == pygame.K_r:
                    from scenes.gameScene import GameScene #importing gameScene for restarting the game
                    self.switchToScene(GameScene()) #swithch to game scene to restart the game

                #quit the game when player presses esc
                if event.key == pygame.K_ESCAPE:
                    self.terminate()

    def update(self):
        pass

    def render(self, screen): #method for rendering the game over screen

        screen.fill(settings.GB_DARKEST)


        #uses the colors and fonts defined in settings
        titleText = self.font_big.render("TIME IS UP!", True, settings.GB_LIGHTEST)
        scoreText = self.font_small.render(f"SCORE: {self.score}", True, settings.GB_LIGHT)
        restartText = self.font_small.render("PRESS R TO TRY AGAIN", True, settings.GB_LIGHT)
        quitText = self.font_small.render("ESC TO QUIT", True, settings.GB_LIGHT)

        #write the text to the screen -> centered horizontally and spaced vertically
        screen.blit(titleText, (settings.WINDOW_WIDTH // 2 - titleText.get_width() // 2, 230))
        screen.blit(scoreText, (settings.WINDOW_WIDTH // 2 - scoreText.get_width() // 2, 320))
        screen.blit(restartText, (settings.WINDOW_WIDTH // 2 - restartText.get_width() // 2, 390))
        screen.blit(quitText, (settings.WINDOW_WIDTH // 2 - quitText.get_width() // 2, 430))