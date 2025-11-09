'''
File: test_angelfish.py
Description: A module defining a class that uses pytest to test the outputs of the angelfish module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from angelfish import Angelfish


class TestAngelfish:
    @pytest.fixture
    def angelfish(self):
        return Angelfish("Willow", 2, saltwater=True)

    # Test that the cry method prints correctly.
    def test_cry(self, angelfish, capsys):
        angelfish.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*blop blop*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, angelfish, capsys):
        angelfish.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Willow hovers asleep in the water..."

    # Test that the eat method prints correctly.
    def test_eat(self, angelfish, capsys):
        angelfish.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Willow slurps up food..."

    # Test that the swim method prints correctly.
    def test_swim(self, angelfish, capsys):
        angelfish.swim()
        swim = capsys.readouterr()
        assert swim.out.strip() == "Willow floats around..."

    # Test that the environment types list is correct.
    def test_environment_types(self, angelfish):
        assert angelfish.environment_types == ["saltwater aquatic"]