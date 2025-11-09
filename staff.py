'''
File: staff.py
Description: A module defining an abstract class that represents a general zoo staff member.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC


class Staff(ABC):
    '''
    An abstract class which represents a staff member at a zoo.

    Parameters:
        name : A string representing the staff member's name.

    Attributes:
        id : An integer unique to this staff object (no other staff objects will have the same number).
        name : A string of the staff member's name.
        enclosures : A list of the enclosures the staff members is assigned to.
        role : The staff member's role/job (class name).

    Class Methods:
        get_id() : Returns the staff member's id number.

        get_name() : Returns the staff member's name.

        set_name(name) : Updates the staff's name.

        get_enclosures() : Returns a list of the enclosures the staff member is assigned to.

        get_role() : Returns the staff member's role.

        get_duties() : Returns a list of the staff's duties.

        add_to_enclosure(enclosure) : Adds enclosure to staff's enclosure list.

        remove_from_enclosure(enclosure) : Removes enclosure from staff's enclosure list.

        __eq__(other) : Determines if the staff is equal to another.

        __str__() : Returns a string of the staff's details.

    Abstract Methods:
        None

    Properties:
        id : get_id()

        name : get_name(), set_name()

        enclosures : get_enclosures()

        role : get_role()

        duties : get_duties()
    '''

    # Global attribute.
    __next_id = 1

    def __init__(self, name:str) -> None:
        self.__id = self.__create_id()
        self.__name = ""
        self.__enclosures = []
        self.__role = self.__class__.__name__
        self._duties = ["general"]

        # Validate name.
        self.set_name(name)

    def get_id(self) -> int:
        '''
        Returns:
             integer

        Returns the staff member's id number.
        '''
        return self.__id

    def __create_id(self) -> int:
        '''
        Returns:
            integer

        A private method used when the object is created to create the unique id number.
        '''
        temp = Staff.__next_id
        Staff.__next_id += 1
        return temp

    def get_name(self) -> str:
        '''
        Returns:
             string

        Returns the staff member's name.
        '''
        return self.__name

    def set_name(self, name:str) -> None:
        '''
        Parameters:
            name : A string to which the staff member's name will be changed.

        Returns:
            None

        Updates the staff's name attribute if the name is valid (non-blank string).
        If the name is invalid, displays error message.
        '''
        if self.__name == "" and type(name) != str:
            print("Invalid name. Name set to empty string.")
        elif type(name) == str:
            self.__name = name
        else:
            print("Invalid name.")

    def get_enclosures(self) -> list:
        '''
        Returns:
             list

        Returns a list of the enclosures the staff member is assigned to.
        '''
        return self.__enclosures

    def get_role(self) -> str:
        '''
        Returns:
             string

        Returns the staff member's role.
        '''
        return self.__role

    def get_duties(self) -> list:
        return self._duties

    def add_to_enclosure(self, enclosure) -> None:
        '''
        Parameters:
            enclosure : An Enclosure object, to which the staff will be assigned.

        Returns:
            None

        Assigns the staff to the enclosure.
        Note that this method cannot actually assign a staff member to an enclosure. That must be done using the Enclosure
        object itself. This method is to add the Enclosure object to the staff's enclosure list attribute.

        If the staff is not assigned to the enclosure, displays error message.
        If the enclosure is invalid, displays error message.
        '''
        try:
            # Get list of all staff assigned to enclosure.
            staff_list = []
            for duty_list in enclosure.staff.values():
                for staff in duty_list:
                    staff_list.append(staff)

            if self in staff_list:
                self.__enclosures.append(enclosure)
            else:
                print("Staff is not assigned to enclosure. Must assign staff using enclosure object.")
        except AttributeError:
            print("Invalid enclosure.")

    def remove_from_enclosure(self, enclosure) -> None:
        '''
        Parameters:
            enclosure : An Enclosure object, from which the staff will be removed.

        Returns:
            None

        Removes the staff from the enclosure.
        Note that this method cannot actually remove a staff member from an enclosure. That must be done using the Enclosure
        object itself. This method is to remove the Enclosure object from the staff's enclosure list attribute.

        If the staff is not assigned to the enclosure, displays error message.
        If the enclosure is invalid, displays error message.
        '''
        try:
            check = enclosure.cleanliness_level  # Throw exception if not Enclosure object

            if enclosure in self.enclosures:
                self.__enclosures.remove(enclosure)
            else:
                print("Staff is not assigned to enclosure. Must assign staff using enclosure object.")
        except AttributeError:
            print("Invalid enclosure.")

    id = property(get_id)
    name = property(get_name, set_name)
    enclosures = property(get_enclosures)
    role = property(get_role)
    duties = property(get_duties)

    def __eq__(self, other:Staff) -> bool:
        '''
        Parameters:
            other : Another Staff object to which this object is compared.

        Returns:
            boolean

        Compares two Staff objects and returns True of the objects are equal or False if not.
        The objects are equal if they are both of the Staff class and have the same id number.
        '''
        return isinstance(other, Staff) and self.id == other.id

    def __str__(self) -> str:
        '''
        Returns:
             string

        Returns a string of the staff member's details in the following format:

        ---STAFF DETAILS---
        ID: <id>

        Name: <name>

        Role: <role>

        Enclosures:

        Enclosure #<id>: <num> animals (species: <species>)

        Enclosure #<id>: <num> animals (species: <species>)
        '''
        enclosure_statement = ""
        if self.enclosures == []:
            enclosure_statement += "None"
        else:
            for enclosure in self.enclosures:
                enclosure_statement += (f"\nEnclosure #{enclosure.id}: {len(enclosure.animals)} animals (species: "
                                        f"{enclosure.species})")

        return f"---STAFF DETAILS---\nID: {self.__id}Name: {self.__name}\nRole: {self.role}\nEnclosures: {enclosure_statement}"