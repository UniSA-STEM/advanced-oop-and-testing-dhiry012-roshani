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
    def research(self):
        print(f"{self.name} is researching the animals...")