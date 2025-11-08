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
    def train(self):
        print(f"{self.name} is training the animals...")