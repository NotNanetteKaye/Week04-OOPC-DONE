
# from unicodedata import name
# from dinosaur import Dinosaur
# from weapon import Weapon
# from battlefield import Battlefield


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100 
        # self.active_weapon = Weapon()
    
    def attack_dinosaur(self, dinosaur):
      dinosaur -= self.health - 35
      print(f"{self.name} attacked dinosaur.name with a weapon.name for {dinosaur} damage!")
      print("Dinosaur.name has health remaining!")
    # # will be a void function: does not return anything


robot_Nanette = Robot("Nanette")
print(robot_Nanette.name)