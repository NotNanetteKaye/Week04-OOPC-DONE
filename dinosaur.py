
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = int(attack_power)

    def attack(self, robot):
        robot -= self.attack_power
        print(f"{self.name} attacked Robot Rowdy for {self.attack_power} damage!")
        print(f"Robot Rowdy has {robot} health remaining!")
        # will be a void function
    

dino_darling = Dinosaur("Dino Darling", 80)
dino_darling.attack(100)