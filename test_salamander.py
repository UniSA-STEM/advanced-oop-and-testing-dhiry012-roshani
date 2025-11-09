'''
File: test_salamander.py
Description: A module defining a class that uses pytest to test the outputs of the salamander module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from salamander import Salamander


class TestSalamander:
    @pytest.fixture
    def salamander(self):
        return Salamander("Newt", 16)

    # Test that the cry method prints correctly.
    def test_cry(self, salamander, capsys):
        salamander.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*quiet clicking and squeaks*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, salamander, capsys):
        salamander.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Newt sleeps during the day..."

    # Test that the eat method prints correctly.
    def test_eat(self, salamander, capsys):
        salamander.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Newt munches on grubs..."

    # Test that the move method prints correctly.
    def test_move(self, salamander, capsys):
        salamander.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Newt crawls around..."

    # Test that the swim method prints correctly.
    def test_swim(self, salamander, capsys):
        salamander.swim()
        swim = capsys.readouterr()
        assert swim.out.strip() == "Newt wiggles around in the water..."

    # Test that the environment types list is correct.
    def test_environment_types(self, salamander):
        assert salamander.environment_types == ["tropical", "forest", "freshwater aquatic", "wetland"]