import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import BOSS

class Boss(Enemy):
    WIDTH = 533
    HEIGHT = 500
    SPEED_X = 4
    SPEED_Y = 3
    MOVEMENT_y = 7
    MOVEMENT_X = 10
    INTERVAL = 80
    
    def __init__(self):
        self.image = BOSS
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        super().__init__(self.image)