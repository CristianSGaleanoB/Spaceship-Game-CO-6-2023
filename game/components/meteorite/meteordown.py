import pygame
from game.components.meteorite.meteorite import Meteorite
from game.utils.constants import  METEORDOWN

class Meteordown(Meteorite):
    WIDTH = 80
    HEIGHT = 70
    SPEED_X = 0
    SPEED_Y = 10
  
    def __init__(self):
        self.image = METEORDOWN
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        super().__init__(self.image)