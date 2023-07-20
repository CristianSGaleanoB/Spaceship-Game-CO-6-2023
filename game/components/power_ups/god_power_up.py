from game.components.power_ups.power_up import PowerUp
from game.utils.constants import GOD_POWER

class GodPower(PowerUp):
    DURATION = 3000
    def __init__(self):
        self.image = GOD_POWER
        super().__init__(self.image)
