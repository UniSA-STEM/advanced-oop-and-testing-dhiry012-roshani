'''
File: test_penguin.py
Description: A module defining a class that uses pytest to test the outputs of the penguin module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from penguin import Penguin


class TestPenguin:
    @pytest.fixture
    def penguin(self):
        return Penguin("Mumble", 1)

    # Test that the cry method prints correctly.
    def test_cry(self, penguin, capsys):
        penguin.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*braying honking squawking*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, penguin, capsys):
        penguin.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Mumble tucks in beak to doze..."

    # Test that the eat method prints correctly.
    def test_eat(self, penguin, capsys):
        penguin.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Mumble swallows fish whole..."

    # Test that the move method prints correctly.
    def test_move(self, penguin, capsys):
        penguin.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Mumble waddles and shuffles along..."

    # Test that the fly method prints correctly.
    def test_fly(self, penguin, capsys):
        penguin.fly()
        fly = capsys.readouterr()
        assert fly.out.strip() == "Mumble flaps wings ineffectually..."

    # Test that the swim method prints correctly.
    def test_swim(self, penguin, capsys):
        penguin.swim()
        swim = capsys.readouterr()
        assert swim.out.strip() == "Mumble darts through the water..."

    # Test that the environment types list is correct.
    def test_environment_types(self, penguin):
        assert penguin.environment_types == ["saltwater aquatic", "arctic"]