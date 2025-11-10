'''
File: animal.py
Description: A module defining an abstract class that represents a general zoo animal.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    '''
    An abstract class which represents a zoo animal.

    Parameters:
        name : A string representing the name of the animal.
        age : An integer representing the age of the animal in years.

    Attributes:
        id : An integer unique to this animal object (not shared by other objects which inherit this class).
        species : The species of the animal (the class name).
        name : Name of the animal.
        age : Age of the animal in years (integer only).
        dietary needs : A list of the animal's dietary needs (a list of strings).
        under_treatment : A boolean value indicating whether the animal is currently undergoing treatment.
        environment_types : A list of strings indicating which environments the animal can live in.
        enclosure : Shows what zoo enclosure, if any, the animal is currently in (either None or an object of Enclosure class).

    Class Methods:
        set_name(name) : Changes the animal's name.

        set_age(age) : Changes the animal's age.

        get_name() : Returns the animal's name.

        get_age() : Returns the animal's age.

        get_species() : Returns the animal's species (class name).

        get_under_treatment() : Returns Boolean indicating if animal is under treatment.

        set_under_treatment(under_treatment) : Changes the animal's under_treatment attribute.

        get_dietary_needs() : Returns a formatted string of the animal's dietary needs list.

        add_dietary_need(dietary_need) : Adds the specified dietary need to the animal's list.

        remove_dietary_need(index) : Removes a dietary need at a specified position (index).

        get_id() : Returns the animal's id number.

        get_environment_types() : Returns a list of the environments the animal can live in.

        add_note(category, description, date_reported, severity, notes, treatment) : Adds a note with the specified details to the animal's record.

        remove_note(category, index, treatment) : Removes a specified note from the animal's record.

        report() : Displays the animal's current notes.

        species_report() : Displays a report for each animal which shares the target animal's species.

        animals_report() : Displays a report for all instantiated animals.

        get_enclosure() : Returns None (if animal not in enclosure) or an Enclosure object (the animal is currently in that enclosure).

        add_to_enclosure(enclosure) : Updates the animal's enclosure attribute.

        remove_from_enclosure(enclosure) : Updates the animal's enclosure attribute.

        __eq__(other) : Determines if the object and another specified object are equal.

        __str__() : Displays the animal's details.

    Abstract Methods:
        cry() : Must display a message showing what sound the animal makes.

        sleep() : Must display a message about how the animal sleeps.

        eat() : Must display a message about how/what the animal eats.

    Properties:
        id : get_id()

        name : get_name(), set_name()

        age : get_age(), set_age()

        species : get_species()

        dietary_needs : get_dietary_needs()

        under_treatment : get_under_treatment(), set_under_treatment()

        environment_types : get_environment_types()

        enclosure : get_enclosure()
    '''

    # Global attributes.
    __notes = {}  # Registry/notes for all animals.
    __next_id = 1  # Holds the next id number (to ensure all unique).
    __species = set()  # A unique set (list) of all instantiated species.

    def __init__(self, name, age):
        self.__id = self.__create_id()
        self.__species = self.__class__.__name__
        self.__name = self.__species
        self.__age = None
        self.__dietary_needs = []
        self.__under_treatment = False
        self.__environment_types = []
        self.__enclosure = None

        self.__add_object_to_notes()  # Add object to global registry.
        self.set_name(name)  # Check name is valid before accepting.
        self.set_age(age)  # Check age is valid before accepting.
        Animal.__species.add(self.__species)  # Add species to global set.

    def set_name(self, name: str) -> None:
        '''
        Parameters:
            name : The new name of the animal (must be a string to be accepted).

        Returns:
            None

        If the provided name is valid (a string that isn't blank), changes the animal's name to the given string.
        If the name is invalid, prints an error message and the animal's name doesn't change.
        '''
        if type(name) == str and name != "":
            # Update name variable.
            self.__name = name

            # Update global registry.
            animal_record = Animal.__notes.get(f"{self.__species}-{self.__id}")
            animal_record.update({"name": name})
        else:
            print("Invalid name.")

    def set_age(self, age: int) -> None:
        '''
        Parameters:
            age : The new age (in years) of the animal (must be an integer to be accepted).

        Returns:
            None

        If the given value is a valid integer (at least 0), changes the animal's age to the given value.
        If the value is invalid, prints an error message and the animal's age doesn't change.
        '''
        if type(age) == int and age >= 0:
            self.__age = age
        elif type(age) == int and age < 0:
            print("Age must be greater than or equal to 0.")
        else:
            print("Invalid age. Must be a whole number.")

    def get_name(self) -> str:
        '''
        Returns:
            string

        Returns the animal's current name.
        '''
        return self.__name

    def get_age(self) -> int | str:
        '''
        Returns:
            integer or string

        Returns the age of the animal. If the animal's age is not recorded, returns "Age not specified".
        '''
        return self.__age if self.__age is not None else "Age not specified"

    def get_species(self) -> str:
        '''
        Returns:
             string

        Returns the animal's species (eg. Lion or Penguin).
        '''
        return self.__species

    def get_under_treatment(self) -> bool:
        '''
        Returns:
             boolean

        Returns a boolean value indicating if the animal is currently undergoing any treatment.
        '''
        return self.__under_treatment

    def set_under_treatment(self, under_treatment: bool) -> None:
        '''
        Parameters:
            under_treatment : A boolean value indicating if the animal is under treatment.

        Returns:
            None

        If the given value is a boolean (True or False), changes the animal's under_treatment attribute to the given value.
        If the new value is True and the animal is currently in an enclosure, the animal is removed from the enclosure
        to undergo the treatment.
        '''
        # Validate given argument.
        if type(under_treatment) == bool:
            self.__under_treatment = under_treatment

        # Remove the animal from any enclosure if undergoing treatment.
        if self.under_treatment and self.enclosure is not None:
            self.__enclosure.remove_animal(self)

    def get_dietary_needs(self) -> str:
        '''
        Returns:
            string

        Returns a formatted string showing the animal's dietary needs.
        If the animal has no dietary needs, returns "<name> has no specific dietary needs."
        '''
        if self.__dietary_needs == []:
            result = f"{self.__name} has no specific dietary needs."
        else:
            result = f"Dietary Needs for {self.__name}:\n"
            count = 1
            for item in self.__dietary_needs:
                result += f"{count}. {item}\n"
                count += 1
        return result

    def add_dietary_need(self, dietary_need: str) -> None:
        '''
        Parameters:
            dietary_need : A string of the dietary need to add to the animal's list.

        Returns:
            None

        If the provided string is valid (not blank), it is added to the animal's list of dietary needs.
        If the value is invalid, an error message is displayed.
        '''
        if type(dietary_need) == str and dietary_need != "":
            self.__dietary_needs.append(dietary_need)
        else:
            print("Invalid entry. Not added to list.")

    def remove_dietary_need(self, index: int) -> None:
        '''
        Parameters:
            index : An integer indicating the index of the note to remove from the dietary needs list (starting at 0).

        Returns:
            None

        If the index is valid (an integer in range of the current list), the specified note is deleted.
        If there is nothing in the animal's dietary needs list, an error message is displayed.
        If the index is invalid, displays an error message.

        '''
        try:
            if self.__dietary_needs == []:
                print("Nothing to remove.")
            else:
                del self.__dietary_needs[index]
        except (IndexError, TypeError) as e:
            if e.__class__.__name__ == "IndexError":
                print("Index out of range.")
            else:
                print("Invalid index.")

    def get_id(self) -> int:
        '''
        Returns:
             integer

        Returns the animal's id number.
        '''
        return self.__id

    def __create_id(self) -> int:
        '''
        Returns:
             integer

        A private method used when the class is instantiated to generate the animal's id number.
        '''
        temp = Animal.__next_id
        Animal.__next_id += 1
        return temp

    def get_environment_types(self) -> list:
        '''
        Returns:
             list (of string)

        Returns a list of the environments the animal can survive in.
        '''
        return self.__environment_types

    def __add_object_to_notes(self) -> None:
        '''
        Returns:
            None

        A private method called when the class is instantiated to add the animal's details (and blank notes template)
        to the global notes attribute.
        '''
        value = {"name": self.__name, "injuries": [], "illnesses": [], "behavioural_concerns": []}
        key = f"{self.__species}-{self.__id}"
        Animal.__notes.update({key: value})

    def __validate_date(self, date: str) -> bool:
        '''
        Parameters:
             date : A string of a date in the format dd/mm/yyyy.

        Returns:
            boolean

        A private method to determine if a given value is a valid date. Used in the add_note() method.
        '''
        # Initialise valid to True.
        valid = True

        # If any of these conditions are False, set valid to False.
        if (type(date) != str or len(date) != 10 or not (date[:2] + date[3:5] + date[6:]).isdigit() or
                (date[2] + date[5]) != "//" or date[:2].lstrip("0") == "" or
                date[3:5].lstrip("0") == "" or date[6:].lstrip("0") == "" or
                int(date[:2].lstrip("0")) < 1 or int(date[3:5].lstrip("0")) < 1
                or int(date[6:].lstrip("0")) < 1 or int(date[3:5].lstrip("0")) > 12 or
                (int(date[3:5].lstrip("0")) in [4, 6, 9, 11] and int(date[:2].lstrip("0")) > 30) or
                (int(date[3:5].lstrip("0")) in [1, 3, 5, 7, 8, 10, 12] and int(date[:2].lstrip("0")) > 31) or
                (int(date[3:5].lstrip("0")) == 2 and int(date[:2].lstrip("0")) not in [28, 29])):
            valid = False
        return valid

    def add_note(self, category: str, description: str, date_reported: str, severity: str, notes="none",
                 treatment=False) -> None:
        '''
        Parameters:
            category: A string indicating which category the note is (must be one of "injuries", "illnesses", or
            "behavioural_concerns".)
            description : A string describing the illness/injury/concern.
            date_reported : A string of a date in format dd/mm/yyyy, indicating the date the illness/injury/concern
            was first reported.
            severity : A string indicating how severe the illness/injury/concern is (must be one of "high", "med", or
            "low".)
            notes : A string of any additional notes to be included. If no notes are given, defaults to "none".
            treatment : A boolean value indicating if the animal is receiving treatment for this illness/injury/concern.
            If parameter not specified, defaults to False.

        Returns:
            None

        Adds a note to the animal's record (global notes attribute). If any provided value is invalid, displays an error
        message and the note is not added. If the note is added successfully, displays "Note successfully added."
        '''
        if category not in ["injuries", "illnesses", 'behavioural_concerns']:
            print("Invalid category. Must be 'injuries', 'illnesses', or 'behavioural_concerns'.")
        elif type(description) != str or description == "":
            print("Invalid description.")
        elif not self.__validate_date(date_reported):
            print("Invalid date.")
        elif severity not in ["high", "med", "low"]:
            print("Invalid severity. Must be either high, med, or low.")
        elif type(notes) != str or notes == "":
            print("Invalid notes.")
        elif type(treatment) != bool:
            print("Invalid treatment indication. Must be a boolean value.")
        else:
            # Get records.
            animal_record = Animal.__notes.get(f"{self.__species}-{self.__id}")
            category_record = animal_record.get(category)

            # Add new record.
            category_record.append([description, date_reported, severity, notes])
            animal_record.update({category: category_record})
            Animal.__notes.update({f"{self.__species}-{self.__id}": animal_record})

            # Update treatment attribute.
            if treatment:
                self.under_treatment = treatment

            # Print confirmation message
            print("Note successfully added.\n")

    def remove_note(self, category: str, index: int, treatment=False) -> None:
        '''
        Parameters:
            category: A string indicating which category the note is (must be one of "injuries", "illnesses", or
            "behavioural_concerns".)
            index : An integer value indicating the position of the note to remove (starting from 0).
            treatment : A boolean value indicating if the animal is still receiving treatment for another
            illness/injury/concern. If parameter not specified, defaults to False.

        Returns:
            None

        Removes a specified note from the animal's record (from the global notes attribute). If the specified category
        name or index number is invalid, displays an error message and nothing is removed.
        If the specified category has no notes, displays a message and nothing is removed.
        If the treatment or index parameters are invalid, displays a message and nothing is removed.
        '''
        # Check if category is valid.
        if category not in ["injuries", "illnesses", 'behavioural_concerns']:
            print("Invalid category. Must be 'injuries', 'illnesses', or 'behavioural_concerns'.")
        else:  # If category valid...
            try:
                # Get records.
                animal_record = Animal.__notes.get(f"{self.__species}-{self.__id}")
                category_record = animal_record.get(category)

                if category_record == []:
                    print("There are no notes in that category.")
                elif type(treatment) != bool:
                    print("Invalid treatment indication. Must be a boolean value.")
                else:
                    del category_record[index]  # This will throw Exception if index invalid.
                    self.under_treatment = treatment
                    animal_record.update({category: category_record})
                    Animal.__notes.update({f"{self.__species}-{self.__id}": animal_record})
                    print("Note removed successfully.")
            except (TypeError, IndexError) as e:  # If index is invalid...
                if e.__class__.__name__ == "IndexError":
                    print("Index out of range.")
                else:
                    print("Invalid index.")

    def report(self) -> None:
        '''
        Returns:
            None

        Displays the current notes for the animal from the global notes attribute.
        Notes are separated by category (injuries, illnesses, behavioural concerns).
        Within categories, notes are numbered (starting from 1).
        If there are no notes in a category, "None" is displayed under the category heading.

        Example:
            ---Report for: <name> (ID-<id>)---

            INJURIES

            None

            ILLNESSES

            1.

            Description: something

            Date reported: 11/11/1111

            Severity: med

            Notes: additional notes

            BEHAVIOURAL CONCERNS

            None
        '''
        # Get whole record.
        animal_record = Animal.__notes.get(f"{self.__species}-{self.__id}")

        # Get string of each record category.
        injuries = ""
        if animal_record.get("injuries") == []:
            injuries += "None\n\n"
        else:
            count = 1
            for note in animal_record.get("injuries"):
                injuries += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                count += 1

        illnesses = ""
        if animal_record.get("illnesses") == []:
            illnesses += "None\n\n"
        else:
            count = 1
            for note in animal_record.get("illnesses"):
                illnesses += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                count += 1

        behavioural_concerns = ""
        if animal_record.get("behavioural_concerns") == []:
            behavioural_concerns += "None\n\n"
        else:
            count = 1
            for note in animal_record.get("behavioural_concerns"):
                behavioural_concerns += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                count += 1

        # Print results.
        print(f"\n---Report for: {self.__name} (ID-{self.__id})---\n\n"
              f"INJURIES\n{injuries}ILLNESSES\n{illnesses}BEHAVIOURAL CONCERNS\n{behavioural_concerns}-----------------")

    def species_report(self) -> None:
        '''
        Returns:
            None

        Displays the current notes for all animals which share this animal's species.
        Notes are separated by animal, then category (injuries, illnesses, behavioural concerns).
        Within categories, notes are numbered (starting from 1).
        If there are no notes in a category, "None" is displayed under the category heading.

        Example:
            ------Species Report: Lion------

            ---<name> (ID-<id>)---

            INJURIES

            None

            ILLNESSES

            1.

            Description: something

            Date reported: 11/11/1111

            Severity: med

            Notes: additional notes

            BEHAVIOURAL CONCERNS

            None
        '''
        print(f"\n------Species Report: {self.__species}------\n")
        for key in Animal.__notes:
            if self.__species in key:
                # Get animal's record.
                animal_record = Animal.__notes.get(key)

                # Get string of each record category.
                injuries = ""
                if animal_record.get("injuries") == []:
                    injuries += "None\n\n"
                else:
                    count = 1
                    for note in animal_record.get("injuries"):
                        injuries += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                        count += 1

                illnesses = ""
                if animal_record.get("illnesses") == []:
                    illnesses += "None\n\n"
                else:
                    count = 1
                    for note in animal_record.get("illnesses"):
                        illnesses += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                        count += 1

                behavioural_concerns = ""
                if animal_record.get("behavioural_concerns") == []:
                    behavioural_concerns += "None\n\n"
                else:
                    count = 1
                    for note in animal_record.get("behavioural_concerns"):
                        behavioural_concerns += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                        count += 1

                # Print results.
                print(f"---{animal_record.get("name")} (ID-{key.split("-")[1]})---\n\n"
                      f"INJURIES\n{injuries}ILLNESSES\n{illnesses}BEHAVIOURAL CONCERNS\n{behavioural_concerns}")

        print("--------------------------")

    def animals_report(self) -> None:
        '''
        Returns:
            None

        Displays the current notes for all instantiated animals, separated by species.
        Notes are separated by animal, then category (injuries, illnesses, behavioural concerns).
        Within categories, notes are numbered (starting from 1).
        If there are no notes in a category, "None" is displayed under the category heading.

        Example:
            ------Report for all Animals------

            ------SPECIES: Lion------

            ---<name> (ID-<id>)---

            INJURIES

            None

            ILLNESSES

            1.

            Description: something

            Date reported: 11/11/1111

            Severity: med

            Notes: additional notes

            BEHAVIOURAL CONCERNS

            None
        '''
        print(f"\n------Report for all Animals------\n")

        # Get list of species in alphabetical order.
        species_list = [item for item in Animal.__species]
        species_list.sort()

        for species in species_list:
            print(f"-----SPECIES: {species}-----\n")
            for key in Animal.__notes:
                if species in key:
                    # Get animal's record.
                    animal_record = Animal.__notes.get(key)

                    # Get string of each record category.
                    injuries = ""
                    if animal_record.get("injuries") == []:
                        injuries += "None\n\n"
                    else:
                        count = 1
                        for note in animal_record.get("injuries"):
                            injuries += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                            count += 1

                    illnesses = ""
                    if animal_record.get("illnesses") == []:
                        illnesses += "None\n\n"
                    else:
                        count = 1
                        for note in animal_record.get("illnesses"):
                            illnesses += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                            count += 1

                    behavioural_concerns = ""
                    if animal_record.get("behavioural_concerns") == []:
                        behavioural_concerns += "None\n\n"
                    else:
                        count = 1
                        for note in animal_record.get("behavioural_concerns"):
                            behavioural_concerns += f"{count}.\nDescription: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"
                            count += 1

                    # Print results.
                    print(f"---{animal_record.get("name")} (ID-{key.split("-")[1]})---\n\n"
                          f"INJURIES\n{injuries}ILLNESSES\n{illnesses}BEHAVIOURAL CONCERNS\n{behavioural_concerns}")

        print("------------------------------")

    def get_enclosure(self):
        '''
        Returns:
            Enclosure object or None

        Returns either None (meaning the animal is not in an enclosure) or an Enclosure object (indicating the
        enclosure in which the animal is located).
        '''
        return self.__enclosure

    def add_to_enclosure(self, enclosure) -> None:
        '''
        Parameters:
             enclosure : An Enclosure object, to which the animal will be added.

        Returns:
            None

        Adds the animal into a specified enclosure.
        Note that this method cannot actually add an animal into an enclosure. That must be done using the Enclosure
        object itself. This method is to set the animal's enclosure attribute to the enclosure it is currently in.

        If the animal is already in an enclosure, displays an error message.
        If the animal has not been added to the enclosure using the Enclosure object, displays an error message.
        If the provided enclosure is invalid, displays an error message.
        '''
        try:
            check = enclosure.cleanliness_level  # Throw an exception if not Enclosure object.

            if self.__enclosure == enclosure:
                print("Animal is already in this enclosure.")
            elif self.__enclosure is not None:
                print("Animal is already in an another enclosure.")
            elif self not in enclosure.animals:
                print("Animal is not in this enclosure. Must first add animal using enclosure object.")
            else:
                self.__enclosure = enclosure
        except AttributeError:
            print("Invalid enclosure.")

    def remove_from_enclosure(self, enclosure) -> None:
        '''
        Parameters:
             enclosure : An Enclosure object, from which the animal will be removed.

        Returns:
            None

        Removed the animal from a specified enclosure.
        Note that this method cannot actually remove an animal from an enclosure. That must be done using the Enclosure
        object itself. This method is to set the animal's enclosure attribute to None if the animal is successfully removed.

        If the animal is not in any enclosure, displays an error message.
        If the animal is not in the specified enclosure, displays an error message.
        If the provided enclosure is invalid, displays an error message.
        '''
        try:
            check = enclosure.cleanliness_level  # Throw an exception if not Enclosure object.

            if self.enclosure is None:
                print("Animal is not in any enclosure.")
            elif self.enclosure != enclosure:
                print("Animal is in another enclosure.")
            else:
                self.__enclosure = None
        except AttributeError:
            print("Invalid enclosure.")

    @abstractmethod
    def cry(self) -> None:
        '''
        Returns:
            None

        Displays the animal's sound.
        '''
        pass

    @abstractmethod
    def sleep(self) -> None:
        '''
        Returns:
            None

        Displays how the animal sleeps.
        '''
        pass

    @abstractmethod
    def eat(self) -> None:
        '''
        Returns:
            None

        Displays how/what the animal eats.
        '''
        pass

    # Properties
    id = property(get_id)
    name = property(get_name, set_name)
    age = property(get_age, set_age)
    species = property(get_species)
    dietary_needs = property(get_dietary_needs)
    under_treatment = property(get_under_treatment, set_under_treatment)
    environment_types = property(get_environment_types)
    enclosure = property(get_enclosure)

    def __eq__(self, other: Animal) -> bool:
        '''
        Parameters:
            other : Another Animal object to which this object is compared.

        Returns:
            boolean

        Compares two Animal objects and returns True of the objects are equal or False if not.
        The objects are equal if they are both of the Animal class and have the same id number.
        '''
        return isinstance(other, Animal) and self.id == other.id

    def __str__(self) -> str:
        '''
        Returns:
             string

        Returns a string of the animal's details in the following format:

        ---ANIMAL DETAILS---

        ID: <id>

        Name: <name>

        Age: <age> or "Age not specified"

        Species: <species>

        Environment types: <eg. grassland, tropical>

        Dietary needs for <name>:

        1. something

        2. another thing

        <only if animal undergoing treatment>
        <name> is undergoing treatment.

        ---------
        '''
        age_statement = f"{self.age} years" if type(self.age) == int else self.age
        treatment_statement = f"{self.name} is undergoing treatment.\n" if self.under_treatment else ""

        environment_statement = f"Environment types: "
        if self.environment_types == []:
            environment_statement += f"none specified"
        else:
            for item in self.environment_types:
                environment_statement += f"{item}, "

        return (f"\n---ANIMAL DETAILS---\nID: {self.id}\nName: {self.name}\nAge: {age_statement}\n"
                f"Species: {self.species}\n{environment_statement.strip(", ")}\n{self.dietary_needs}\n{treatment_statement}---------")
