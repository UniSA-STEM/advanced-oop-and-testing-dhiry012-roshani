'''
File: shark.py
Description: A module defining a class that represents a shark.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from fish import Fish


class Shark(Fish):
    def __init__(self, name, age, freshwater=False, saltwater=False):
        super().__init__(name, age, freshwater, saltwater)
        if freshwater == True:
            self._Animal__environment_types.append("freshwater aquatic")
        if saltwater == True:
            self._Animal__environment_types.append("saltwater aquatic")

    def cry(self):
        print("*da da...da da...dadadadadada*")

    def sleep(self):
        print(f"{self.name} keeps moving...or dies...")

    def eat(self):
        print(f"{self.name} attacks food mercilessly...")

    def swim(self):
        print(f"{self.name} cruises through the water...")