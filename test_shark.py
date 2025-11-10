'''
File: test_shark.py
Description: A module defining a class that uses pytest to test the outputs of the shark module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from shark import Shark


class TestShark:
    @pytest.fixture
    def shark(self):
        return Shark("Bruce", 32, freshwater=True)

    # Test that the cry method prints correctly.
    def test_cry(self, shark, capsys):
        shark.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*da da...da da...dadadadadada*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, shark, capsys):
        shark.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Bruce keeps moving...or dies..."

    # Test that the eat method prints correctly.
    def test_eat(self, shark, capsys):
        shark.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Bruce attacks food mercilessly..."

    # Test that the swim method prints correctly.
    def test_swim(self, shark, capsys):
        shark.swim()
        swim = capsys.readouterr()
        assert swim.out.strip() == "Bruce cruises through the water..."

    # Test that the environment types list is correct.
    def test_environment_types(self, shark):
        assert shark.environment_types == ["freshwater aquatic"]
