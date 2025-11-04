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
    def cry(self):
        print("*grunt grunt honk*")

    def sleep(self):
        print(f"{self.name} sinks underwater to sleep...")

    def eat(self):
        print(f"{self.name} chomps on some grass...")

    def move(self):
        print(f"{self.name} trots along...even underwater...")