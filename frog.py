'''
File: frog.py
Description: A module defining a class that represents a frog.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from amphibian import Amphibian


class Frog(Amphibian):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._Animal__environment_types.append("wetland")
        self._Animal__environment_types.append("tropical")
        self._Animal__environment_types.append("forest")
        self._Animal__environment_types.append("freshwater aquatic")

    def cry(self):
        print("*ribbit ribbit croak*")

    def sleep(self):
        print(f"{self.name} rests on a lillypad...")

    def eat(self):
        print(f"{self.name} catches bug on tongue...")

    def move(self):
        print(f"{self.name} jumps around...")

    def swim(self):
        print(f"{self.name} pushes through the water...")