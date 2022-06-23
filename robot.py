
from unicodedata import name
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = int() 
        self.active_weapon = Weapon()
    
    def attack_dinosaur(self, dinosaur):
        pass
    # will be a void function: does not return anything