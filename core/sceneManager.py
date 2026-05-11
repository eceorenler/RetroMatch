#this script defines the base class for all scenes and the scene manager that handles switching between scenes.

import pygame
import settings


class SceneBase: #base class for all scenes
    def __init__(self):
        self.nextScene = self

    def processInput(self, events, pressedKeys):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

    def switchToScene(self, nextScene):
        self.nextScene = nextScene
        
    def terminate(self):
        self.switchToScene(None)

        
class SceneManager: #runs the current scene and handles switching between scenes
    def __init__(self, startingScene):
        self.currentScene = startingScene

    def run(self): #main game loop
        screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)) #creates game window
        pygame.display.set_caption(settings.TITLE)
        clock = pygame.time.Clock()

        while self.currentScene is not None:
            events = pygame.event.get() #takes all user inputs in this frame

            pressedKeys = pygame.key.get_pressed() #takes all keyboard inputs in this frame

            for event in events: #if the window closed -> quit the game
                if event.type == pygame.QUIT:
                    self.currentScene = None
            
            if self.currentScene: #if there is a current scene -> run
                self.currentScene.processInput(events, pressedKeys)
                self.currentScene.update()
                self.currentScene.render(screen)

                pygame.display.flip() # display everything we just rendered
                clock.tick(settings.FPS)

                self.currentScene = self.currentScene.nextScene 

        
        pygame.quit()

