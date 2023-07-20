from game.components.power_ups.shield import Shield

class PoweUpHandler:
    INTERVAL_TIME = 300
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
        self.powerups.append(Shield())

    def remove_power_up(self, power_up):
        self.powerups.remove(power_up)

    def reset(self):
        self.powerups = []
        self.interval_time = 0