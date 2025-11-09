'''
File: turtle.py
Description: A module defining a class that represents a turtle.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from reptile import Reptile


class Turtle(Reptile):
    '''
    A class which represents a turtle and inherits from the Reptile class.

    Parameters:
        name : A string representing the name of the animal.
        age : An integer representing the age of the animal in years.

    Attributes:
        id : An integer unique to this animal object (not shared by other objects which inherit this class).
        species : The species of the animal (the class name).
        name : Name of the animal.
        age : Age of the animal in years (integer only).
        dietary needs : A list of the animal's dietary needs (a list of strings).
        under_treatment : A boolean value indicating whether the animal is currently undergoing treatment.
        environment_types : A list of strings indicating which environments the animal can live in.
        enclosure : Shows what zoo enclosure, if any, the animal is currently in (either None or an object of Enclosure class).
        freshwater : A boolean value indicating if the turtle can live in freshwater.
        saltwater : A boolean value indicating if the turtle can live in saltwater.

    Methods:
        set_name(name) : Changes the animal's name.

        set_age(age) : Changes the animal's age.

        get_name() : Returns the animal's name.

        get_age() : Returns the animal's age.

        get_species() : Returns the animal's species (class name).

        get_under_treatment() : Returns Boolean indicating if animal is under treatment.

        set_under_treatment(under_treatment) : Changes the animal's under_treatment attribute.

        get_dietary_needs() : Returns a formatted string of the animal's dietary needs list.

        add_dietary_need(dietary_need) : Adds the specified dietary need to the animal's list.

        remove_dietary_need(index) : Removes a dietary need at a specified position (index).

        get_id() : Returns the animal's id number.

        get_environment_types() : Returns a list of the environments the animal can live in.

        get_freshwater() : Returns a boolean value indicating if the turtle can live in freshwater.

        set_freshwater(freshwater) : Updates the turtle's freshwater attribute.

        get_saltwater() : Returns a boolean value indicating if the turtle can live in saltwater.

        set_saltwater(saltwater) : Updates the turtle's saltwater attribute.

        add_note(category, description, date_reported, severity, notes, treatment) : Adds a note with the specified details to the animal's record.

        remove_note(category, index, treatment) : Removes a specified note from the animal's record.

        report() : Displays the animal's current notes.

        species_report() : Displays a report for each animal which shares the target animal's species.

        animals_report() : Displays a report for all instantiated animals.

        get_enclosure() : Returns None (if animal not in enclosure) or an Enclosure object (the animal is currently in that enclosure).

        add_to_enclosure(enclosure) : Updates the animal's enclosure attribute.

        remove_from_enclosure(enclosure) : Updates the animal's enclosure attribute.

        cry() : Must display a message showing what sound the animal makes.

        sleep() : Must display a message about how the animal sleeps.

        eat() : Must display a message about how/what the animal eats.

        move() : Displays a statement about how the animal moves.

        __eq__(other) : Determines if the object and another specified object are equal.

        __str__() : Displays the animal's details.

    Properties:
        id : get_id()

        name : get_name(), set_name()

        age : get_age(), set_age()

        species : get_species()

        dietary_needs : get_dietary_needs()

        under_treatment : get_under_treatment(), set_under_treatment()

        environment_types : get_environment_types()

        enclosure : get_enclosure()

        freshwater : get_freshwater(), set_freshwater()

        saltwater : get_saltwater(), set_saltwater()
    '''

    def __init__(self, name:str, age:int, freshwater=False, saltwater=False) -> None:
        self.__freshwater = False  # Create freshwater attribute.
        self.__saltwater = False   # Create saltwater attribute.
        super().__init__(name, age)

        # Validate boolean values.
        self.set_freshwater(freshwater)
        self.set_saltwater(saltwater)

    def cry(self) -> None:
        print("*chirp growl wheeze*")

    def sleep(self) -> None:
        print(f"{self.name} retreats into shell to sleep...")

    def eat(self) -> None:
        print(f"{self.name} bites into food...")

    def move(self) -> None:
        print(f"{self.name} crawls and shuffles...")

    def swim(self) -> None:
        print(f"{self.name} paddles through the water...")

    def get_freshwater(self) -> bool:
        '''
        Returns:
            boolean

        Returns a boolean value indicating if the turtle can live in freshwater.
        '''
        return self.__freshwater

    def set_freshwater(self, freshwater:bool) -> None:
        '''
        Parameters:
            freshwater : A boolean value indicating if the turtle can live in freshwater.

        Returns:
            None

        If the provided value is valid (boolean), updates the turtle's freshwater attribute.
        If freshwater is set to True and freshwater aquatic is not in the environment types list, adds it to list.
        If freshwater is set to False and freshwater aquatic is in the environment types list, removes it from list.
        If it is invalid, prints an error message.
        '''
        if type(freshwater) == bool:
            # Update attribute.
            self.__freshwater = freshwater

            # Add environment type, if True and not in list.
            if self.freshwater == True and "freshwater aquatic" not in self.environment_types:
                self._Animal__environment_types.append("freshwater aquatic")

            # Remove environment type, if False and in list.
            if self.freshwater == False and "freshwater aquatic" in self.environment_types:
                self._Animal__environment_types.remove("freshwater aquatic")
        else:
            print("Invalid value. Must be True or False")

    def get_saltwater(self) -> bool:
        '''
        Returns:
            boolean

        Returns a boolean value indicating if the turtle can live in saltwater.
        '''
        return self.__saltwater

    def set_saltwater(self, saltwater:bool) -> None:
        '''
        Parameters:
            saltwater : A boolean value indicating if the turtle can live in saltwater.

        Returns:
            None

        If the provided value is valid (boolean), updates the turtle's saltwater attribute.
        If saltwater is set to True and saltwater aquatic is not in the environment types list, adds it to list.
        If saltwater is set to False and saltwater aquatic is in the environment types list, removes it from list.
        If it is invalid, prints an error message.
        '''
        if type(saltwater) == bool:
            # Update attribute.
            self.__saltwater = saltwater

            # Add environment type, if True and not in list.
            if self.saltwater == True and "saltwater aquatic" not in self.environment_types:
                self._Animal__environment_types.append("saltwater aquatic")

            # Remove environment type, if False and in list.
            if self.saltwater == False and "saltwater aquatic" in self.environment_types:
                self._Animal__environment_types.remove("saltwater aquatic")
        else:
            print("Invalid value. Must be True or False")

    # Properties
    freshwater = property(get_freshwater, set_freshwater)
    saltwater = property(get_saltwater, set_saltwater)