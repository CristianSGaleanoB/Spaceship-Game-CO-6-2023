import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

MOON = pygame.image.load(os.path.join(IMG_DIR, 'Other/Moon.png'))

EARTH = pygame.image.load(os.path.join(IMG_DIR, 'Other/earth.png'))

METEOR = pygame.image.load(os.path.join(IMG_DIR, 'Other/meteor.png'))

BIGROCK = pygame.image.load(os.path.join(IMG_DIR, 'Other/Bigrock.png'))

METEORDOWN = pygame.image.load(os.path.join(IMG_DIR, 'Other/meteor down.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_GODPOWER =pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_godpower.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
FIGHTER_SHIP = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ship_fighter.png"))
OVNI = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ovni.png"))
BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/boss.png"))
FONT_STYLE = 'freesansbold.ttf'

LEFT = 'left'
RIGTH = 'right'

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/Gameover.png"))

NAME_GAME = pygame.image.load(os.path.join(IMG_DIR, "Other/spacesurvival.png"))

MOVE = pygame.image.load(os.path.join(IMG_DIR, "Other/move.png"))
WIDTH_MOVE = 90
HEIGHT_MOVE = 80

SHOOT = pygame.image.load(os.path.join(IMG_DIR, "Other/space.png"))
WIDTH_SHOOT = 100
HEIGHT_SHOOT = 40

WHITE = (255, 255, 255)

GOD_POWER = pygame.image.load(os.path.join(IMG_DIR, "Other/god_power.png"))