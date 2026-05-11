import pygame
import settings
from core.sceneManager import SceneBase

class MenuScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.font_big = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf", 72)
        self.font_small = pygame.font.Font("assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf", 16)

    def process_input(self, events, pressedKeys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    from scenes.gameScene import GameScene
                    self.switchToScene(GameScene())

    def update(self):
        pass

    def render(self, screen):
        screen.fill(settings.GB_DARKEST)

        title1 = self.font_big.render("RETRO", True, settings.GB_LIGHTEST)
        title2 = self.font_big.render("MATCH", True, settings.GB_LIGHTEST)
        instr = self.font_small.render("Press ENTER to play", True, settings.GB_LIGHT)

        #center the text
        screen.blit(title1, (settings.WINDOW_WIDTH // 2 - title1.get_width() // 2, 250))
        screen.blit(title2, (settings.WINDOW_WIDTH // 2 - title2.get_width() // 2, 320))
        screen.blit(instr, (settings.WINDOW_WIDTH // 2 - instr.get_width() // 2, 500))