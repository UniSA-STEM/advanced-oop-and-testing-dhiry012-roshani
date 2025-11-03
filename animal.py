'''
File: animal.py
Description: A module defining an abstract class that represents a general zoo animal.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.__name = self.__class__.__name__
        self.__age = None
        self.__dietary_needs = []

        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        '''
        Takes a string as a parameter.
        If the name is valid (letters only), sets the name attribute to the given string.
        If the name is invalid, prints an error message.
        '''
        if name.isalpha():
            self.__name = name
        else:
            print("Invalid name.")

    def set_age(self, age):
        '''
        Takes one parameter.
        If the argument is a positive integer, sets the argument as the animal's age.
        If the argument is invalid, prints an error message.
        '''
        if type(age) == int and age > 0:
            self.__age = age
        elif type(age) == int and age <= 0:
            print("Age must be greater than 0.")
        else:
            print("Invalid age. Must be a whole number.")

    def get_name(self):
        '''Returns a string of the animal's name.'''
        return self.__name

    def get_age(self):
        '''Returns the animal's age, or "Age not specified" if age is None.'''
        return self.__age if self.__age is not None else "Age not specified"

    @abstractmethod
    def cry(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    # Properties
    name = property(get_name, set_name)
    age = property(get_age, set_age)
