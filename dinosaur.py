
from email.base64mime import header_length
from unicodedata import name


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack_robot(self, robot):
        robot = ''
        # will be a void function
        pass