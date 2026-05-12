#this script defines the menu scene of the game, where players can start the game or quit.
#it displays the game title and some alien sprites for visual appeal.
#the menu music is also played in this scene.

import pygame
import settings
from core.sceneManager import SceneBase

class MenuScene(SceneBase): #menu scene class inherits from SceneBase -> provides basic scene management
    
    def __init__(self):
        super().__init__()
        self.font_big = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf", 48)
        self.font_small = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf", 12)

        self.menuMusic = pygame.mixer.Sound("assets/sounds/menu.mp3")
        self.menuMusic.play()

        self.aliens = [] #load alien sprites for menu screen

        for i in range(5): 
            img = pygame.image.load(f"assets/sprites/alien{i+1}.png")
            img = pygame.transform.scale(img, (50, 50))
            self.aliens.append(img)

    def processInput(self, events, pressedKeys): #handle user input in the menu scene
        
        for event in events: #check for key presses in the frame
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #if the pressed key is enter -> switch the game scene

                    self.menuMusic.stop() 
                    
                    from scenes.gameScene import GameScene
                    self.switchToScene(GameScene())

                if event.key == pygame.K_ESCAPE: #if the pressed key is escape -> quit the game
                    self.terminate()

    def update(self):
        pass

    def render(self, screen): #render the menu screen with title, instructions and alien sprites
        screen.fill(settings.GB_DARKEST)

        title1 = self.font_big.render("RETRO", True, settings.GB_LIGHTEST)
        title2 = self.font_big.render("MATCH", True, settings.GB_LIGHTEST)
        playText = self.font_small.render("PRESS ENTER TO PLAY", True, settings.GB_LIGHT)
        quitText = self.font_small.render("ESC TO QUIT", True, settings.GB_LIGHT)

        #draw alien sprites to screen in different locations
        screen.blit(self.aliens[0], (35, 70))
        screen.blit(self.aliens[1], (315, 95))
        screen.blit(self.aliens[2], (360, 250))
        screen.blit(self.aliens[3], (55, 470))
        screen.blit(self.aliens[4], (300, 575))

    
        #texts are centered on the screen using their width and the window width
        screen.blit(title1, (settings.WINDOW_WIDTH // 2 - title1.get_width() // 2, 230))
        screen.blit(title2, (settings.WINDOW_WIDTH // 2 - title2.get_width() // 2, 295))
        screen.blit(playText, (settings.WINDOW_WIDTH // 2 - playText.get_width() // 2, 430))
        screen.blit(quitText, (settings.WINDOW_WIDTH // 2 - quitText.get_width() // 2, 490))