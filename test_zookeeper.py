'''
File: test_zookeeper.py
Description: A module defining a class that uses pytest to test the outputs of the zookeeper module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from zookeeper import Zookeeper
from enclosure import Enclosure  # To use in testing research method.
from turtle import Turtle  # To use in testing research method.

class TestZookeeper:
    @pytest.fixture
    def zookeeper(self):
        return Zookeeper("Peter")

    @pytest.fixture
    def enclosure(self):
        return Enclosure(500, "freshwater aquatic")

    @pytest.fixture
    def turtle(self):
        return Turtle("Sue", 12, freshwater=True)

    # Test that all duties are in the list.
    def test_get_duties(self, zookeeper):
        assert zookeeper.duties == ["general", "feeding", "cleaning"]

    # Test feeding an enclosure to which zookeeper is not assigned.
    def test_feed_animals_unassigned_enclosure(self, zookeeper, enclosure, capsys):
        zookeeper.feed_animals(enclosure)
        message = capsys.readouterr()
        assert message.out.strip() == "Peter is not assigned to that enclosure."

    # Test feeding an enclosure to which zookeeper has not been specifically assigned feeding duties.
    def test_feed_animals_not_feeding_duty(self, zookeeper, enclosure, capsys):
        enclosure.add_staff(zookeeper)  # Add zookeeper to enclosure (general duties).
        zookeeper.feed_animals(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == ("Peter assigned to general duties in enclosure 2.\n"
                                       "Peter is not assigned feeding duties for that enclosure.")
                                        or message.out.strip() ==
                                        ("Peter assigned to general duties in enclosure 64.\n"
                                       "Peter is not assigned feeding duties for that enclosure."))

    # Test feeding an empty enclosure.
    def test_feed_animals_empty_enclosure(self, zookeeper, enclosure, capsys):
        enclosure.add_staff(zookeeper, "feeding")  # Assign zookeeper to enclosure (no animals).
        zookeeper.feed_animals(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == "Peter assigned to feeding duties in enclosure 3.\nEnclosure is empty."
                                        or message.out.strip() ==
                                        "Peter assigned to feeding duties in enclosure 65.\nEnclosure is empty.")

    # Test feeding an enclosure with an animal.
    def test_feed_animals_enclosure(self, zookeeper, enclosure, turtle, capsys):
        enclosure.add_animal(turtle)  # Add animal to enclosure.
        enclosure.add_staff(zookeeper, "feeding")  # Add zookeeper to feeding duties.
        zookeeper.feed_animals(enclosure)  # Feed.
        message = capsys.readouterr()
        assert (message.out.strip() == ("Sue added to enclosure 4.\nPeter assigned to feeding duties in enclosure 4.\n"
                                       "Sue bites into food...")
                                        or message.out.strip() ==
                                        ("Sue added to enclosure 66.\nPeter assigned to feeding duties in enclosure 66.\n"
                                       "Sue bites into food..."))

    # Test feeding an invalid enclosure.
    def test_feed_animals_invalid_enclosure(self, zookeeper, capsys):
        zookeeper.feed_animals("an object")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid enclosure."

    # Test cleaning an enclosure to which zookeeper is not assigned.
    def test_clean_enclosure_unassigned_enclosure(self, zookeeper, enclosure, capsys):
        zookeeper.clean_enclosure(enclosure)
        message = capsys.readouterr()
        assert message.out.strip() == "Peter is not assigned to that enclosure."

    # Test cleaning an enclosure to which zookeeper has not been specifically assigned cleaning duties.
    def test_clean_enclosure_not_cleaning_duty(self, zookeeper, enclosure, capsys):
        enclosure.add_staff(zookeeper)  # Add zookeeper to enclosure (general duties).
        zookeeper.clean_enclosure(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == ("Peter assigned to general duties in enclosure 6.\n"
                                       "Peter is not assigned cleaning duties for that enclosure.")
                                        or message.out.strip() ==
                                        ("Peter assigned to general duties in enclosure 68.\n"
                                       "Peter is not assigned cleaning duties for that enclosure."))

    # Test cleaning an empty enclosure (should work normally).
    def test_clean_enclosure_empty_enclosure(self, zookeeper, enclosure, capsys):
        enclosure.add_staff(zookeeper, "cleaning")  # Assign zookeeper to enclosure (no animals).
        zookeeper.clean_enclosure(enclosure)
        message = capsys.readouterr()
        assert (message.out.strip() == "Peter assigned to cleaning duties in enclosure 7.\nPeter is cleaning the enclosure..."
                                        or message.out.strip() ==
                                        "Peter assigned to cleaning duties in enclosure 69.\nPeter is cleaning the enclosure...")

    # Test cleaning an enclosure with an animal (same as empty enclosure).
    def test_clean_enclosure(self, zookeeper, enclosure, turtle, capsys):
        enclosure.add_animal(turtle)  # Add animal to enclosure.
        enclosure.add_staff(zookeeper, "cleaning")  # Add zookeeper to cleaning duties.
        zookeeper.clean_enclosure(enclosure)  # Clean.
        message = capsys.readouterr()
        assert (message.out.strip() == ("Sue added to enclosure 8.\nPeter assigned to cleaning duties in enclosure 8.\n"
                                       "Peter is cleaning the enclosure...")
                                        or message.out.strip() ==
                                        ("Sue added to enclosure 70.\nPeter assigned to cleaning duties in enclosure 70.\n"
                                       "Peter is cleaning the enclosure..."))

    # Test cleaning an invalid enclosure.
    def test_clean_enclosure_invalid_enclosure(self, zookeeper, capsys):
        zookeeper.clean_enclosure("an object")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid enclosure."