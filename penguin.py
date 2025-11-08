'''
File: penguin.py
Description: A module defining a class that represents a penguin.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from bird import Bird


class Penguin(Bird):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._Animal__environment_types.append("saltwater aquatic")
        self._Animal__environment_types.append("arctic")

    def cry(self):
        print("*braying honking squawking*")

    def sleep(self):
        print(f"{self.name} tucks in beak to doze...")

    def eat(self):
        print(f"{self.name} swallows fish whole...")

    def move(self):
        print(f"{self.name} waddles and shuffles along...")

    def fly(self):
        print(f"{self.name} flaps wings ineffectually...")

    def swim(self):
        print(f"{self.name} darts through the water...")