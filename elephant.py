'''
File: elephant.py
Description: A module defining a class that represents an elephant.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal


class Elephant(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._Animal__environment_types.append("grassland")
        self._Animal__environment_types.append("tropical")
        self._Animal__environment_types.append("forest")

    def cry(self):
        print("*trumpets!*")

    def sleep(self):
        print(f"{self.name} lies down to sleep...")

    def eat(self):
        print(f"{self.name} brings food to their mouth with their trunk...")

    def move(self):
        print(f"{self.name} stomps around...")