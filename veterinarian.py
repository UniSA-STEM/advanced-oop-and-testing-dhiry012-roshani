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
    def health_check(self, enclosure):
        try:
            if self.enclosures == []:
                print(f"{self.name} is not assigned to any enclosures")
            elif enclosure.id == "":
                pass  # Ensure error is thrown if enclosure not valid object.
            elif enclosure not in self.enclosures:
                print(f"{self.name} is not assigned that that enclosure.")
            else:
                print(f"-----ENCLOSURE {enclosure.id} HEALTH CHECK-----")
                if enclosure.animals == []:
                    print("Enclosure empty")
                else:
                    for animal in enclosure.animals:
                        animal.report()
        except AttributeError:
            print("Invalid enclosure.")