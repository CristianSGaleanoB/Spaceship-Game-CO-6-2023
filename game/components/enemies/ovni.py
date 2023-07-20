import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import OVNI

class Ovni(Enemy):
    WIDTH = 50
    HEIGHT = 40
    SPEED_X = 4
    SPEED_Y = 3
    MOVEMENT_y = 7
    MOVEMENT_X = 10
    INTERVAL = 80
    SHOOTING_TIME = 20
    LIFE = 5

    
    def __init__(self):
        self.image = OVNI
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        self.type = 'normal'
        super().__init__(self.image, self.type)
    
    #def update(self):
     #    self.move_ovni()
      #   super().update()
    
    #def move_ovni(self):
     #   if self.index > self.INTERVAL:
      #      self.rect.y -= self.MOVEMENT_X
       #     self.rect.x -= self.MOVEMENT_y
            