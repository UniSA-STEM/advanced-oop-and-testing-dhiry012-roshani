'''
File: veterinarian.py
Description: A module defining a class that represents a veterinarian.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff


class Veterinarian(Staff):
    '''
    A class which represents a Veterinarian and inherits from the Staff class.

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

        health_check(enclosure) : Conducts a health check on the animals in an enclosure.

        __eq__(other) : Determines if the staff is equal to another.

        __str__() : Returns a string of the staff's details.

    Properties:
        id : get_id()

        name : get_name(), set_name()

        enclosures : get_enclosures()

        role : get_role()

        duties : get_duties()
    '''

    def __init__(self, name:str) -> None:
        super().__init__(name)
        self._duties.append("health")

    def health_check(self, enclosure) -> None:
        '''
         Paremeters:
            enclosure: An Enclosure class on which to conduct a health check.

        Returns:
            None

        Conducts a health check on the animals in an enclosure. This displays a report for each animal.
        If there are no animals in the enclosure, displays "Enclosure is empty".
        If the Veterinarian is not assigned the enclosure, displays error message.
        If the enclosure is invalid, displays error message.
        '''
        try:
            # Get all staff assigned to health duties in the enclosure.
            health_staff = enclosure.staff.get("health")

            if enclosure not in self.enclosures:
                print(f"{self.name} is not assigned to that enclosure.")
            elif self not in health_staff:
                print(f"{self.name} is not assigned health duties for that enclosure.")
            else:
                print(f"-----ENCLOSURE {enclosure.id} HEALTH CHECK-----")
                if enclosure.animals == []:
                    print("Enclosure empty")
                else:
                    for animal in enclosure.animals:
                        animal.report()
        except AttributeError:
            print("Invalid enclosure.")