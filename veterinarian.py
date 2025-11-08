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
    def heal(self):
        print(f"{self.name} is healing the animals...")