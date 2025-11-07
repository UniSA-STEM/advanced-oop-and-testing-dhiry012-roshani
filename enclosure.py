'''
File: enclosure.py
Description: A module defining a class that represents a zoo enclosure.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Enclosure:
    __next_id = 1
    __valid_environmental_types = ["tropical", "grassland", "desert", "forest", "freshwater aquatic", "saltwater aquatic",
                                   "mountainous", "wetland", "arctic"]

    def __init__(self, area, environmental_type):
        self.__id = self.__create_id()
        self.__size = None
        self.__environmental_type = None
        self.__cleanliness_level = 10
        self.__MAX_CLEANLINESS_LEVEL = 10
        self.__staff = []
        self.__animals = []

        self.set_size(area)
        self.set_environmental_type(environmental_type)

    def __create_id(self):
        '''Returns an integer for the object's id number.'''
        temp = self.__next_id
        self.__next_id += 1
        return temp

    def set_size(self, area):
        '''
        Sets the size of the enclosure (area). Takes one parameter. If the given argument is an integer or float,
        sets the size of the enclosure to the argument.
        Else, prints an error message.
        '''
        if type(area) == int or type(area) == float:
            self.__size = area
        else:
            print("Invalid area for enclosure.")

    def set_environmental_type(self, environment):
        '''
        Sets the environment type for the enclosure, if the given argument is in the list of valid environment types.
        Else, prints an error message.
        '''
        if environment in self.__valid_environmental_types:
            self.__environmental_type = environment
        else:
            print("Invalid environmental type.")