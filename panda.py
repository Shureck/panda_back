
from importlib.util import set_loader


class Panda(object):
    def __init__(self):
        self.food = 100
        self.happiness = 100
        self.health = 100
        self.tired = 0
        self.age = 0
        self.name = "Panda"
        self.is_alive = True
        self.is_sleeping = False
        self.is_eating = False
        self.is_playing = False
        self.is_sick = False
        self.is_hungry = False
        self.is_tired = False
        self.is_bored = False
        self.is_happy = False
        self.is_coocking = False

    def __str__(self):
        return f"{self.name} is {self.age} years old, {self.health} health, {self.happiness} happiness, {self.food} food\n" \
                f"Is sleeping: {self.is_sleeping}, is eating: {self.is_eating}, is playing: {self.is_playing}, is sick: {self.is_sick}\n"
    
    def panda_live(self):
        self.age += 0.2
        self.happiness -= 0.2
        self.food -= 0.5
        self.tired += 0.2

    def cookings(self):
        self.food += 10
        self.happiness += 10
        self.is_coocking = True
        self.tired += 10

    def panda_eat(self):
        if (self.food + 40 > 100):
            self.food = 100
        else:
            self.food += 40
        self.is_eating = True
        if (self.happiness + 10 > 100):
            self.happiness = 100
        else:
            self.happiness += 10
        if (self.tired - 7 < 0):
            self.tired = 0
        else:
            self.tired -= 7
        

    def panda_sleep(self):
        self.tired -= 50
        self.is_sleeping = True