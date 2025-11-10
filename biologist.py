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

        get_duties() : Returns a list of the staff's duties.

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

        duties : get_duties()
    '''

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._duties.append("research")

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
            # Get all staff assigned to research duties in the enclosure.
            research_staff = enclosure.staff.get("research")

            if enclosure not in self.enclosures:
                print(f"{self.name} is not assigned to that enclosure.")
            elif self not in research_staff:
                print(f"{self.name} is not assigned research duties for that enclosure.")
            else:
                print(f"-----ENCLOSURE {enclosure.id} RESEARCH-----")
                if enclosure.animals == []:
                    print("Enclosure is empty.")
                else:
                    for animal in enclosure.animals:
                        print(animal)
        except AttributeError:
            print("Invalid enclosure.")
