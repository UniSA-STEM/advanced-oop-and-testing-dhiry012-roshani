'''
File: test_elephant.py
Description: A module defining a class that uses pytest to test the outputs of the elephant module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from elephant import Elephant


class TestElephant:
    @pytest.fixture
    def elephant(self):
        return Elephant("Ellie", 42)

    def test_cry(self, elephant, capsys):
        elephant.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*trumpets!*"

    def test_sleep(self, elephant, capsys):
        elephant.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Ellie lies down to sleep..."

    def test_eat(self, elephant, capsys):
        elephant.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Ellie brings food to their mouth with their trunk..."

    def test_move(self, elephant, capsys):
        elephant.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Ellie stomps around..."

    def test_environment_types(self, elephant):
        assert elephant.environment_types == ["grassland", "tropical", "forest"]