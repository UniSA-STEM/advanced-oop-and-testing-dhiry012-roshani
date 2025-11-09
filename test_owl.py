'''
File: test_owl.py
Description: A module defining a class that uses pytest to test the outputs of the owl module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from owl import Owl


class TestOwl:
    @pytest.fixture
    def owl(self):
        return Owl("Wol", 1)

    # Test that the cry method prints correctly.
    def test_cry(self, owl, capsys):
        owl.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*hoot hoot*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, owl, capsys):
        owl.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Wol sleeps in the daytime..."

    # Test that the eat method prints correctly.
    def test_eat(self, owl, capsys):
        owl.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Wol tears into food..."

    # Test that the move method prints correctly.
    def test_move(self, owl, capsys):
        owl.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Wol hops and struts along..."

    # Test that the fly method prints correctly.
    def test_fly(self, owl, capsys):
        owl.fly()
        fly = capsys.readouterr()
        assert fly.out.strip() == "Wol glides silently..."

    # Test that the environment types list is correct.
    def test_environment_types(self, owl):
        assert owl.environment_types == ["forest"]