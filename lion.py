'''
File: mammal.py
Description: A module defining an abstract class that represents a mammal.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal


class Lion(Mammal):
    def cry(self):
        print("*Roaarrrr!!*")

    def sleep(self):
        print(f"{self.__name} lies down to sleep...")

    def eat(self):
        print(f"{self.__name} munches on meat")

    def move(self):
        print(f"{self.__name} prowls...")