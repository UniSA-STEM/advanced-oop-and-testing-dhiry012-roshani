'''
File: test_animal.py
Description: A module defining a class that uses pytest to test the outputs of the abstract animal module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from animal import Animal

# Create a mock class with which to test the Animal class methods.
class MockClass(Animal):
    def cry(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass


class TestAnimal:
    @pytest.fixture
    def animal(self):
        return MockClass("Leo", 3)

    def test_name(self, animal):
        assert animal.name == "Leo"

    def test_name_invalid_blank(self, animal, capsys):
        animal.name = ""
        message = capsys.readouterr()
        assert animal.name == "Leo"
        assert message.out.strip() == "Invalid name."

    def test_name_change(self, animal):
        animal.name = "Fred"
        assert animal.name == "Fred"

    def test_age(self, animal):
        assert animal.age == 3

    def test_age_change(self, animal):
        animal.age = 12
        assert animal.age == 12

    def test_age_negative(self, animal, capsys):
        animal.age = -2
        message = capsys.readouterr()
        assert animal.age == 3
        assert message.out.strip() == "Age must be greater than 0."

    def test_age_string(self, animal, capsys):
        animal.age = "hello"
        message = capsys.readouterr()
        assert animal.age == 3
        assert message.out.strip() == "Invalid age. Must be a whole number."

    def test_age_float(self, animal, capsys):
        animal.age = 5.5
        message = capsys.readouterr()
        assert animal.age == 3
        assert message.out.strip() == "Invalid age. Must be a whole number."

    def test_species(self, animal):
        assert animal.species == "MockClass"

    def test_under_treatment(self, animal):
        assert animal.under_treatment == False

    def test_under_treatment_change(self, animal):
        animal.under_treatment = True
        assert animal.under_treatment == True

    def test_under_treatment_invalid(self, animal):
        animal.under_treatment = "True"
        assert animal.under_treatment == False

    def test_get_dietary_needs(self, animal):
        assert animal.dietary_needs == "Leo has no specific dietary needs."

    def test_add_dietary_need(self, animal, capsys):
        animal.add_dietary_need("Drinks only single malt whisky")
        print(animal.dietary_needs)
        message = capsys.readouterr()
        assert message.out.strip() == "Dietary Needs for Leo:\n1. Drinks only single malt whisky"

    def test_dietary_need_invalid_empty(self, animal, capsys):
        animal.add_dietary_need("")
        print(animal.dietary_needs)
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid entry. Not added to list.\nLeo has no specific dietary needs."

    def test_dietary_need_invalid_nonstring(self, animal, capsys):
        animal.add_dietary_need(123)
        print(animal.dietary_needs)
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid entry. Not added to list.\nLeo has no specific dietary needs."

    def test_remove_dietary_need(self, animal, capsys):
        animal.add_dietary_need("Something")
        animal.remove_dietary_need(0)
        print(animal.dietary_needs)
        message = capsys.readouterr()
        assert message.out.strip() == "Leo has no specific dietary needs."

    def test_remove_dietary_need_blank(self, animal, capsys):
        animal.remove_dietary_need(5)
        print(animal.dietary_needs)
        message = capsys.readouterr()
        assert message.out.strip() == "Nothing to remove.\nLeo has no specific dietary needs."