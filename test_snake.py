'''
File: test_snake.py
Description: A module defining a class that uses pytest to test the outputs of the snake module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from snake import Snake


class TestSnake:
    @pytest.fixture
    def snake(self):
        return Snake("Nagini", 92)

    # Test that the cry method prints correctly.
    def test_cry(self, snake, capsys):
        snake.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*hissss*"

    # Test that the sleep method prints correctly.
    def test_sleep(self, snake, capsys):
        snake.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == "Nagini curls up to sleep...with eyes open..."

    # Test that the eat method prints correctly.
    def test_eat(self, snake, capsys):
        snake.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == "Nagini swallows food whole..."

    # Test that the move method prints correctly.
    def test_move(self, snake, capsys):
        snake.move()
        move = capsys.readouterr()
        assert move.out.strip() == "Nagini slithers..."

    # Test that the environment types list is correct.
    def test_environment_types(self, snake):
        assert snake.environment_types == ["tropical", "grassland", "desert", "forest", "wetland"]
