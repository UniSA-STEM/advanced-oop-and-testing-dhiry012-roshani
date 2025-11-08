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
    def feed_animals(self, enclosure):
        try:
            if self.enclosures == []:
                print(f"{self.name} is not assigned to any enclosures")
            elif enclosure.id == "":
                pass  # Ensure error is thrown if enclosure not valid object.
            elif enclosure not in self.enclosures:
                print(f"{self.name} is not assigned that that enclosure.")
            else:
                if enclosure.animals == []:
                    print("Enclosure is empty.")
                else:
                    for animal in enclosure.animals:
                        animal.eat()
                        enclosure.reduce_cleanliness(0.5)
        except AttributeError:
            print("Invalid enclosure.")

    def clean_enclosure(self, enclosure):
        try:
            if self.enclosures == []:
                print(f"{self.name} is not assigned to any enclosures.")
            elif enclosure in self.enclosures:
                enclosure.clean(self)
            else:
                check = enclosure.id
                print(f"{self.name} is not assigned to this enclosure.")
        except AttributeError:
            print("Invalid enclosure.")