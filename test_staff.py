'''
File: test_staff.py
Description: A module defining a class that uses pytest to test the outputs of the abstract staff module.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from staff import Staff
from enclosure import Enclosure  # To test adding and removing staff from enclosure.

# Create a mock class with which to test the Animal class methods.
class MockStaff(Staff):
    pass  # No new methods to add.


class TestStaff:
    @pytest.fixture
    def staff(self):
        return MockStaff("Jordie")

    @pytest.fixture
    def staff_no_name(self):
        return MockStaff(123)

    @pytest.fixture
    def enclosure(self):
        return Enclosure(50, "forest")

    # Test get_id method (through property).
    def test_get_id(self, staff):
        assert staff.id == 1 or staff.id == 17

    # Test get_name methods (through property).
    def test_get_name(self, staff):
        assert staff.name == "Jordie"

    # Test that an invalid name when object created results in empty string as name.
    def test_get_name_invalid_initial_name(self, staff_no_name):
        assert staff_no_name.name == ""

    # Test set_name method.
    def test_set_name(self, staff):
        staff.name = "Rietzveld"
        assert staff.name == "Rietzveld"

    # Test set_name method with invalid name.
    def test_set_name_invalid(self, staff, capsys):
        staff.name = 5.2
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid name."
        assert staff.name == "Jordie"

    # Test get_enclosures method (through property).
    def test_get_enclosures(self, staff):
        assert staff.enclosures == []

    # Test get_role method (through property).
    def test_get_role(self, staff):
        assert staff.role == "MockStaff"

    # Test get_duties method (through property).
    def test_get_duties(self, staff):
        assert staff.duties == ["general"]

    # Test that calling add_to_enclosure methods doesn't add the enclosure twice.
    def test_add_to_enclosure(self, staff, enclosure, capsys):
        enclosure.add_staff(staff)                # Add staff to enclosure.
        assert staff.enclosures == [enclosure]    # Check that enclosure added to list.
        staff.add_to_enclosure(enclosure)         # Try adding enclosure again.
        assert staff.enclosures == [enclosure]    # Check enclosure only in list once.

    # Test adding enclosure to list when staff is not assigned to enclosure.
    def test_add_to_unassigned_enclosure(self, staff, enclosure, capsys):
        staff.add_to_enclosure(enclosure)
        message = capsys.readouterr()
        assert message.out.strip() == "Staff is not assigned to enclosure. Must assign staff using enclosure object."
        assert staff.enclosures == []

    # Test trying to add invalid enclosure (check enclosures list and printed message).
    def test_add_to_enclosure_invalid(self, staff, capsys):
        staff.add_to_enclosure("room")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid enclosure."
        assert staff.enclosures == []

    # Test removing staff from an enclosure.
    def test_remove_from_enclosure(self, staff, enclosure, capsys):
        enclosure.add_staff(staff)
        staff.remove_from_enclosure(enclosure)
        assert staff.enclosures == [enclosure]
        message = capsys.readouterr()
        assert message.out.strip() == ("Jordie assigned to general duties in enclosure 57.\n"
                                       "Staff is has not been removed from the enclosure. Must remove staff using "
                                       "enclosure object.")

    # Test trying to remove staff from enclosure they were not assigned to.
    def test_remove_from_enclosure_not_assigned(self, staff, enclosure, capsys):
        staff.remove_from_enclosure(enclosure)
        message = capsys.readouterr()
        assert message.out.strip() == "Staff is not assigned to enclosure. Must assign staff using enclosure object."

    # Test removing staff from invalid enclosure.
    def test_remove_from_enclosure_invalid(self, staff, capsys):
        staff.remove_from_enclosure("something")
        message = capsys.readouterr()
        assert message.out.strip() == "Invalid enclosure."

    # Test that two staff objects are not equal.
    def test_unequal(self, staff, staff_no_name):
        assert staff != staff_no_name

    # Test that a staff object is equal to itself.
    def test_equal(self, staff):
        assert staff == staff