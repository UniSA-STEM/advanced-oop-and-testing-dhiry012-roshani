'''
File: test_amphibian.py
Description: A module defining a class that uses pytest to test the outputs of the abstract amphibian module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from amphibian import Amphibian

# Note: I didn't test any of the inherited abstract methods, as these are tested in other modules.

# Create a mock class.
class MockAmphibian(Amphibian):
    def cry(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

    def move(self):
        return "move"

    def swim(self):
        return "swim"


class TestAmphibian:
    @pytest.fixture
    def amphibian(self):
        return MockAmphibian("Toad", 3)

    # Test that Amphibian class cannot be instantiated.
    def test_raises(self, amphibian):
        with pytest.raises(TypeError):
            Amphibian("Name", 7)

    # Test move method.
    def test_move(self, amphibian):
        assert amphibian.move() == "move"

    # Test swim method.
    def test_swim(self, amphibian):
        assert amphibian.swim() == "swim"