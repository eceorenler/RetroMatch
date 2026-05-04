import pygame
import settings
from core.sceneManager import SceneManager
from scenes.menuScene import MenuScene

pygame.init()
pygame.mixer.init()

SceneManager(MenuScene()).run()