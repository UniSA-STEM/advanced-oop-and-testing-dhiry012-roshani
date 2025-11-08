'''
File: hippopotamus.py
Description: A module defining a class that represents a hippopotamus.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal


class Hippopotamus(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._Animal__environment_types.append("tropical")
        self._Animal__environment_types.append("grassland")
        self._Animal__environment_types.append("freshwater aquatic")
        self._Animal__environment_types.append("wetland")

    def cry(self):
        print("*grunt grunt honk*")

    def sleep(self):
        print(f"{self.name} sinks underwater to sleep...")

    def eat(self):
        print(f"{self.name} chomps on some grass...")

    def move(self):
        print(f"{self.name} trots along...even underwater...")