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

    def test_cry(self, owl, capsys):
        owl.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*hoot hoot*"

    def test_sleep(self, owl, capsys):
        owl.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Wol sleeps in the daytime..."

    def test_eat(self, owl, capsys):
        owl.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Wol tears into food..."

    def test_move(self, owl, capsys):
        owl.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Wol hops and struts along..."

    def test_fly(self, owl, capsys):
        owl.fly()
        fly = capsys.readouterr()
        assert fly.out.strip() == "Wol glides silently..."

    def test_environment_types(self, owl):
        assert owl.environment_types == ["forest"]