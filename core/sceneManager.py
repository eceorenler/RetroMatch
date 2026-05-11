import pygame
import settings


class SceneBase:
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

        
class SceneManager:
    def __init__(self, startingScene):
        self.currentScene = startingScene

    def run(self):
        screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        clock = pygame.time.Clock()

        while self.currentScene is not None:
            events = pygame.event.get()

            pressedKeys = pygame.key.get_pressed()

            for event in events:
                if event.type == pygame.QUIT:
                    self.currentScene = None
            
            if self.currentScene:
                self.currentScene.processInput(events, pressedKeys)
                self.currentScene.update()
                self.currentScene.render(screen)

                pygame.display.flip()
                clock.tick(settings.FPS)

                self.currentScene = self.currentScene.nextScene 

        
        pygame.quit()

