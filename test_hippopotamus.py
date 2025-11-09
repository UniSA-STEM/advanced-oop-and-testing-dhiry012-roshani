'''
File: test_hippopotamus.py
Description: A module defining a class that uses pytest to test the outputs of the hippopotamus module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from hippopotamus import Hippopotamus


class TestHippopotamus:
    @pytest.fixture
    def hippopotamus(self):
        return Hippopotamus("Hippie", 7)

    # Test that the cry method prints correctly.
    def test_cry(self, hippopotamus, capsys):
        hippopotamus.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*grunt grunt honk*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, hippopotamus, capsys):
        hippopotamus.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Hippie sinks underwater to sleep..."

    # Test that the eat method prints correctly.
    def test_eat(self, hippopotamus, capsys):
        hippopotamus.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Hippie chomps on some grass..."

    # Test that the move method prints correctly.
    def test_move(self, hippopotamus, capsys):
        hippopotamus.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Hippie trots along...even underwater..."

    # Test that the environment types list is correct.
    def test_environment_types(self, hippopotamus):
        assert hippopotamus.environment_types == ["tropical", "grassland", "freshwater aquatic", "wetland"]