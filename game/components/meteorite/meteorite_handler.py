import random
from game.components.meteorite.meteor import Meteor
from game.components.meteorite.bigrock import Bigrock
from game.components.meteorite.meteordown import Meteordown


class Meteoritehandler:
    def __init__(self):
        self.meteorites = []

    def update(self, player):
        self.add_meteorite()
        for meteorite in self.meteorites:
            meteorite.update(player)
            if not meteorite.is_visible:
                self.remove_meteorite(meteorite)
    
    def draw(self, screen):
        for meteorite in self.meteorites:
            meteorite.draw(screen)
    
    def add_meteorite(self):
        if len(self.meteorites) < 5:
            meteorite_type = random.choice([Meteor, Bigrock, Meteordown])
            self.meteorites.append(meteorite_type())
    
    def remove_meteorite(self, meteorite):
        self.meteorites.remove(meteorite)

    def reset(self):
        self.meteorites = []