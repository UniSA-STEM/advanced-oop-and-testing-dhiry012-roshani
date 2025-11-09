'''
File: test_turtle.py
Description: A module defining a class that uses pytest to test the outputs of the turtle module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from turtle import Turtle


class TestTurtle:
    @pytest.fixture
    def turtle(self):
        return Turtle("Crush", 40)

    def test_cry(self, turtle, capsys):
        turtle.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*chirp growl wheeze*"

    def test_sleep(self, turtle, capsys):
        turtle.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Crush retreats into shell to sleep..."

    def test_eat(self, turtle, capsys):
        turtle.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Crush bites into food..."

    def test_move(self, turtle, capsys):
        turtle.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Crush crawls and shuffles..."

    def test_swim(self, turtle, capsys):
        turtle.swim()
        swim = capsys.readouterr()
        assert swim.out.strip() == "Crush paddles through the water..."

    def test_environment_types(self, turtle):
        assert turtle.environment_types == []

    def test_get_freshwater(self, turtle):
        assert turtle.freshwater == False

    def test_get_saltwater(self, turtle):
        assert turtle.saltwater == False

    def test_set_freshwater(self, turtle):
        turtle.freshwater = True
        assert turtle.freshwater == True

    def test_set_freshwater_invalid(self, turtle, capsys):
        turtle.freshwater = "something"
        message = capsys.readouterr()
        assert turtle.freshwater == False
        assert message.out.strip() == "Invalid value. Must be True or False"

    def test_environment_types_set_freshwater_true(self, turtle):
        turtle.freshwater = True
        assert turtle.environment_types == ["freshwater aquatic"]

    def test_environment_types_set_freshwater_false(self, turtle):
        turtle.freshwater = True
        assert turtle.environment_types == ["freshwater aquatic"]
        turtle.freshwater = False
        assert turtle.environment_types == []

    def test_set_saltwater(self, turtle):
        turtle.saltwater = True
        assert turtle.saltwater == True

    def test_set_saltwater_invalid(self, turtle, capsys):
        turtle.saltwater = "something"
        message = capsys.readouterr()
        assert turtle.saltwater == False
        assert message.out.strip() == "Invalid value. Must be True or False"

    def test_environment_types_set_saltwater_true(self, turtle):
        turtle.saltwater = True
        assert turtle.environment_types == ["saltwater aquatic"]

    def test_environment_types_set_saltwater_false(self, turtle):
        turtle.saltwater = True
        assert turtle.environment_types == ["saltwater aquatic"]
        turtle.saltwater = False
        assert turtle.environment_types == []