import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import FIGHTER_SHIP

class Figther_ship(Enemy):
    WIDTH = 50
    HEIGHT = 60
    SPEED_X = 4
    SPEED_Y = 2
    MOVEMENT_y = 7
    MOVEMENT_X = 15
    INTERVAL = 30

    def __init__(self):
        self.image = FIGHTER_SHIP
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

   #def update(self):
    #     self.move_fighter()
     

    #def move_fighter(self):
     #   if self.index > self.INTERVAL:
      #      self.rect.y += self.MOVEMENT_X
       #     self.rect.x += self.MOVEMENT_y
        