import pygame

from game.utils.constants import BG, EARTH, MOON, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE 
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import Enemyhandler
from game.components.meteorite.meteorite_handler import Meteoritehandler
from game.components.bullets.bullet_handler import BulletHandler
from game.utils import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = Enemyhandler()
        self.bullet_handler = BulletHandler()
        self.meteorite = Meteoritehandler()
        self.score = 0
        self.score_max = 0
        self.number_deaths = 0
        

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.reset()
                self.playing = True

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(self.game_speed, user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies)
            self.score = self.enemy_handler.enemies_basic_destroyed
            if self.score > self.score_max:
                self.score_max = self.score
            self.meteorite.update(self.player)
            if not self.player.is_alive:
                pygame.time.delay(1000)
                self.playing = False
                self.number_deaths += 1

    
    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS) 
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.meteorite.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu() 
        pygame.display.update()
        pygame.display.flip()
 
    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

        earth = pygame.transform.scale(EARTH, (200, 200))
        image_height = earth.get_height()
        self.screen.blit(earth, (100, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(earth, (100, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += 5
        
        moon = pygame.transform.scale(MOON, (50, 50))
        image_height = moon.get_height()
        self.screen.blit(moon, (80, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(moon, (80, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += 5

    def draw_menu(self):
        if self.number_deaths == 0:
            text, text_rect = text_utils.get_message('Press any key', 30, WHITE)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('press any key to Restart', 30, WHITE)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE, height= SCREEN_HEIGHT // 2 + 50)
            score_max, score_max_rect = text_utils.get_message(f'Max Score: {self.score_max}', 30, WHITE, height = SCREEN_HEIGHT // 2 - 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(score_max, score_max_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE, 1000, 40)
        self.screen.blit(score, score_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.meteorite.reset()
        self.score = 0       