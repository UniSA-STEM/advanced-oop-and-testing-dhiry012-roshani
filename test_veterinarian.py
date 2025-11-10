'''
File: test_veterinarian.py
Description: A module defining a class that uses pytest to test the outputs of the veterinarian module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from veterinarian import Veterinarian
from enclosure import Enclosure  # To use in testing health check method.
from turtle import Turtle  # To use in testing health check method.


# IMPORTANT NOTE
# As with the test_animal module, I include two output options for the outputs which include id numbers: one for running
# "pytest test_staff.py" in the Terminal window and one for "pytest".


class TestVeterinarian:
    @pytest.fixture
    def veterinarian(self):
        return Veterinarian("Lucy")

    @pytest.fixture
    def enclosure(self):
        return Enclosure(500, "freshwater aquatic")

    @pytest.fixture
    def turtle(self):
        return Turtle("Sue", 12, freshwater=True)

    # Test that all duties are in the list.
    def test_get_duties(self, veterinarian):
        assert veterinarian.duties == ["general", "health"]

    # Test health checking an enclosure to which vet is not assigned.
    def test_health_check_unassigned_enclosure(self, veterinarian, enclosure, capsys):
        veterinarian.health_check(enclosure)
        message = capsys.readouterr()
        assert message.out.strip() == "Lucy is not assigned to that enclosure."

    # Test health checking an enclosure to which vet has not been specifically assigned health duties.
    def test_research_not_health_duty(self, veterinarian, enclosure, capsys):
        enclosure.add_staff(veterinarian)  # Add vet to enclosure (general duties).
        veterinarian.health_check(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == ("Lucy assigned to general duties in enclosure 2.\n"
                                       "Lucy is not assigned health duties for that enclosure.")
                                        or message.out.strip() ==
                                        ("Lucy assigned to general duties in enclosure 61.\n"
                                       "Lucy is not assigned health duties for that enclosure."))

    # Test health checking an empty enclosure.
    def test_health_check_empty_enclosure(self, veterinarian, enclosure, capsys):
        enclosure.add_staff(veterinarian, "health")  # Assign vet to enclosure (no animals).
        veterinarian.health_check(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == ("Lucy assigned to health duties in enclosure 3.\n-----ENCLOSURE 3 HEALTH CHECK"
                                        "-----\nEnclosure empty")
                                        or message.out.strip() ==
                                        ("Lucy assigned to health duties in enclosure 62.\n-----ENCLOSURE 62 HEALTH CHECK"
                                         "-----\nEnclosure empty"))

    # Test health checking an enclosure with an animal.
    def test_health_check_enclosure(self, veterinarian, enclosure, turtle, capsys):
        enclosure.add_animal(turtle)  # Add animal to enclosure.
        enclosure.add_staff(veterinarian, "health")  # Add vet to health duties.
        veterinarian.health_check(enclosure)  # Health check.
        message = capsys.readouterr()
        assert (message.out.strip() == ("Sue added to enclosure 4.\nLucy assigned to health duties in enclosure 4.\n"
                                       "-----ENCLOSURE 4 HEALTH CHECK-----\n\n---Report for: Sue (ID-1)---\n\nINJURIES\n"
                                        "None\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n-----------------")
                                        or message.out.strip() ==
                                        ("Sue added to enclosure 63.\nLucy assigned to health duties in enclosure 63.\n"
                                       "-----ENCLOSURE 63 HEALTH CHECK-----\n\n---Report for: Sue (ID-143)---\n\nINJURIES\n"
                                        "None\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n-----------------"))

    # Test health checking an invalid enclosure.
    def test_health_check_invalid_enclosure(self, veterinarian, capsys):
        veterinarian.health_check("an object")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid enclosure."