'''
File: turtle.py
Description: A module defining a class that represents a turtle.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from reptile import Reptile


class Turtle(Reptile):
    def __init__(self, name, age, freshwater=False, saltwater=False):
        super().__init__(name, age)
        if freshwater == True:
            self._Animal__environment_types.append("freshwater aquatic")
        if saltwater == True:
            self._Animal__environment_types.append("saltwater aquatic")

    def cry(self):
        print("*chirp growl wheeze*")

    def sleep(self):
        print(f"{self.name} retreats into shell to sleep...")

    def eat(self):
        print(f"{self.name} bites into food...")

    def move(self):
        print(f"{self.name} crawls and shuffles...")

    def swim(self):
        print(f"{self.name} paddles through the water...")