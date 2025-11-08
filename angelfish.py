'''
File: angelfish.py
Description: A module defining a class that represents an angelfish.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from fish import Fish


class Angelfish(Fish):
    def __init__(self, name, age, freshwater=False, saltwater=False):
        super().__init__(name, age, freshwater, saltwater)
        if freshwater == True:
            self._Animal__environment_types.append("freshwater aquatic")
        if saltwater == True:
            self._Animal__environment_types.append("saltwater aquatic")

    def cry(self):
        print("*blop blop*")

    def sleep(self):
        print(f"{self.name} hovers asleep in the water...")

    def eat(self):
        print(f"{self.name} slurps up food...")

    def swim(self):
        print(f"{self.name} floats around...")