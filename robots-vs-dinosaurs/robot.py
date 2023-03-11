from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100 
        self.active_weapon = Weapon("knife", 20)
        pass
    
    def attack(self, dinosaur):
      dinosaur.health -= self.active_weapon.attack_power
      print(f"{self.name} attacked Dino Darling with a {self.active_weapon.name} for {self.active_weapon.attack_power} damage!")
      print(f"Dino Darling has {dinosaur.health} health remaining!")
      pass
    # # will be a void function: does not return anything



