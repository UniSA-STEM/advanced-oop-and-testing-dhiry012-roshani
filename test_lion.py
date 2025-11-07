'''
File: test_lion.py
Description: A module defining a class that uses pytest to test the outputs of the lion module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from lion import Lion


class TestLion:
    @pytest.fixture
    def lion(self):
        return Lion("Leo", 3)

    @pytest.fixture
    def lion2(self):
        return Lion("Annie", 500)

    def test_cry(self, lion, capsys):
        lion.cry()
        cry = capsys.readouterr()
        assert cry.out.strip() == "*Roaarrrr!!*"
        # Code inspired by:
        # Pytest. (2015). How to capture stdout/stderr output. https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html

    def test_sleep(self, lion, capsys):
        lion.sleep()
        sleep = capsys.readouterr()
        assert sleep.out.strip() == f"{lion.name} lies down to sleep..."

    def test_eat(self, lion, capsys):
        lion.eat()
        eat = capsys.readouterr()
        assert eat.out.strip() == f"{lion.name} munches on meat"

    def test_move(self, lion, capsys):
        lion.move()
        move = capsys.readouterr()
        assert move.out.strip() == f"{lion.name} prowls..."

    def test_name(self, lion, capsys):
        lion.name = "Simba"
        assert lion.name == "Simba"
        lion.name = "123"
        message = capsys.readouterr()
        assert lion.name == "Simba"
        assert message.out.strip() == "Invalid name."
        lion.name = ""
        message = capsys.readouterr()
        assert lion.name == "Simba"
        assert message.out.strip() == "Invalid name."

    def test_age(self, lion, capsys):
        lion.age = 12
        assert lion.age == 12
        lion.age = -2
        message = capsys.readouterr()
        assert message.out.strip() == "Age must be greater than 0."
        lion.age = "hello"
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid age. Must be a whole number."
        lion.age = 5.5
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid age. Must be a whole number."

    def test_species(self, lion):
        assert lion.species == "Lion"

    def test_under_treatment(self, lion):
        assert lion.under_treatment == False
        lion.under_treatment = True
        assert lion.under_treatment == True
        lion.under_treatment = "False"
        assert lion.under_treatment == True

    def test_get_dietary_needs(self, lion):
        assert lion.dietary_needs == f"{lion.name} has no specific dietary needs."

    def test_add_dietary_need(self, lion, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda _: "Drinks only single malt whisky")
        lion.add_dietary_need()
        assert lion.dietary_needs == f"\nDietary Needs for {lion.name}:\n1. Drinks only single malt whisky\n"
        # Code (use of monkeypatch) inspired by:
        # mareoraft. (2016, April 2). As The Compiler suggested, pytest has a new monkeypatch fixture for this. A
        # monkeypatch object can alter an attribute in [Comment on the online forum post How to test a function with
        # input call?]. Stack Overflow. https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
        inputs = iter(["", "Another thing"])
        monkeypatch.setattr("builtins.input", lambda msg: next(inputs))
        lion.add_dietary_need()
        message = capsys.readouterr()
        assert message.out.strip() == "Entry cannot be blank."
        assert lion.dietary_needs == (f"\nDietary Needs for {lion.name}:\n1. Drinks only single malt whisky\n"
                                      f"2. Another thing\n")
        # Code (mocking multiple inputs) inspired by:
        # theY4Kman. (2020, January 31). The last monkeypatch will win out against all the others, so input(f"overwrite
        # {filename} (y/n): ") is getting "n", and so [Comment on the online forum post How to simulate two consecutive
        # console inputs with pytest monkeypatch]. Stack Overflow.
        # https://stackoverflow.com/questions/59986625/how-to-simulate-two-consecutive-console-inputs-with-pytest-monkeypatch

    def test_remove_dietary_need(self, lion, monkeypatch, capsys):
        # Try removing from empty list.
        lion.remove_dietary_need()
        message = capsys.readouterr()
        assert message.out.strip() == f"{lion.name} has no specific dietary needs.\nNothing to remove."

        # Add an item to later remove.
        monkeypatch.setattr("builtins.input", lambda _: "Drinks only single malt whisky")
        lion.add_dietary_need()

        # Remove added item.
        inputs = iter(["", "hello", "0", "-3", "2", "1"])
        monkeypatch.setattr("builtins.input", lambda msg: next(inputs))
        lion.remove_dietary_need()
        message = capsys.readouterr()
        assert message.out.strip() == (f"Dietary Needs for {lion.name}:\n1. Drinks only single malt whisky\n\n"
                                       "Please enter a whole number from the list.\nPlease enter a whole number from the list.\n"
                                       "Number cannot be 0.\nPlease enter a whole number from the list.\n"
                                       "Number is out of range. Please enter a number from the list.\nRemoved successfully.")

    def test_report(self, lion, capsys):
        lion.report()
        message = capsys.readouterr()
        assert message.out.strip() == (f"---Report for: {lion.name} (ID-{lion.id})---\n\nINJURIES\nNone\n\nILLNESSES\n"
                                       f"None\n\nBEHAVIOURAL CONCERNS\nNone")

    def test_add_note(self, lion, monkeypatch, capsys):
        inputs = iter(["", "illnesses", "4", "1", "", "Here is a desc", "today", "12/42/2913", "00/00/0000", "11-11-2004",
                       "ee/gg/fdoi", "30/02/2000", "31/11/4710", "04/11/2025", "", "medium", "med", "write some notes",
                       "", "yes", "y"])
        monkeypatch.setattr("builtins.input", lambda msg: next(inputs))
        lion.add_note()
        lion.report()
        message = capsys.readouterr()
        assert message.out.strip() == (f"---Add note for: {lion.name}---\nCategories:\n1. Injuries\n2. Illnesses\n3. "
                                       f"Behavioural concerns\n\nInvalid category.\nInvalid category.\nInvalid category.\n"
                                       f"Description cannot be blank.\nInvalid date.\nInvalid date.\nInvalid date.\n"
                                       f"Invalid date.\nInvalid date.\nInvalid date.\nInvalid date.\nInvalid input.\n"
                                       f"Invalid input.\nPlease enter y or n.\nPlease enter y or n.\nNote successfully added.\n"
                                       f"\n---Report for: {lion.name} (ID-{lion.id})---\n\nINJURIES\n1.\nDescription: Here "
                                       f"is a desc\nDate reported: 04/11/2025\nSeverity: med\nNotes: write some notes\n\n"
                                       f"ILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone")
        assert lion.under_treatment == True

    def test_remove_note(self, lion, monkeypatch, capsys):
        inputs = iter(["3", "this is a description", "04/11/2025", "high", "", "n", "1", "this is a description",
                       "11/01/2015", "low", "additional notes here", "y", "nothing", "", "something-else", "illnesses-e",
                       "injuries-0", "illnesses-3", "behavioural concerns-2", "e", "injuries-1", "n"])
        monkeypatch.setattr("builtins.input", lambda msg: next(inputs))
        lion.add_note()
        lion.add_note()
        assert lion.under_treatment == True
        lion.remove_note()
        lion.remove_note()
        assert lion.under_treatment == False
        lion.report()
        message = capsys.readouterr()
        assert message.out.strip() == (f"---Add note for: {lion.name}---\nCategories:\n1. Injuries\n2. Illnesses\n3. "
                                       f"Behavioural concerns\n\nNote successfully added.\n\n---Add note for: {lion.name}---"
                                       f"\nCategories:\n1. Injuries\n2. Illnesses\n3. Behavioural concerns\n\nNote "
                                       f"successfully added.\n\n---Report for: {lion.name} "
                                       f"(ID-{lion.id})---\n\nINJURIES\n1.\nDescription: this is a description\nDate "
                                       f"reported: 11/01/2015\nSeverity: low\nNotes: additional notes here\n\n"
                                       f"ILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\n1.\nDescription: this is a description"
                                       f"\nDate reported: 04/11/2025\nSeverity: high\nNotes: none\n\n\nInvalid entry. "
                                       f"Please use the example format.\nInvalid entry. Please use the example format.\n"
                                       f"Invalid entry. Please use the example format.\nInvalid entry. Please use the "
                                       f"example format.\nIndex cannot be 0.\nThere are no notes for that category. "
                                       f"Please choose another category or enter e to exit.\nThat category only has 1 "
                                       f"note(s). Please enter a valid index.\n\n---Report for: {lion.name} "
                                       f"(ID-{lion.id})---\n\nINJURIES\n1.\nDescription: this is a description\nDate "
                                       f"reported: 11/01/2015\nSeverity: low\nNotes: additional notes here\n\n"
                                       f"ILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\n1.\nDescription: this is a description"
                                       f"\nDate reported: 04/11/2025\nSeverity: high\nNotes: none\n\n\nNote removed successfully.\n"
                                       f"\n---Report for: {lion.name} (ID-{lion.id})---\n\nINJURIES\nNone\n\n"
                                       f"ILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\n1.\nDescription: this is a description"
                                       f"\nDate reported: 04/11/2025\nSeverity: high\nNotes: none")

    def test_species_report(self, lion, lion2, capsys):
        lion.species_report()
        message = capsys.readouterr()
        assert message.out.strip() == (f"------Species Report: Lion------\n\n---Leo (ID-1)---\n\nINJURIES\nNone\n\n"
                                       f"ILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n\n---Annie (ID-2)---\n\n"
                                       f"INJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone")

    def test_animals_report(self, lion, lion2, capsys):
        lion2.animals_report()
        message = capsys.readouterr()
        assert message.out.strip() == (f"------Report for all Animals------\n\n-----SPECIES: Lion-----\n\n"
                                       f"---Leo (ID-1)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\n"
                                       f"None\n\n\n---Annie (ID-2)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       f"BEHAVIOURAL CONCERNS\nNone")

    def test_str(self, lion, capsys):
        print(lion)
        message = capsys.readouterr()
        assert message.out.strip() == (f"---ANIMAL DETAILS---\nName: Leo\nAge: 3\nSpecies: Lion\nLeo has no specific "
                                       f"dietary needs.\n---------")
        lion.under_treatment = True
        print(lion)
        message = capsys.readouterr()
        assert message.out.strip() == (f"---ANIMAL DETAILS---\nName: Leo\nAge: 3\nSpecies: Lion\nLeo has no specific "
                                       f"dietary needs.\nLeo is undergoing treatment.\n---------")


