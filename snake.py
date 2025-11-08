'''
File: snake.py
Description: A module defining a class that represents a snake.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from reptile import Reptile


class Snake(Reptile):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._Animal__environment_types.append("tropical")
        self._Animal__environment_types.append("grassland")
        self._Animal__environment_types.append("desert")
        self._Animal__environment_types.append("forest")
        self._Animal__environment_types.append("wetland")

    def cry(self):
        print("*hissss*")

    def sleep(self):
        print(f"{self.name} curls up to sleep...with eyes open...")

    def eat(self):
        print(f"{self.name} swallows food whole...")

    def move(self):
        print(f"{self.name} slithers...")
