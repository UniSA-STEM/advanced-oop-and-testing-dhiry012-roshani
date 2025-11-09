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

# Create a mock class with which to test the non-abstract Amphibian class methods.
# Note: I didn't test any of the methods defined in the Animal class, as these get tested thoroughly in the many
# species and Animal testing modules.
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

    def test_raises(self, amphibian):
        with pytest.raises(TypeError):
            Amphibian("Name", 7)

    def test_move(self, amphibian):
        assert amphibian.move() == "move"

    def test_swim(self, amphibian):
        assert amphibian.swim() == "swim"




