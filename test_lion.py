'''
File: test_lion.py
Description: A module defining a class that uses pytest to test the outputs of the lion module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from lion import Lion


class TestLion:
    @pytest.fixture
    def lion(self):
        return Lion("Leo", 3)

    def test_cry(self, lion, capsys):
        lion.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*Roaarrrr!!*"
        # Code inspired by:
        # Pytest. (2015). How to capture stdout/stderr output. https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html

    def test_sleep(self, lion, capsys):
        lion.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Leo lies down to sleep..."

    def test_eat(self, lion, capsys):
        lion.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Leo munches on meat"

    def test_move(self, lion, capsys):
        lion.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Leo prowls..."