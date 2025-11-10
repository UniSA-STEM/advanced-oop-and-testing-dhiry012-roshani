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
matthias = Zookeeper()  # Create staff without giving arguments.

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
saphira = Snake()  # Create animal without giving arguments.
toothless = Snake("Toothless", 20)

# Create enclosures.
saltwater_aquarium = Enclosure(150, "saltwater aquatic")
grassland_enclosure_1 = Enclosure(10000, "grassland")
grassland_enclosure_2 = Enclosure(5, "grassland")
wetland_enclosure = Enclosure(2, "wetland")
forest_enclosure = Enclosure()  # Create enclosure without giving arguments.

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
grassland_enclosure_2.add_staff(matthias)  # Staff without name (calls him Staff 6).
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
saltwater_aquarium.add_animal(roach)  # Won't add.

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

forest_enclosure.add_animal(harry)  # Won't add (environmental type not specified).
forest_enclosure.environmental_type = "forest"  # Change environmental type.
forest_enclosure.add_animal(harry)
forest_enclosure.add_animal(ron)
forest_enclosure.add_animal(hermione)

# Enclosure status report.
print(forest_enclosure)

# Staff details.
print(kaz)
print(wylan)

# Add and remove dietary needs.
sam.add_dietary_need("'taters")
sam.add_dietary_need("roast chicken")
smaug.add_dietary_need("dwarves")
toothless.add_dietary_need("no eels")
toothless.remove_dietary_need(0)
print(sam)  # See results.
print(smaug)
print(toothless)

# Add and remove health records notes.
dandelion.add_note("injuries", "bite from another shark", "12/04/2015", "med", "was bitten by Roach", True)
frodo.add_note("behavioural_concerns", "attachment to ring", "05/06/2024", "low", "obsessed with a golden ring")
minho.add_note("behavioural_concerns", "runs everywhere", "01/01/2000", "med",
               "is super quick and runs all over the place")
dandelion.add_note("behavioural_concerns", "noisy", "04/05/1200", "high",
                   "looks like he's trying to sing all the time, annoys Roach a lot")
frodo.remove_note("behavioural_concerns", 0)

# Animal details/reports.
print(saphira)  # Details of animal where name and age not given upon creation.
dandelion.report()
newt.species_report()
hermione.animals_report()

# Manually reduce cleanliness level of enclosure.
saltwater_aquarium.reduce_cleanliness(5.8)
print(saltwater_aquarium.cleanliness_level)  # See level.

# Remove animals from enclosure.
saltwater_aquarium.remove_animal(geralt)
saltwater_aquarium.remove_animal(roach)  # Not in enclosure, will print message.

# Remove staff from enclosure.
saltwater_aquarium.remove_staff(nina, "health")
grassland_enclosure_1.remove_staff(wylan)  # Print's message, as not assigned to enclosure.

# Clean enclosure (2 ways of doing the same thing).
jesper.clean_enclosure(saltwater_aquarium)
saltwater_aquarium.clean(jesper)

# Enclosure status to see updates.
print(saltwater_aquarium)

# Other staff duties in action.
kaz.feed_animals(forest_enclosure)
inej.health_check(wetland_enclosure)
wylan.research(grassland_enclosure_2)
