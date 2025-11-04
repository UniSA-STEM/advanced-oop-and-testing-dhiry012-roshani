'''
File: amphibian.py
Description: A module defining an abstract class that represents an amphibian.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import abstractmethod
from animal import Animal


class Amphibian(Animal):
    @abstractmethod
    def move(self):
        '''Displays a statement about how the animal moves.'''
        pass

    @abstractmethod
    def swim(self):
        '''Displays a statement about how the animal swims.'''
        pass