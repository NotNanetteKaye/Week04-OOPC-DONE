
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        pass

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacked Robot Rowdy for {self.attack_power} damage!")
        print(f"Robot Rowdy has {robot.health} health remaining!")
        pass
        # will be a void function
    

