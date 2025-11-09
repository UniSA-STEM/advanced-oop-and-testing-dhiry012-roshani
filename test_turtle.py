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

    # Test that the cry method prints correctly.
    def test_cry(self, turtle, capsys):
        turtle.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*chirp growl wheeze*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, turtle, capsys):
        turtle.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Crush retreats into shell to sleep..."

    # Test that the eat method prints correctly.
    def test_eat(self, turtle, capsys):
        turtle.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Crush bites into food..."

    # Test that the move method prints correctly.
    def test_move(self, turtle, capsys):
        turtle.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Crush crawls and shuffles..."

    # Test that the swim method prints correctly.
    def test_swim(self, turtle, capsys):
        turtle.swim()
        swim = capsys.readouterr()
        assert swim.out.strip() == "Crush paddles through the water..."

    # Test that there are no initial environment types (saltwater and freshwater should be False).
    def test_environment_types(self, turtle):
        assert turtle.environment_types == []

    # Test that freshwater is False.
    def test_get_freshwater(self, turtle):
        assert turtle.freshwater == False

    # Test that saltwater is False.
    def test_get_saltwater(self, turtle):
        assert turtle.saltwater == False

    # Test setting freshwater to True (and checking it worked).
    def test_set_freshwater(self, turtle):
        turtle.freshwater = True
        assert turtle.freshwater == True

    # Test setting freshwater to an invalid value, that it doesn't change the attribute, and that it prints the
    # correct statement.
    def test_set_freshwater_invalid(self, turtle, capsys):
        turtle.freshwater = "something"
        message = capsys.readouterr()
        assert turtle.freshwater == False
        assert message.out.strip() == "Invalid value. Must be True or False"

    # Test that setting freshwater to True also adds freshwater aquatic to environment types.
    def test_environment_types_set_freshwater_true(self, turtle):
        turtle.freshwater = True
        assert turtle.environment_types == ["freshwater aquatic"]

    # Test that setting freshwater to True then False adds then removes freshwater aquatic from environment types.
    def test_environment_types_set_freshwater_false(self, turtle):
        turtle.freshwater = True
        assert turtle.environment_types == ["freshwater aquatic"]
        turtle.freshwater = False
        assert turtle.environment_types == []

    # Test setting saltwater to True (and checking it worked).
    def test_set_saltwater(self, turtle):
        turtle.saltwater = True
        assert turtle.saltwater == True

    # Test setting saltwater to an invalid value, that it doesn't change the attribute, and that it prints the
    # correct statement.
    def test_set_saltwater_invalid(self, turtle, capsys):
        turtle.saltwater = "something"
        message = capsys.readouterr()
        assert turtle.saltwater == False
        assert message.out.strip() == "Invalid value. Must be True or False"

    # Test that setting saltwater to True also adds saltwater aquatic to environment types.
    def test_environment_types_set_saltwater_true(self, turtle):
        turtle.saltwater = True
        assert turtle.environment_types == ["saltwater aquatic"]

    # Test that setting saltwater to True then False adds then removes saltwater aquatic from environment types.
    def test_environment_types_set_saltwater_false(self, turtle):
        turtle.saltwater = True
        assert turtle.environment_types == ["saltwater aquatic"]
        turtle.saltwater = False
        assert turtle.environment_types == []