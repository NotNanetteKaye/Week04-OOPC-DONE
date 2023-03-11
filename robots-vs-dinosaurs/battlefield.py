from urllib import robotparser
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("Robot Rowdy")
        self.dinosaur = Dinosaur("Dino Darling", 30)
        pass
    
    def run_game(self):
       self.display_welcome()
       self.battle()
       self.display_winner()
       pass

    def display_welcome(self):
       print("Welcome to an epic battle! Only one side can win!!")
       print("Only one side can win!")
       pass


    def battle(self):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
        pass
                

    def display_winner(self):
        if self.dinosaur.health <= 0: 
            print(f"{self.robot.name} won!!!")
        if self.robot.health <= 0:
            print(f"{self.dinosaur.name} won!!!")
        pass
        # will be a void function


        


