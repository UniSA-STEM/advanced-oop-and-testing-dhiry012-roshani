'''
File: salamander.py
Description: A module defining a class that represents a salamander.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from amphibian import Amphibian


class Salamander(Amphibian):
    def cry(self):
        print("*quiet clicking and squeaks*")

    def sleep(self):
        print(f"{self.name} sleeps during the day...")

    def eat(self):
        print(f"{self.name} munches on grubs...")

    def move(self):
        print(f"{self.name} crawls around...")

    def swim(self):
        print(f"{self.name} wiggles around in the water...")