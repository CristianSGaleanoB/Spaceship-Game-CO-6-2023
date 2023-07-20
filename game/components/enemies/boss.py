import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import BOSS, SCREEN_WIDTH, SCREEN_HEIGHT

class Boss(Enemy):
    WIDTH = 320
    HEIGHT = 300
    SPEED_X = 6
    SPEED_Y = 3
    INTERVAL = 130
    SHOOTING_TIME = 15
    LIFE = 25
    
    def __init__(self):
        self.image = BOSS
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        self.type = 'Boss'
        super().__init__(self.image, self.type)
    
#    def update(self, bullet_handler):
 #       if self.rect.y >= SCREEN_HEIGHT // 2:  # Comprobar si el objeto ha alcanzado o pasado la mitad
  #          self.rect.y = SCREEN_HEIGHT // 2  # Establecer la coordenada y en la posición de la mitad
   #         self.velocity_y = -self.velocity_y  # Invertir la dirección vertical para que el objeto vuelva a subir
    #        super().update()