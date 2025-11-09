'''
File: test_frog.py
Description: A module defining a class that uses pytest to test the outputs of the frog module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from frog import Frog


class TestFrog:
    @pytest.fixture
    def frog(self):
        return Frog("Naveen", 25)

    # Test that the cry method prints correctly.
    def test_cry(self, frog, capsys):
        frog.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*ribbit ribbit croak*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, frog, capsys):
        frog.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Naveen rests on a lillypad..."

    # Test that the eat method prints correctly.
    def test_eat(self, frog, capsys):
        frog.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Naveen catches bug on tongue..."

    # Test that the move method prints correctly.
    def test_move(self, frog, capsys):
        frog.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Naveen jumps around..."

    # Test that the swim method prints correctly.
    def test_swim(self, frog, capsys):
        frog.swim()
        swim = capsys.readouterr()
        assert swim.out.strip() == "Naveen pushes through the water..."

    # Test that the environment types list is correct.
    def test_environment_types(self, frog):
        assert frog.environment_types == ["wetland", "tropical", "forest", "freshwater aquatic"]