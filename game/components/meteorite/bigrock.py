import pygame
from game.components.meteorite.meteorite import Meteorite
from game.utils.constants import METEOR

class Bigrock(Meteorite):
    WIDTH = 80
    HEIGHT = 70
    SPEED_X = 2
    SPEED_Y = 5
  
    def __init__(self):
        self.image = METEOR
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
