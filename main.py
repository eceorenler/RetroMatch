#this is the main file that runs the game. 
#initializes pygame, sets up the scene manager and starts the game loop.

import pygame
from core.sceneManager import SceneManager
from scenes.menuScene import MenuScene

pygame.init()
pygame.mixer.init()

SceneManager(MenuScene()).run()