'''
File: test_biologist.py
Description: A module defining a class that uses pytest to test the outputs of the biologist module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from biologist import Biologist
from enclosure import Enclosure  # To use in testing research method.
from turtle import Turtle  # To use in testing research method.


# IMPORTANT NOTE
# As with the test_animal module, I include two output options for the outputs which include id numbers: one for running
# "pytest test_staff.py" in the Terminal window and one for "pytest".


class TestBiologist:
    @pytest.fixture
    def biologist(self):
        return Biologist("Billy")

    @pytest.fixture
    def enclosure(self):
        return Enclosure(500, "freshwater aquatic")

    @pytest.fixture
    def turtle(self):
        return Turtle("Sue", 12, freshwater=True)

    # Test that all duties are in the list.
    def test_get_duties(self, biologist):
        assert biologist.duties == ["general", "research"]

    # Test researching an enclosure to which biologist is not assigned.
    def test_research_unassigned_enclosure(self, biologist, enclosure, capsys):
        biologist.research(enclosure)
        message = capsys.readouterr()
        assert message.out.strip() == "Billy is not assigned to that enclosure."

    # Test researching an enclosure to which biologist has not been specifically assigned research duties.
    def test_research_not_research_duty(self, biologist, enclosure, capsys):
        enclosure.add_staff(biologist)  # Add biologist to enclosure (general duties).
        biologist.research(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == ("Billy assigned to general duties in enclosure 2.\n"
                                        "Billy is not assigned research duties for that enclosure.")
                or message.out.strip() ==
                ("Billy assigned to general duties in enclosure 5.\n"
                 "Billy is not assigned research duties for that enclosure."))

    # Test researching an empty enclosure.
    def test_research_empty_enclosure(self, biologist, enclosure, capsys):
        enclosure.add_staff(biologist, "research")  # Assign biologist to enclosure (no animals).
        biologist.research(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == (
            "Billy assigned to research duties in enclosure 3.\n-----ENCLOSURE 3 RESEARCH-----\n"
            "Enclosure is empty.")
                or message.out.strip() ==
                ("Billy assigned to research duties in enclosure 6.\n-----ENCLOSURE 6 RESEARCH-----\n"
                 "Enclosure is empty."))

    # Test researching an enclosure with an animal.
    def test_research_enclosure(self, biologist, enclosure, turtle, capsys):
        enclosure.add_animal(turtle)  # Add animal to enclosure.
        enclosure.add_staff(biologist, "research")  # Add biologist to research duties.
        biologist.research(enclosure)  # Research.
        message = capsys.readouterr()
        assert (message.out.strip() == ("Sue added to enclosure 4.\nBilly assigned to research duties in enclosure 4.\n"
                                        "-----ENCLOSURE 4 RESEARCH-----\n\n---ANIMAL DETAILS---\nID: 1\nName: Sue\n"
                                        "Age: 12 years\nSpecies: Turtle\nEnvironment types: freshwater aquatic\nSue has "
                                        "no specific dietary needs.\n---------")
                or message.out.strip() ==
                ("Sue added to enclosure 7.\nBilly assigned to research duties in enclosure 7.\n"
                 "-----ENCLOSURE 7 RESEARCH-----\n\n---ANIMAL DETAILS---\nID: 59\nName: Sue\n"
                 "Age: 12 years\nSpecies: Turtle\nEnvironment types: freshwater aquatic\nSue has "
                 "no specific dietary needs.\n---------"))

    # Test researching an invalid enclosure.
    def test_research_invalid_enclosure(self, biologist, capsys):
        biologist.research("an object")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid enclosure."
