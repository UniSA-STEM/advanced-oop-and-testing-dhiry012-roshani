'''
File: bird.py
Description: A module defining an abstract class that represents a bird.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import abstractmethod
from animal import Animal


class Bird(Animal):
    @abstractmethod
    def move(self):
        '''Displays a statement about how the animal moves.'''
        pass

    @abstractmethod
    def fly(self):
        '''Displays a statement about how the animal flies.'''
        pass