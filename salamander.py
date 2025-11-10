'''
File: salamander.py
Description: A module defining a class that represents a salamander.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from amphibian import Amphibian


class Salamander(Amphibian):
    '''
    A class which represents a salamander and inherits from the Amphibian class.

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
        environment_types : A list of strings indicating which environments the animal can live in. Set to ["tropical", "forest", "freshwater aquatic", "wetland"].
        enclosure : Shows what zoo enclosure, if any, the animal is currently in (either None or an object of Enclosure class).

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

        swim() : Displays a statement about how the animal swims.

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
    '''

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self._Animal__environment_types.append("tropical")
        self._Animal__environment_types.append("forest")
        self._Animal__environment_types.append("freshwater aquatic")
        self._Animal__environment_types.append("wetland")

    def cry(self) -> None:
        print("*quiet clicking and squeaks*")

    def sleep(self) -> None:
        print(f"{self.name} sleeps during the day...")

    def eat(self) -> None:
        print(f"{self.name} munches on grubs...")

    def move(self) -> None:
        print(f"{self.name} crawls around...")

    def swim(self) -> None:
        print(f"{self.name} wiggles around in the water...")
