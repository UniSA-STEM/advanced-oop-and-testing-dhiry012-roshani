'''
File: main.py
Description: A module demonstrating the use of an object-oriented Zoo Management System.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

# Import statements.
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from biologist import Biologist
from shark import Shark
from elephant import Elephant
from salamander import Salamander
from owl import Owl
from snake import Snake

# Create staff objects.
kaz = Zookeeper("Kaz")
inej = Veterinarian("Inej")
nina = Veterinarian("Nina")
jesper = Zookeeper("Jesper")
wylan = Biologist("Wylan")
Matthias = Zookeeper("Matthias")

# Create animals.
geralt = Shark("Geralt", 61, saltwater=True)
dandelion = Shark("Dandelion", 43, saltwater=True)
yennefer = Shark("Yennefer", 99, saltwater=True)
roach = Shark("Roach", 12, freshwater=True)

frodo = Elephant("Frodo", 50)
sam = Elephant("Sam", 38)
merry = Elephant("Merry", 37)
pippin = Elephant("Pippin", 29)

thomas = Salamander("Thomas", 16)
minho = Salamander("Minho", 17)
newt = Salamander("Newt", 16)

harry = Owl("Harry", 13)
hermione = Owl("Hermione", 13)
ron = Owl("Ron", 13)

smaug = Snake("Smaug the Terrible", 171)
saphira = Snake("Saphira", 2)
toothless = Snake("Toothless", 20)

# Create enclosures.
saltwater_aquarium = Enclosure(150, "saltwater aquatic")
grassland_enclosure_1 = Enclosure(10000, "grassland")
grassland_enclosure_2 = Enclosure(5, "grassland")
wetland_enclosure = Enclosure(2, "wetland")
forest_enclosure = Enclosure(100, "forest")
