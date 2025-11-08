'''
File: lion.py
Description: A module defining a class that represents a lion.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal


class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._Animal__environment_types.append("grassland")

    def cry(self):
        print("*Roaarrrr!!*")

    def sleep(self):
        print(f"{self.name} lies down to sleep...")

    def eat(self):
        print(f"{self.name} munches on meat")

    def move(self):
        print(f"{self.name} prowls...")

lion = Lion("Leo", 3)
print(lion)