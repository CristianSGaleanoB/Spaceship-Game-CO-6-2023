import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT, RIGTH

class Meteorite:
    Y_POS = 0
    SPEED_X = 2
    SPEED_Y = 2
    MOV_X = [LEFT, RIGTH]
    INTERVAL = 100

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(image.get_width(), SCREEN_WIDTH - image.get_width())
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.is_visible = True
    
    def update(self):
        self.move()
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_visible = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.rect.x <= 0:
                self.rect.x = SCREEN_WIDTH
                       
        else:
            self.rect.x += self.SPEED_X
            if self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.rect.x = 0
                               
    
    
