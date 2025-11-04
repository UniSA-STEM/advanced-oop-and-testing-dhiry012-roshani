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
    def cry(self):
        print("*hissss*")

    def sleep(self):
        print(f"{self.name} curls up to sleep...with eyes open...")

    def eat(self):
        print(f"{self.name} swallows food whole...")

    def move(self):
        print(f"{self.name} slithers...")
