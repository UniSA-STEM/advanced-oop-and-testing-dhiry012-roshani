'''
File: test_reptile.py
Description: A module defining a class that uses pytest to test the outputs of the abstract reptile module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from reptile import Reptile

# Note: I didn't test any of the inherited abstract methods, as these are tested in other modules.

# Create a mock class.
class MockReptile(Reptile):
    def cry(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

    def move(self):
        return "move"


class TestReptile:
    @pytest.fixture
    def reptile(self):
        return MockReptile("Voldie", 3)

    # Test that Reptile class cannot be instantiated.
    def test_raises(self, reptile):
        with pytest.raises(TypeError):
            Reptile("Name", 7)

    # Test move method.
    def test_move(self, reptile):
        assert reptile.move() == "move"