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
    __next_id = 1

    def __init__(self, name):
        self.__id = self.__create_id()
        self.__name = ""
        self.__enclosures = []
        self.__role = self.__class__.__name__

        self.set_name(name)

    def get_id(self):
        return self.__id

    def __create_id(self):
        '''Returns an integer for the object's id number.'''
        temp = Staff.__next_id
        Staff.__next_id += 1
        return temp

    def get_name(self):
        return self.__name

    def set_name(self, name):
        '''
        Takes a string as a parameter.
        If the name is valid (letters only), sets the name attribute to the given string.
        If the name is invalid, prints an error message.
        If the name attribute is an empty string (eg when the object is instantiated), specifies in message that
        the name is now an empty string.
        '''
        if name.isalpha():
            self.__name = name
        elif self.__name == "":
            print("Invalid name. Name set to empty string.")
        else:
            print("Invalid name.")

    def get_enclosures(self):
        return self.__enclosures

    def get_role(self):
        return self.__role

    def add_to_enclosure(self, enclosure):
        try:
            if self not in enclosure.staff.values():
                print("Staff is not assigned to enclosure. Must assign staff using enclosure object.")
            else:
                self.__enclosures.append(enclosure)
        except AttributeError:
            print("Invalid enclosure.")

    def remove_from_enclosure(self, enclosure):
        try:
            if enclosure.id == "":
                pass
            elif enclosure not in self.enclosures:
                print("Staff is not assigned to this enclosure.")
            else:
                self.__enclosures.remove(enclosure)
        except AttributeError:
            print("Invalid enclosure.")

    id = property(get_id)
    name = property(get_name, set_name)
    enclosures = property(get_enclosures)
    role = property(get_role)

    def __str__(self):
        return (f"---STAFF: {self.__class__.__name__}---\nName: {self.__name}"
                f"\nID: {self.__id}\nEnclosures:")  # Complete once Enclosure class created.