'''
File: owl.py
Description: A module defining a class that represents an owl.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from bird import Bird


class Owl(Bird):
    def cry(self):
        print("*hoot hoot*")

    def sleep(self):
        print(f"{self.name} sleeps in the daytime...")

    def eat(self):
        print(f"{self.name} tears into food...")

    def move(self):
        print(f"{self.name} hops and struts along...")

    def fly(self):
        print(f"{self.name} glides silently...")
