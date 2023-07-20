import random
from game.components.enemies.ship import Ship
from game.components.enemies.ovni import Ovni
from game.components.enemies.ship_fighter import Figther_ship
from game.components.enemies.boss import Boss


class Enemyhandler:
    def __init__(self):
        self.enemies = []
        self.bosses = []
        self.enemies_basic_destroyed = 0
        self.boss_destroyed = 0
        self.spawn_time = 300 
        self.current_spawn_time = self.spawn_time 
    
    def update(self, bullet_handler):
        
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible or not enemy.is_alive:
                self.remove_enemy(enemy)    
            if not enemy.is_alive:
                self.enemies_basic_destroyed += 1
        for boss in self.bosses:
            boss.update(bullet_handler)
            if not boss.is_visible or not boss.is_alive:
                self.remove_boss(boss)    
            if not boss.is_alive:
                self.boss_destroyed += 50
    
    def draw(self, screen):
        for boss in self.bosses:
            boss.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        self.current_spawn_time -= 1
        if self.current_spawn_time <= 0:
            self.bosses.append(Boss())
            self.current_spawn_time = self.spawn_time
        if len(self.enemies) < 5:
            enemy_type = random.choice([Ship, Ovni, Figther_ship])
            self.enemies.append(enemy_type())
        
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def remove_boss(self, boss):
        self.bosses.remove(boss)
 

    def reset(self):
        self.enemies = []
        self.bosses = []
        self.enemies_basic_destroyed = 0
        self.boss_destroyed = 0
        self.spawn_time = 100
        self.current_spawn_time = self.spawn_time