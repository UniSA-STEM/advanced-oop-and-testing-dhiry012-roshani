'''
File: test_fish.py
Description: A module defining a class that uses pytest to test the outputs of the abstract fish module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from fish import Fish


# Note: I didn't test any of the inherited abstract methods, as these are tested in other modules.

# Create a mock class.
class MockFish(Fish):
    def cry(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

    def swim(self):
        return "swim"


class TestFish:
    @pytest.fixture
    def fish(self):
        return MockFish("Bob", 3)

    # Test that Fish class cannot be instantiated.
    def test_raises(self):
        with pytest.raises(TypeError):
            Fish("Name", 7)

    # Test swim method.
    def test_swim(self, fish):
        assert fish.swim() == "swim"
