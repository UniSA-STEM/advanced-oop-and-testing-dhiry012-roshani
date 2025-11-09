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
matthias = Zookeeper("Matthias")

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

# Assign staff to enclosures.
saltwater_aquarium.add_staff(inej, "health")
saltwater_aquarium.add_staff(nina, "health")
saltwater_aquarium.add_staff(kaz, "feeding")
saltwater_aquarium.add_staff(jesper, "feeding")
saltwater_aquarium.add_staff(jesper, "cleaning")

grassland_enclosure_1.add_staff(nina, "health")
grassland_enclosure_1.add_staff(kaz, "feeding")
grassland_enclosure_1.add_staff(jesper, "feeding")
grassland_enclosure_1.add_staff(inej)

grassland_enclosure_2.add_staff(kaz, "feeding")
grassland_enclosure_2.add_staff(matthias)
grassland_enclosure_2.add_staff(wylan, "health")  # Won't assign
grassland_enclosure_2.add_staff(wylan, "research")

wetland_enclosure.add_staff(nina, "health")
wetland_enclosure.add_staff(inej, "health")
wetland_enclosure.add_staff(wylan, "research")
wetland_enclosure.add_staff(wylan, "research")  # Won't assign.
wetland_enclosure.add_staff(kaz, "feeding")

forest_enclosure.add_staff(inej, "feeding")  # Won't assign.
forest_enclosure.add_staff(inej, "health")
forest_enclosure.add_staff(kaz)
forest_enclosure.add_staff(kaz, "feeding")
forest_enclosure.add_staff(wylan, "research")

# Assign animals to enclosures.
saltwater_aquarium.add_animal(geralt)
saltwater_aquarium.add_animal(yennefer)
saltwater_aquarium.add_animal(dandelion)
saltwater_aquarium.add_animal(roach)

grassland_enclosure_1.add_animal(frodo)
grassland_enclosure_1.add_animal(frodo)  # Won't add.
grassland_enclosure_1.add_animal(sam)
grassland_enclosure_1.add_animal(merry)
grassland_enclosure_1.add_animal(pippin)
grassland_enclosure_1.add_animal(smaug)  # Won't add.

grassland_enclosure_2.add_animal(smaug)
grassland_enclosure_2.add_animal(saphira)
toothless.under_treatment = True
grassland_enclosure_2.add_animal(toothless)  # Won't add.

wetland_enclosure.add_animal(thomas)
wetland_enclosure.add_animal(minho)
wetland_enclosure.add_animal(newt)

forest_enclosure.add_animal(harry)
forest_enclosure.add_animal(ron)
forest_enclosure.add_animal(hermione)

# Enclosure status reports.
print(saltwater_aquarium)
print(grassland_enclosure_1)
print(grassland_enclosure_2)
print(wetland_enclosure)
print(forest_enclosure)

# Staff details.
print(kaz)
print(wylan)

# Animal details/reports.
print(smaug)
sam.report()
newt.species_report()
hermione.animals_report()