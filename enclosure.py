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
        self.__species = None

        self.set_size(area)
        self.set_environmental_type(environmental_type)

    def get_id(self):
        '''Returns an integer of the enclosure's id number.'''
        return self.__id

    def __create_id(self):
        '''Returns an integer for the object's id number.'''
        temp = self.__next_id
        self.__next_id += 1
        return temp

    def get_size(self):
        '''Returns an integer or float of the enclosures area.'''
        return self.__size

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

    def get_environmental_type(self):
        '''Returns a string of the enclosure's environmental type.'''
        return self.__environmental_type

    def set_environmental_type(self, environment):
        '''
        Sets the environment type for the enclosure, if the given argument is in the list of valid environment types.
        Else, prints an error message.
        '''
        if environment in self.__valid_environmental_types:
            self.__environmental_type = environment
        else:
            print("Invalid environmental type.")

    def get_cleanliness_level(self):
        '''Returns an integer of the enclosure's current cleanliness level (0-10).'''
        return self.__cleanliness_level

    def get_staff(self):
        '''Returns a list of the staff members assigned to the enclosure.'''
        return self.__staff

    def get_animals(self):
        '''Returns a list of the animals currently in the enclosure.'''
        return self.__animals

    def get_species(self):
        '''Returns a string of what species of animal is currently being housed in the enclosure'''
        return self.__species

    def add_animal(self, animal):
        '''Adds an animal to the enclosure.'''
        try:
            if self.environmental_type is None:
                print("Environment type not set. Cannot add animal.")
            elif self.species is not None and self.species != animal.species:
                print(f"Animal is not {self.species}. Cannot add to enclosure.")
            elif self.environmental_type not in animal.environment_types:
                print(f"Enclosure type ({self.environmental_type}) incompatible with animal's requirements.")
            elif animal in self.animals:
                print("Animal already in this enclosure.")
            elif animal.enclosure is not None:
                print("Animal is already in another enclosure.")
            else:
                if self.species is None:
                    self.__species = animal.species
                self.__animals.append(animal)
                animal.add_to_enclosure(self)
                print(f"{animal.name} added to enclosure.")
        except AttributeError:
            print("Invalid animal.")

    def remove_animal(self, animal):
        try:
            if animal.name == "":
                pass  # Ensure exception is thrown if not type Animal.
            if animal not in self.animals:
                print("Animal is not in this enclosure.")
            else:
                self.__animals.remove(animal)
                animal.remove_from_enclosure(self)
                print(f"{animal.name} removed from enclosure.")
        except AttributeError:
            print("Invalid animal.")

    id = property(get_id)
    size = property(get_size, set_size)
    environmental_type = property(get_environmental_type, set_environmental_type)
    cleanliness_level = property(get_cleanliness_level)
    staff = property(get_staff)
    animals = property(get_animals)
    species = property(get_species)
