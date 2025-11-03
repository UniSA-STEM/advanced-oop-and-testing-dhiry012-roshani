'''
File: mammal.py
Description: A module defining an abstract class that represents a mammal.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import abstractmethod
from animal import Animal


class Mammal(Animal):
    @abstractmethod
    def move(self):
        '''Displays how the animal moves.'''
        pass