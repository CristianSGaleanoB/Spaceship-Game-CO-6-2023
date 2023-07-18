import pygame
from game.components.meteorite.meteorite import Meteorite
from game.utils.constants import METEOR

class Meteor(Meteorite):
    WIDTH = 20
    HEIGHT = 20
    SPEED_X = 7
    SPEED_Y = 4
    
    def __init__(self):
        self.image = METEOR
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        super().__init__(self.image)