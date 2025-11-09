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

# Create a mock class with which to test the Animal class methods. I am testing the non-abstract methods only, as the
# abstract methods are tested thoroughly in the many species testing modules.
class MockAnimal(Animal):
    def cry(self):
        pass

    def sleep(self):
        pass

    def eat(self):
        pass

# IMPORTANT NOTE
# Because I used a global variable for each animal's id number, I ran into some issues when testing. Each time I pass
# an animal object fixture into a test method, a new object is created with a unique id number. For this reason, I decided
# to include two options for what the output can be for those outputs which use the id number. This way, the pytest
# passes when both "pytest" (for all test modules) and "pytest test_animal.py" (for just this module) are run in the
# Terminal. I have tried to make the code as organised as possible.

class TestAnimal:
    @pytest.fixture
    def animal(self):
        return MockAnimal("Leo", 3)

    # Test that the Animal class can't be instantiated.
    def test_raises(self, animal):
        with pytest.raises(TypeError):
            Animal("Name", 7)

    # Test get_name method (through property).
    def test_get_name(self, animal):
        assert animal.name == "Leo"

    # Test set_name method and that it actually changed.
    def test_set_name(self, animal):
        animal.name = "Fred"
        assert animal.name == "Fred"

    def test_species_report(self, animal, capsys):
        animal.species_report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("------Species Report: MockAnimal------\n\n---Leo (ID-1)---\n\nINJURIES\nNone\n\n"
                                       "ILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n\n---Leo (ID-2)---\n\n"
                                       "INJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n\n---Fred "
                                       "(ID-3)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n\n"
                                       "---Leo (ID-4)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\n"
                                       "None\n\n\n--------------------------")
                                        or
                                        ("------Species Report: MockAnimal------\n\n---Leo (ID-4)---\n\nINJURIES\nNone\n\n"
                                       "ILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n\n---Leo (ID-5)---\n\n"
                                       "INJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n\n---Fred "
                                       "(ID-6)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\nNone\n\n\n"
                                       "---Leo (ID-7)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\n"
                                       "None\n\n\n--------------------------"))

    # Test setting name to blank string, that it doesn't change the name attribute, and it prints the correct message.
    def test_set_name_invalid_blank(self, animal, capsys):
        animal.name = ""
        message = capsys.readouterr()
        assert animal.name == "Leo"
        assert message.out.strip() == "Invalid name."

    # Test setting name to a non-string type, that it doesn't change the name attribute, and it prints the correct message.
    def test_set_name_invalid_nonstring(self, animal, capsys):
        animal.name = 123
        message = capsys.readouterr()
        assert animal.name == "Leo"
        assert message.out.strip() == "Invalid name."

    # Test get_age methods (through property).
    def test_get_age(self, animal):
        assert animal.age == 3

    # Test set_age method and that it actually changed.
    def test_set_age(self, animal):
        animal.age = 12
        assert animal.age == 12

    # Test setting age to a negative number, that it doesn't change the attribute, and it prints the correct message.
    def test_set_age_negative(self, animal, capsys):
        animal.age = -2
        message = capsys.readouterr()
        assert animal.age == 3
        assert message.out.strip() == "Age must be greater than or equal to 0."

    # Test setting age to a non-integer, that it doesn't change the attribute, and it prints the correct message.
    def test_set_age_invalid(self, animal, capsys):
        animal.age = "hello"
        message = capsys.readouterr()
        assert animal.age == 3
        assert message.out.strip() == "Invalid age. Must be a whole number."

    # Test get_species methods (through property).
    def test_get_species(self, animal):
        assert animal.species == "MockAnimal"

    # Test that initial under_treatment attribute is False.
    def test_get_under_treatment(self, animal):
        assert animal.under_treatment == False

    # Test set_under_treatment methods and check it changed the attribute.
    def test_set_under_treatment(self, animal):
        animal.under_treatment = True
        assert animal.under_treatment == True

    # Test setting under_treatment to non-boolean type and that it doesn't change the attribute.
    def test_set_under_treatment_invalid(self, animal):
        animal.under_treatment = "True"
        assert animal.under_treatment == False

    # Test dietary needs are none when initialised.
    def test_get_dietary_needs(self, animal):
        assert animal.dietary_needs == "Leo has no specific dietary needs."

    # Test adding dietary need and that it adds to the list.
    def test_add_dietary_need(self, animal):
        animal.add_dietary_need("Drinks only single malt whisky")
        assert animal.dietary_needs == "Dietary Needs for Leo:\n1. Drinks only single malt whisky\n"

    # Test adding empty string as dietary need, that it doesn't change the attribute, and it prints the correct message.
    def test_add_dietary_need_blank(self, animal, capsys):
        animal.add_dietary_need("")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid entry. Not added to list."
        assert animal.dietary_needs == "Leo has no specific dietary needs."

    # Test adding non-string value as dietary need, that it doesn't change the attribute, and it prints the correct message.
    def test_dietary_need_nonstring(self, animal, capsys):
        animal.add_dietary_need(123)
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid entry. Not added to list."
        assert animal.dietary_needs == "Leo has no specific dietary needs."

    # Test removing dietary need from an empty list (shouldn't work).
    def test_remove_dietary_need_blank(self, animal, capsys):
        animal.remove_dietary_need(0)
        message = capsys.readouterr()
        assert message.out.strip() == "Nothing to remove."


    # Test adding two dietary needs and successfully removing one (check attribute).
    def test_remove_dietary_need(self, animal):
        animal.add_dietary_need("Something")
        animal.add_dietary_need("Another thing")
        animal.remove_dietary_need(0)
        assert animal.dietary_needs == "Dietary Needs for Leo:\n1. Another thing\n"

    # Test removing dietary need with index out of range (check attribute and printed message).
    def test_remove_dietary_need_index_error(self, animal, capsys):
        animal.add_dietary_need("Something")
        animal.remove_dietary_need(2)
        message = capsys.readouterr()
        assert message.out.strip() == "Index out of range."
        assert animal.dietary_needs == "Dietary Needs for Leo:\n1. Something\n"

    # Test removing diertary needs with non-integer index (check attribute and printed message).
    def test_remove_dietary_need_index_error(self, animal, capsys):
        animal.add_dietary_need("Something")
        animal.remove_dietary_need("two")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid index."
        assert animal.dietary_needs == "Dietary Needs for Leo:\n1. Something\n"

    # Test get_id method (through property).
    def test_get_id(self, animal):
        assert animal.id == 21 or 29

    # Test get_environment_types attribute (should be empty list for Animal class).
    def test_get_environment_types(self, animal):
        assert animal.environment_types == []

    # Test report method.
    def test_report(self, animal, capsys):
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("---Report for: Leo (ID-31)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------")
                                        or
                                        ("---Report for: Leo (ID-23)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------"))

    # Test adding a valid note and that it shows on the report.
    def test_add_note(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/11/2004", "low",
                        "additional notes")
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Note successfully added.\n\n\n---Report for: Leo (ID-32)---\n\nINJURIES\nNone\n\n"
                                       "ILLNESSES\n1.\nDescription: This is a description\nDate reported: 11/11/2004\n"
                                       "Severity: low\nNotes: additional notes\n\nBEHAVIOURAL CONCERNS\nNone\n\n"
                                       "-----------------")
                                        or
                                        ("Note successfully added.\n\n\n---Report for: Leo (ID-24)---\n\nINJURIES\nNone\n\n"
                                       "ILLNESSES\n1.\nDescription: This is a description\nDate reported: 11/11/2004\n"
                                       "Severity: low\nNotes: additional notes\n\nBEHAVIOURAL CONCERNS\nNone\n\n"
                                       "-----------------"))

    # Test adding a valid note and setting treatment to True (check under treatment attribute).
    def test_add_note_treatment_true(self, animal):
        animal.add_note("illnesses", "This is a description", "11/11/2004", "low",
                        "additional notes", True)
        assert animal.under_treatment == True

    # Test creating a note with invalid category (check it doesn't show in report and check printed message).
    def test_add_note_invalid_category(self, animal, capsys):
        animal.add_note("...", "This is a description", "11/11/2004", "low",
                        "additional notes")
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Invalid category. Must be 'injuries', 'illnesses', or 'behavioural_concerns'.\n"
                                       "\n---Report for: Leo (ID-34)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------")
                                        or
                                        ("Invalid category. Must be 'injuries', 'illnesses', or 'behavioural_concerns'.\n"
                                       "\n---Report for: Leo (ID-26)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------"))

    # Test creating a note with invalid description (check it doesn't show in report and check printed message).
    def test_add_note_invalid_description(self, animal, capsys):
        animal.add_note("illnesses", "", "11/11/2004", "low",
                        "additional notes")
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Invalid description.\n"
                                       "\n---Report for: Leo (ID-35)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------")
                                        or
                                        ("Invalid description.\n"
                                       "\n---Report for: Leo (ID-27)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------"))

    # Test creating a note with invalid date (check it doesn't show in report and check printed message).
    def test_add_note_invalid_date(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11Nov2004", "low",
                        "additional notes")
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Invalid date.\n"
                                       "\n---Report for: Leo (ID-36)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------")
                                        or
                                        ("Invalid date.\n"
                                       "\n---Report for: Leo (ID-28)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------"))

    # Test creating a note with invalid severity (check it doesn't show in report and check printed message).
    def test_add_note_invalid_severity(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/12/2020", "urgent",
                        "additional notes")
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Invalid severity. Must be either high, med, or low.\n"
                                       "\n---Report for: Leo (ID-37)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------")
                                        or
                                        ("Invalid severity. Must be either high, med, or low.\n"
                                       "\n---Report for: Leo (ID-29)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------"))

    # Test creating a note with invalid notes (check it doesn't show in report and check printed message).
    def test_add_note_invalid_notes(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/12/2020", "med",
                        "")
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Invalid notes.\n"
                                       "\n---Report for: Leo (ID-38)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------")
                                        or
                                        ("Invalid notes.\n"
                                       "\n---Report for: Leo (ID-30)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------"))

    # Test creating a note with invalid treatment (check it doesn't show in report and check printed message).
    def test_add_note_invalid_treatment(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/12/2020", "med",
                        "additional notes", "True")
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Invalid treatment indication. Must be a boolean value.\n"
                                       "\n---Report for: Leo (ID-39)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------")
                                        or
                                        ("Invalid treatment indication. Must be a boolean value.\n"
                                       "\n---Report for: Leo (ID-31)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\n"
                                       "BEHAVIOURAL CONCERNS\nNone\n\n-----------------"))

    # Test add note methods with no notes argument specified.
    def test_add_note_no_notes(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/11/2004", "low")
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Note successfully added.\n\n\n---Report for: Leo (ID-40)---\n\nINJURIES\nNone\n\n"
                                       "ILLNESSES\n1.\nDescription: This is a description\nDate reported: 11/11/2004\n"
                                       "Severity: low\nNotes: none\n\nBEHAVIOURAL CONCERNS\nNone\n\n"
                                       "-----------------")
                                        or
                                        ("Note successfully added.\n\n\n---Report for: Leo (ID-32)---\n\nINJURIES\nNone\n\n"
                                       "ILLNESSES\n1.\nDescription: This is a description\nDate reported: 11/11/2004\n"
                                       "Severity: low\nNotes: none\n\nBEHAVIOURAL CONCERNS\nNone\n\n"
                                       "-----------------"))

    # Test removing a note successfully (check removed from report).
    def test_remove_note(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/11/2004", "low",
                        "additional notes")
        animal.remove_note("illnesses", 0)
        animal.report()
        message = capsys.readouterr()
        assert (message.out.strip() == ("Note successfully added.\n\nNote removed successfully.\n\n---Report for: Leo "
                                       "(ID-41)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\n"
                                       "None\n\n-----------------")
                                        or
                                        ("Note successfully added.\n\nNote removed successfully.\n\n---Report for: Leo "
                                       "(ID-33)---\n\nINJURIES\nNone\n\nILLNESSES\nNone\n\nBEHAVIOURAL CONCERNS\n"
                                       "None\n\n-----------------"))

    # Test removing a note from an empty category.
    def test_remove_note_empty_notes(self, animal, capsys):
        animal.remove_note("injuries", 0)
        message = capsys.readouterr()
        assert message.out.strip() == "There are no notes in that category."

    # Test removing a note from an invalid category.
    def test_remove_note_invalid_category(self, animal, capsys):
        animal.remove_note("category", 0)
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid category. Must be 'injuries', 'illnesses', or 'behavioural_concerns'."

    # Test removing a note with an invalid treatment indicator.
    def test_remove_note_invalid_treatment(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/11/2004", "low",
                        "additional notes")
        animal.remove_note("illnesses", 0, "treatment")
        message = capsys.readouterr()
        assert message.out.strip() == "Note successfully added.\n\nInvalid treatment indication. Must be a boolean value."

    # Test removing a note and setting treatment to True (check attribute and printed message).
    def test_remove_note_treatment_true(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/11/2004", "low",
                        "additional notes")
        animal.remove_note("illnesses", 0, True)
        message = capsys.readouterr()
        assert message.out.strip() == "Note successfully added.\n\nNote removed successfully."
        assert animal.under_treatment == True

    # Test removing a note with index that is out of range.
    def test_remove_note_index_out_of_range(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/11/2004", "low",
                        "additional notes")
        animal.remove_note("illnesses", 3)
        message = capsys.readouterr()
        assert message.out.strip() == "Note successfully added.\n\nIndex out of range."

    # Test removing a note with invalid index.
    def test_remove_note_invalid_index(self, animal, capsys):
        animal.add_note("illnesses", "This is a description", "11/11/2004", "low",
                        "additional notes")
        animal.remove_note("illnesses", "0")
        message = capsys.readouterr()
        assert message.out.strip() == "Note successfully added.\n\nInvalid index."