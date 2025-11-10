'''
File: test_enclosure.py
Description: A module defining a class that uses pytest to test the outputs of the enclosure module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from enclosure import Enclosure
from turtle import Turtle  # To test enclosures with animals.
from shark import Shark  # To test enclosures with animals.
from zookeeper import Zookeeper  # To test adding and removing staff.
from biologist import Biologist  # To test clean method.


# IMPORTANT NOTE
# As with the test_animal module, I include two output options for the outputs which include id numbers: one for running
# "pytest test_staff.py" in the Terminal window and one for "pytest".


class TestEnclosure:
    @pytest.fixture
    def enclosure(self):
        return Enclosure(50, "freshwater aquatic")

    @pytest.fixture
    def enclosure2(self):
        return Enclosure(50, "freshwater aquatic")

    @pytest.fixture
    def enclosure_no_environment(self):
        return Enclosure(50, "")

    @pytest.fixture
    def turtle(self):
        return Turtle("Sue", 12, freshwater=True)

    @pytest.fixture
    def shark(self):
        return Shark("Bill", 500, freshwater=True)

    @pytest.fixture
    def zookeeper(self):
        return Zookeeper("Steve")

    @pytest.fixture
    def biologist(self):
        return Biologist("Susan")

    # Test list of valid environmental types.
    def test_get_valid_environmental_types(self, enclosure):
        assert enclosure.valid_environmental_types == ["tropical", "grassland", "desert", "forest", "freshwater aquatic",
                                                       "saltwater aquatic", "mountainous", "wetland", "arctic"]

    # Test get_id method (through property).
    def test_get_id(self, enclosure):
        assert enclosure.id == 2 or enclosure.id == 9

    # Test get_size method (through property).
    def test_get_size(self, enclosure):
        assert enclosure.size == 50

    # Test set_size method to an integer (through property).
    def test_set_size_int(self, enclosure):
        enclosure.size = 60
        assert enclosure.size == 60

    # Test set_size method to a float (through property).
    def test_set_size_float(self, enclosure):
        enclosure.size = 54.9
        assert enclosure.size == 54.9

    # Test set_size method with invalid amount.
    def test_set_size_invalid(self, enclosure, capsys):
        enclosure.size = "30"
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid area for enclosure."
        assert enclosure.size == 50

    # Test get_environmental_type method (through property).
    def test_get_environmental_type(self, enclosure):
        assert enclosure.environmental_type == "freshwater aquatic"

    # Test set_environmental_type.
    def test_set_environmental_type(self, enclosure):
        enclosure.environmental_type = "wetland"
        assert enclosure.environmental_type == "wetland"

    # Test setting environmental type to invalid value.
    def test_set_environmental_type_invalid(self, enclosure, capsys):
        enclosure.environmental_type = 123
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid environmental type."
        assert enclosure.environmental_type == "freshwater aquatic"

    # Test changing environmental type when there are animals in the enclosure.
    def test_set_environmental_type_with_animal(self, enclosure, turtle, capsys):
        enclosure.add_animal(turtle)
        enclosure.environmental_type = "forest"
        message = capsys.readouterr()
        assert (message.out.strip() == ("Sue added to enclosure 10.\nThere are animals in this enclosure. Cannot change"
                                       " environment.")
                                        or message.out.strip() ==
                                        ("Sue added to enclosure 17.\nThere are animals in this enclosure. Cannot change"
                                       " environment."))
        assert enclosure.environmental_type == "freshwater aquatic"

    # Test get_cleanliness_level method (through property).
    def test_get_cleanliness_level(self, enclosure):
        assert enclosure.cleanliness_level == 10

    # Test get_staff method (through property).
    def test_get_staff(self, enclosure):
        assert enclosure.staff == {"feeding": [], "cleaning": [], "health": [], "research": [], "general": []}

    # Test get_animals method (through property).
    def test_get_animals(self, enclosure):
        assert enclosure.animals == []

    # Test get_species method (through property).
    def test_get_species(self, enclosure):
        assert enclosure.species is None

    # Test species after animal added.
    def test_get_species_animal(self, enclosure, turtle):
        enclosure.add_animal(turtle)
        assert enclosure.species == "Turtle"

    # Test adding an animal when environment type is None.
    def test_add_animal_no_environment(self, enclosure_no_environment, turtle, capsys):
        enclosure_no_environment.add_animal(turtle)
        message = capsys.readouterr()
        assert message.out.strip() == "Environment type not set. Cannot add animal."
        assert enclosure_no_environment.animals == []

    # Test adding animal to enclosure with incompatible species.
    def test_add_animal_incompatible_species(self, enclosure, turtle, shark, capsys):
        enclosure.add_animal(shark)
        enclosure.add_animal(turtle)
        message = capsys.readouterr()
        assert (message.out.strip() == "Bill added to enclosure 17.\nSue is not Shark. Cannot add to enclosure."
                                        or message.out.strip() ==
                                        "Bill added to enclosure 24.\nSue is not Shark. Cannot add to enclosure.")
        assert enclosure.animals == [shark]

    # Test adding animal when under treatment.
    def test_add_animal_under_treatment(self, enclosure, turtle, capsys):
        turtle.under_treatment = True
        enclosure.add_animal(turtle)
        message = capsys.readouterr()
        assert message.out.strip() == "Cannot add Sue to enclosure while under treatment."

    # Test adding animal to enclosure with incompatible environment.
    def test_add_animal_incompatible_environment(self, enclosure, turtle, capsys):
        enclosure.environmental_type = "forest"
        enclosure.add_animal(turtle)
        message = capsys.readouterr()
        assert message.out.strip() == "Enclosure type (forest) incompatible with Sue's requirements."

    # Test adding animal that is already in enclosure.
    def test_add_animal_twice(self, enclosure, turtle, capsys):
        enclosure.add_animal(turtle)
        enclosure.add_animal(turtle)
        message = capsys.readouterr()
        assert (message.out.strip() == "Sue added to enclosure 20.\nSue already in this enclosure."
                                        or message.out.strip() ==
                                        "Sue added to enclosure 27.\nSue already in this enclosure.")

    # Test adding animal that's already in another enclosure.
    def test_add_animal_two_enclosures(self, enclosure, enclosure2, turtle, capsys):
        enclosure.add_animal(turtle)
        enclosure2.add_animal(turtle)
        message = capsys.readouterr()
        assert (message.out.strip() == "Sue added to enclosure 21.\nSue is already in another enclosure."
                                        or message.out.strip() ==
                                        "Sue added to enclosure 28.\nSue is already in another enclosure.")

    # Test properly adding an animal.
    def test_add_animal(self, enclosure, turtle, capsys):
        enclosure.add_animal(turtle)
        message = capsys.readouterr()
        assert message.out.strip() == "Sue added to enclosure 23." or message.out.strip() == "Sue added to enclosure 30."
        assert enclosure.animals == [turtle]
        assert enclosure.cleanliness_level == 9

    # Test adding an invalid animal.
    def test_add_animal_invalid(self, enclosure, capsys):
        enclosure.add_animal("animal")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid animal."

    # Test removing an animal not in the enclosure.
    def test_remove_animal_not_in_enclosure(self, enclosure, turtle, capsys):
        enclosure.remove_animal(turtle)
        message = capsys.readouterr()
        assert message.out.strip() == "Animal is not in this enclosure."

    # Test removing invalid animal.
    def test_remove_animal_invalid(self, enclosure, capsys):
        enclosure.remove_animal(enclosure)
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid animal."

    # Test properly removing animal.
    def test_remove_animal(self, enclosure, turtle, capsys):
        enclosure.add_animal(turtle)
        enclosure.remove_animal(turtle)
        message = capsys.readouterr()
        assert (message.out.strip() == "Sue added to enclosure 27.\nSue removed from enclosure."
                                        or message.out.strip() ==
                                        "Sue added to enclosure 34.\nSue removed from enclosure.")
        assert enclosure.animals == []

    # Test adding a staff member.
    def test_add_staff(self, enclosure, zookeeper, capsys):
        enclosure.add_staff(zookeeper, "cleaning")
        message = capsys.readouterr()
        assert (message.out.strip() == "Steve assigned to cleaning duties in enclosure 28."
                                        or message.out.strip() ==
                                        "Steve assigned to cleaning duties in enclosure 35.")
        assert enclosure.staff == {"feeding": [], "cleaning": [zookeeper], "health": [], "research": [], "general": []}

    # Test adding staff to enclosure with invalid duty.
    def test_add_staff_invalid_duty(self, enclosure, zookeeper, capsys):
        enclosure.add_staff(zookeeper, "duty")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid duty. Must be 'feeding', 'cleaning', 'health', 'research', or 'general'."

    # Test adding a staff to the same duty again.
    def test_add_staff_twice(self, enclosure, zookeeper, capsys):
        enclosure.add_staff(zookeeper, "feeding")
        enclosure.add_staff(zookeeper, "feeding")
        message = capsys.readouterr()
        assert (message.out.strip() == "Steve assigned to feeding duties in enclosure 30.\nSteve is already assigned this duty."
                                        or message.out.strip() ==
                                        "Steve assigned to feeding duties in enclosure 37.\nSteve is already assigned this duty.")
        assert enclosure.staff == {"feeding": [zookeeper], "cleaning": [], "health": [], "research": [], "general": []}

    # Test adding staff to a duty they don't have.
    def test_add_staff_unheld_duty(self, enclosure, zookeeper, capsys):
        enclosure.add_staff(zookeeper, "health")
        message = capsys.readouterr()
        assert message.out.strip() == "Health is not one of Steve's duties."
        assert enclosure.staff == {"feeding": [], "cleaning": [], "health": [], "research": [], "general": []}

    # Test adding invalid staff.
    def test_add_staff_invalid(self, enclosure, capsys):
        enclosure.add_staff("steve")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid staff."

    # Test properly removing staff.
    def test_remove_staff(self, enclosure, zookeeper, capsys):
        enclosure.add_staff(zookeeper)
        enclosure.remove_staff(zookeeper, "general")
        message = capsys.readouterr()
        assert (message.out.strip() == ("Steve assigned to general duties in enclosure 33.\nSteve removed from general duties"
                                       " in enclosure 33.")
                                        or message.out.strip() ==
                                        ("Steve assigned to general duties in enclosure 40.\nSteve removed from general duties"
                                       " in enclosure 40."))
        assert enclosure.staff == {"feeding": [], "cleaning": [], "health": [], "research": [], "general": []}

    # Test removing staff with invalid duty.
    def test_remove_staff_invalid_duty(self, enclosure, zookeeper, capsys):
        enclosure.remove_staff(zookeeper, "duty")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid duty. Must be 'feeding', 'cleaning', 'health', 'research', or 'general'."

    # Test removing staff from enclosure they are not assigned to.
    def test_remove_staff_not_assigned(self, enclosure, zookeeper, capsys):
        enclosure.remove_staff(zookeeper, "cleaning")
        message = capsys.readouterr()
        assert message.out.strip() == "Steve has not been assigned this duty."

    # Test removing invalid staff.
    def test_remove_staff_invalid(self, enclosure, capsys):
        enclosure.remove_staff(enclosure)
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid staff."

    # Test reduce_cleanliness method.
    def test_reduce_cleanliness(self, enclosure):
        enclosure.reduce_cleanliness(7.2)
        assert enclosure.cleanliness_level == 2.8

    # Test reduce_cleanliness method > 10.
    def test_reduce_cleanliness_more_than_10(self, enclosure):
        enclosure.reduce_cleanliness(31)
        assert enclosure.cleanliness_level == 0

    # Test reduce_cleanliness method with negative number.
    def test_reduce_cleanliness_negative(self, enclosure, capsys):
        enclosure.reduce_cleanliness(-6)
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid amount."
        assert enclosure.cleanliness_level == 10

    # Test reduce_cleanliness method with non-number
    def test_reduce_cleanliness_invalid(self, enclosure, capsys):
        enclosure.reduce_cleanliness("5")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid amount."
        assert enclosure.cleanliness_level == 10

    # Test clean method.
    def test_clean(self, enclosure, zookeeper, capsys):
        enclosure.reduce_cleanliness(5)  # Reduce cleanliness.
        enclosure.add_staff(zookeeper, "cleaning")  # Add to cleaning duties.
        enclosure.clean(zookeeper)
        message = capsys.readouterr()
        assert (message.out.strip() == "Steve assigned to cleaning duties in enclosure 41.\nSteve is cleaning the enclosure..."
                                        or message.out.strip() ==
                                        "Steve assigned to cleaning duties in enclosure 48.\nSteve is cleaning the enclosure...")
        assert enclosure.cleanliness_level == 10

    # Test cleaning the enclosure with non-zookeeper staff.
    def test_clean_biologist(self, enclosure, biologist, capsys):
        enclosure.reduce_cleanliness(5)
        enclosure.clean(biologist)
        message = capsys.readouterr()
        assert message.out.strip() == "Susan is not a Zookeeper."
        assert enclosure.cleanliness_level == 5

    # Test cleaning the enclosure with zookeeper not assigned to cleaning.
    def test_clean_zookeeper_unassigned(self, enclosure, zookeeper, capsys):
        enclosure.reduce_cleanliness(5)  # Reduce cleanliness.
        enclosure.clean(zookeeper)
        message = capsys.readouterr()
        assert message.out.strip() == "Steve is not assigned to cleaning duties."
        assert enclosure.cleanliness_level == 5

    # Test clean method with invalid staff.
    def test_clean_invalid_staff(self, enclosure, capsys):
        enclosure.clean("steve")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid staff."

    # Test equal method.
    def test_equal(self, enclosure):
        assert enclosure == enclosure

    # Test equal method with other enclosure.
    def test_unequal(self, enclosure, enclosure2):
        assert enclosure != enclosure2

    # Test string method.
    def test_str(self, enclosure, capsys):
        print(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == ("---ENCLOSURE REPORT---\nID: 48\nType: freshwater aquatic\nSize: 50m\u00b2\n"
                                       "Cleanliness level: 10/10\n\nAnimals: None\n\nStaff:\n> Feeding: None\n"
                                       "> Cleaning: None\n> Health: None\n> Research: None\n> General: None"
                                       "\n--------------------")
                                        or message.out.strip() ==
                                        ("---ENCLOSURE REPORT---\nID: 55\nType: freshwater aquatic\nSize: 50m\u00b2\n"
                                       "Cleanliness level: 10/10\n\nAnimals: None\n\nStaff:\n> Feeding: None\n"
                                       "> Cleaning: None\n> Health: None\n> Research: None\n> General: None"
                                       "\n--------------------"))