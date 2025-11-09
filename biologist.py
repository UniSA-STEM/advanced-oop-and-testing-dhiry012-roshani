'''
File: biologist.py
Description: A module defining a class that represents a biologist.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff


class Biologist(Staff):
    '''
    A class which represents a Biologist and inherits from the Staff class.

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

        add_to_enclosure(enclosure) : Adds enclosure to staff's enclosure list.

        remove_from_enclosure(enclosure) : Removes enclosure from staff's enclosure list.

        research(enclosure) : Conducts research on the animals in the enclosure.

        __eq__(other) : Determines if the staff is equal to another.

        __str__() : Returns a string of the staff's details.

    Properties:
        id : get_id()
        name : get_name(), set_name()
        enclosures : get_enclosures()
        role : get_role()
    '''

    def research(self, enclosure) -> None:
        '''
        Parameters:
             enclosure: An Enclosure object in which to research the animals.

        Returns:
            None

        Conducts research on the animals in the enclosure. This displays each animal's details.
        If there are no animals in the enclosure, displays "Enclosure is empty".
        If the Biologist is not assigned the enclosure, displays error message.
        If the enclosure is invalid, displays error message.
        '''
        try:
            check = enclosure.cleanliness_level  # Throw an Exception if not Enclosure object.

            if enclosure not in self.enclosures:
                print(f"{self.name} is not assigned that that enclosure.")
            else:
                print(f"-----ENCLOSURE {enclosure.id} RESEARCH-----")
                if enclosure.animals == []:
                    print("Enclosure is empty.")
                else:
                    for animal in enclosure.animals:
                        print(animal)
        except AttributeError:
            print("Invalid enclosure.")