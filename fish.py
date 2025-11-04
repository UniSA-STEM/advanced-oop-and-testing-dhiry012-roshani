'''
File: fish.py
Description: A module defining an abstract class that represents a fish.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import abstractmethod
from animal import Animal


class Fish(Animal):
    def __init__(self, name, age, freshwater=False, saltwater=False):
        self.__freshwater = None
        self.__saltwater = None
        super().__init__(name, age)

        self.set_freshwater(freshwater)
        self.set_saltwater(saltwater)

    def get_freshwater(self):
        '''Returns a boolean value indicating if the fish can live in freshwater.'''
        return self.__freshwater

    def set_freshwater(self, freshwater):
        '''
        Takes a boolean parameter indicating if the fish can live in freshwater.
        If the given argument is a valid boolean value, it is set as the freshwater attribute.
        This method returns nothing.
        '''
        if type(freshwater) == bool:
            self.__freshwater = freshwater

    def get_saltwater(self):
        '''Returns a boolean value indicating if the fish can live in saltwater.'''
        return self.__saltwater

    def set_saltwater(self, saltwater):
        '''
        Takes a boolean parameter indicating if the fish can live in saltwater.
        If the given argument is a valid boolean value, it is set as the saltwater attribute.
        This method returns nothing.
        '''
        if type(saltwater) == bool:
            self.__saltwater = saltwater

    @abstractmethod
    def swim(self):
        '''Displays a statement about how the animal swims.'''
        pass

    # Properties
    freshwater = property(get_freshwater, set_freshwater)
    saltwater = property(get_saltwater, set_saltwater)

    # Override Animal string method.
    def __str__(self):
        treatment_statement = f"{self.name} is undergoing treatment.\n" if self.under_treatment else ""

        if not self.saltwater and not self.freshwater:
            water_statement = f"{self.name} can live in neither saltwater nor freshwater."
        elif self.saltwater and self.freshwater:
            water_statement = f"{self.name} can live in both saltwater and freshwater."
        else:
            water_statement = f"{self.name} is a {"saltwater" if self.saltwater else "freshwater"} fish."

        return (f"\n---ANIMAL DETAILS---\nName: {self.name}\nAge: {self.age}\nSpecies: {self.species}\n"
                f"{self.dietary_needs}\n{treatment_statement}{water_statement}\n---------")