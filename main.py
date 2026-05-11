import pygame
from scenes.gameScene import GameScene
import settings
from core.sceneManager import SceneManager
from scenes.menuScene import MenuScene

pygame.init()
pygame.mixer.init()

SceneManager(GameScene()).run()