import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1

class Ship(Enemy):
    WIDTH = 40
    HEIGHT = 60
    LIFE = 2

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        self.type = 'normal'
        super().__init__(self.image, self.type)
