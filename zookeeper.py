'''
File: zookeeper.py
Description: A module defining a class that represents a zookeeper.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff


class Zookeeper(Staff):
    '''
    A class which represents a Zookeeper and inherits from the Staff class.

    Parameters:
        name : A string representing the staff member's name.

    Attributes:
        id : An integer unique to this staff object (no other staff objects will have the same number).
        name : A string of the staff member's name.
        enclosures : A list of the enclosures the staff members is assigned to.
        role : The staff member's role/job (class name).

    Methods:
        get_id() : Returns the staff member's id number.

        get_name() : Returns the staff member's name.

        set_name(name) : Updates the staff's name.

        get_enclosures() : Returns a list of the enclosures the staff member is assigned to.

        get_role() : Returns the staff member's role.

        get_duties() : Returns a list of the staff's duties.

        add_to_enclosure(enclosure) : Adds enclosure to staff's enclosure list.

        remove_from_enclosure(enclosure) : Removes enclosure from staff's enclosure list.

        feed_animals(enclosure) : Feed the animals in the specified enclosure.

        clean_enclosure(enclosure) : Cleans an enclosure, increasing the cleanliness level.

        __eq__(other) : Determines if the staff is equal to another.

        __str__() : Returns a string of the staff's details.

    Properties:
        id : get_id()

        name : get_name(), set_name()

        enclosures : get_enclosures()

        role : get_role()

        duties : get_duties()
    '''

    def __init__(self, name="") -> None:
        super().__init__(name)
        self._duties.append("feeding")
        self._duties.append("cleaning")

    def feed_animals(self, enclosure) -> None:
        '''
        Parameters:
             enclosure : An Enclosure object in which to feed the animals.

        Returns:
            None

        Feed the animals in the specified enclosure. This displays each animal's eat method and reduces the enclosure's
        cleanliness by 0.5 for each animal.
        If the Zookeeper is not assigned to the enclosure or there are no animals in the enclosure, displays error
        message.
        If the enclosure is not valid, displays error message.
        '''
        try:
            # Get all staff assigned to feeding duties in the enclosure.
            feeding_staff = enclosure.staff.get("feeding")

            if enclosure not in self.enclosures:
                print(f"{self.name} is not assigned to that enclosure.")
            elif self not in feeding_staff:
                print(f"{self.name} is not assigned feeding duties for that enclosure.")
            elif enclosure.animals == []:
                print("Enclosure is empty.")
            else:
                for animal in enclosure.animals:
                    animal.eat()
                    enclosure.reduce_cleanliness(0.5)
        except AttributeError:
            print("Invalid enclosure.")

    def clean_enclosure(self, enclosure) -> None:
        '''
        Parameters:
             enclosure : An Enclosure object to clean.

        Returns:
            None

        Cleans an enclosure, increasing the cleanliness level.
        If the Zookeeper is not assigned to the enclosure, displays error message.
        If the enclosure is not valid, displays error message.
        '''
        try:
            # Get all staff assigned to cleaning duties in the enclosure.
            cleaning_staff = enclosure.staff.get("cleaning")

            if enclosure not in self.enclosures:
                print(f"{self.name} is not assigned to that enclosure.")
            elif self not in cleaning_staff:
                print(f"{self.name} is not assigned cleaning duties for that enclosure.")
            else:
                enclosure.clean(self)
        except AttributeError:
            print("Invalid enclosure.")
