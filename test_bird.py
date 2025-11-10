'''
File: test_bird.py
Description: A module defining a class that uses pytest to test the outputs of the abstract bird module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from bird import Bird


# Note: I didn't test any of the inherited abstract methods, as these are tested in other modules.

# Create a mock class.
class MockBird(Bird):
    def cry(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

    def move(self):
        return "move"

    def fly(self):
        return "fly"


class TestBird:
    @pytest.fixture
    def bird(self):
        return MockBird("Tweety", 3)

    # Test that Bird class cannot be instantiated.
    def test_raises(self):
        with pytest.raises(TypeError):
            Bird("Name", 7)

    # Test move method.
    def test_move(self, bird):
        assert bird.move() == "move"

    # Test fly method.
    def test_fly(self, bird):
        assert bird.fly() == "fly"
