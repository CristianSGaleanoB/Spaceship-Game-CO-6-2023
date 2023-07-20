import pygame

from game.utils.constants import BG, EARTH, MOON, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE, GAME_OVER, NAME_GAME, MOVE, SHOOT, WIDTH_MOVE, WIDTH_SHOOT, HEIGHT_MOVE, HEIGHT_SHOOT
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import Enemyhandler
from game.components.meteorite.meteorite_handler import Meteoritehandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.power_up_handler import PowerUpHandler
from game.utils import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        pygame.time.get_ticks()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.velocity = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = Enemyhandler()
        self.bullet_handler = BulletHandler()
        self.meteorite = Meteoritehandler()
        self.power_up_handler = PowerUpHandler()
        self.score_bosses = 0
        self.score = 0
        self.score_travel = 0
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
            self.score_travel += 1
            self.player.update(self.velocity, user_input, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.enemies, self.enemy_handler.bosses)
            self.power_up_handler.update(self.player)
            self.score = self.enemy_handler.enemies_basic_destroyed + self.enemy_handler.boss_destroyed + self.score_travel
            self.score_bosses = self.enemy_handler.boss_destroyed // 1000
            if self.score > self.score_max:
                self.score_max = self.score
            self.meteorite.update(self.player)
            if not self.player.is_alive:
                pygame.time.delay(500)
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
            self.power_up_handler.draw(self.screen)
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
            image = NAME_GAME
            image_rect = image.get_rect()
            image_rect.center = (SCREEN_WIDTH // 2 + 30, SCREEN_HEIGHT // 2 - 50)
            image_move = MOVE
            image_move = pygame.transform.scale(image_move, (WIDTH_MOVE, HEIGHT_MOVE))
            image_move_rect = image_move.get_rect()
            image_move_rect.center = (150, 440)
            image_shoot = SHOOT
            image_shoot = pygame.transform.scale(image_shoot, (WIDTH_SHOOT, HEIGHT_SHOOT))
            image_shoot_rect = image_move.get_rect()
            image_shoot_rect.center = (155, 545)
            
            text, text_rect = text_utils.get_message('Press any key to start', 30, WHITE, width = SCREEN_WIDTH // 2 - 30, height = SCREEN_HEIGHT // 2 + 80)
            text_tip, text_tip_rect = text_utils.get_message('TIP: The boos survive 25 bullets', 20, WHITE, 180, 20 )
            text_tip1, text_tip1_rect = text_utils.get_message('The other enemies survive minus 10 bullets', 20, WHITE, 230, 40 )
            text_tip2, text_tip2_rect = text_utils.get_message('Be careful whit meteors they only need 1 hit', 20, WHITE, 230, 60 )
            text_to_player, text_to_player_rect = text_utils.get_message('Play with ur friends and tell us who have the best score :)', 30, WHITE, width = SCREEN_WIDTH // 2 - 30, height = SCREEN_HEIGHT // 2 - 120)
            text_move, text_move_rect =text_utils.get_message('Move with: ', 20, WHITE, 60, 448 )
            text_shoot, text_shoot_rect =text_utils.get_message('Shoot with: ', 20, WHITE, 60, 528 ) 
            
            self.screen.blit(text_tip2, text_tip2_rect)
            self.screen.blit(text_tip1, text_tip1_rect)
            self.screen.blit(text_tip, text_tip_rect)
            self.screen.blit(text_to_player, text_to_player_rect)
            self.screen.blit(text_shoot, text_shoot_rect)
            self.screen.blit(text_move, text_move_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(image, image_rect)
            self.screen.blit(image_move, image_move_rect)
            self.screen.blit(image_shoot, image_shoot_rect)
        else:
            image = GAME_OVER
            image_rect = image.get_rect()
            image_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            text, text_rect = text_utils.get_message('press any key to Restart', 30, WHITE)            
            score_max, score_max_rect = text_utils.get_message(f'Max Score: {self.score_max}', 30, WHITE, height = SCREEN_HEIGHT // 2 + 50)
            score_attemps, score_attemps_rect = text_utils.get_message(f'Attemp number: {self.number_deaths}', 30, WHITE, height = SCREEN_HEIGHT // 2 + 100)
            score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 30, WHITE, height= SCREEN_HEIGHT // 2 + 150)
            score_boss, score_boss_rect = text_utils.get_message(f'You kill {self.score_bosses} bosses in this round', 30, WHITE, height= SCREEN_HEIGHT // 2 + 200)
            score_travel, score_travel_rect = text_utils.get_message(f'You travel {self.score_travel} years in your ship', 30, WHITE, height= SCREEN_HEIGHT // 2 + 250)
            
            self.screen.blit(score_travel, score_travel_rect)
            self.screen.blit(score_boss, score_boss_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(score_max, score_max_rect)
            self.screen.blit(score_attemps, score_attemps_rect)
            self.screen.blit(image, image_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Your score is: {self.score}', 20, WHITE, 1000, 40)
        self.screen.blit(score, score_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.meteorite.reset()
        self.power_up_handler.reset()
        self.score = 0
        self.score_bosses= 0
        self.score_travel = 0