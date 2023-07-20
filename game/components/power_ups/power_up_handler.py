import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.god_power_up import GodPower

class PowerUpHandler:
    INTERVAL_TIME = random.randint(100, 300)


    def __init__(self):
        self.powerups = []
        self.interval_time = 0

    def update(self, player):
        self.interval_time += 1
        if self.interval_time % self.INTERVAL_TIME == 0:
            self.add_power_up()
        for power_up in self.powerups:
            power_up.update(player)
            if not power_up.is_visible:
                self.remove_power_up(power_up)
            if power_up.is_used:
                player.activate_power_up(power_up)

    def draw(self, screen):
        for power_up in self.powerups:
            power_up.draw(screen)

    def add_power_up(self):
        if len(self.powerups) < 5:
            power_type = random.choice([Shield, GodPower])
            self.powerups.append(power_type())
 

    def remove_power_up(self, power_up):
        self.powerups.remove(power_up)

    def reset(self):
        self.powerups = []
        self.interval_time = 0