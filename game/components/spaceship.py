import pygame
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, SPACESHIP_GODPOWER, WHITE
from game.components.power_ups.shield import Shield
from game.components.power_ups.god_power_up import GodPower
from game.utils import text_utils

class Spaceship:
    WIDTH = 40
    HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS =  500
    LIFE = 3

   
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS  
        self.rect.y = self.Y_POS
        self.shooting = False
        self.is_alive = True
        self.has_shield = False
        self.has_godpower = False
        self.time_up = 0
        self.life = self.LIFE
        

    def update(self, velocity, user_input, bullet_handler):
        if self.has_godpower:
            velocity = velocity + 30
            if self.has_godpower:
                time_to_show = round((self.time_up - pygame.time.get_ticks()) / 1000, 2)
                if time_to_show < 0:
                    self.deactivate_power_up()
        if user_input[pygame.K_SPACE]:
            self.shooting =True
            self.shoot(bullet_handler)
        if user_input[pygame.K_LEFT]:
            self.move_left(velocity)
        if user_input[pygame.K_RIGHT]:
            self.move_right(velocity)
        if user_input[pygame.K_UP]:
            self.move_up(velocity)
        if user_input[pygame.K_DOWN]:
            self.move_down(velocity)
        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.deactivate_power_up()
        

    def draw(self,screen):
        text, text_rect = text_utils.get_message(f'LIFES: {self.life}', 20, WHITE,  70, 20 )
        screen.blit(text, text_rect)
        screen.blit(self.image, self.rect)

    def modify_velocity(self, velocity):
        if self.has_godpower:
            new_velocity = velocity + 30
            velocity =  new_velocity

    def move_left(self, velocity):
        self.rect.x -= velocity
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH
        
    def move_right(self, velocity):
        self.rect.x += velocity
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 0

    def move_up(self, velocity):
        if self.rect.y > (SCREEN_HEIGHT // 2):
            self.rect.y -= velocity
    
    def move_down(self, velocity):
        if self.rect.bottom < (SCREEN_HEIGHT - 20) :
            self.rect.y += velocity

    def shoot(self, bullet_handler):
        if self.shooting == True:
            bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)
        else: 
            self.shooting = False
    
        
    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
            self.has_shield = True
        
        if type(power_up) == GodPower:
            self.image = SPACESHIP_GODPOWER
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
            self.has_godpower = True


    def deactivate_power_up(self):
        self.has_godpower = False
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    
    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect  = self.image.get_rect()
        self.rect.x = self.X_POS  
        self.rect.y = self.Y_POS
        self.shooting = False
        self.is_alive = True
        self.has_shield = False
        self.has_godpower = False
        self.life = self.LIFE