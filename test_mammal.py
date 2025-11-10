'''
File: test_mammal.py
Description: A module defining a class that uses pytest to test the outputs of the abstract mammal module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from mammal import Mammal


# Note: I didn't test any of the inherited abstract methods, as these are tested in other modules.

# Create a mock class.
class MockMammal(Mammal):
    def cry(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

    def move(self):
        return "move"


class TestMammal:
    @pytest.fixture
    def mammal(self):
        return MockMammal("Roo", 3)

    # Test that Mammal class cannot be instantiated.
    def test_raises(self):
        with pytest.raises(TypeError):
            Mammal("Name", 7)

    # Test move method.
    def test_move(self, mammal):
        assert mammal.move() == "move"
