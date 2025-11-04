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
    def cry(self):
        print("*trumpets!*")

    def sleep(self):
        print(f"{self.name} lies down to sleep...")

    def eat(self):
        print(f"{self.name} brings food to their mouth with their trunk...")

    def move(self):
        print(f"{self.name} stomps around...")