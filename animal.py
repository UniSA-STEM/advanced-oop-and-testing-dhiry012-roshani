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
    __notes = {}
    __next_id = 1
    __species = set()

    def __init__(self, name, age):
        self.__id = self.__create_id()
        self.__species = self.__class__.__name__
        self.__name = self.__species
        self.__age = None
        self.__dietary_needs = []
        self.__under_treatment = False
        self.__environment_types = []
        self.__enclosure = None

        self.__add_object_to_notes()
        self.set_name(name)
        self.set_age(age)
        Animal.__species.add(self.__species)

    def set_name(self, name):
        '''
        Takes a string as a parameter.
        If the name is valid, sets the name attribute to the given string.
        If the name is invalid, prints an error message.
        '''
        if type(name) == str and name != "":
            self.__name = name
            animal_record = Animal.__notes.get(f"{self.__species}-{self.__id}")
            animal_record.update({"name": name})
        else:
            print("Invalid name.")

    def set_age(self, age):
        '''
        Takes one parameter.
        If the argument is a positive integer, sets the argument as the animal's age.
        If the argument is invalid, prints an error message.
        '''
        if type(age) == int and age > 0:
            self.__age = age
        elif type(age) == int and age <= 0:
            print("Age must be greater than 0.")
        else:
            print("Invalid age. Must be a whole number.")

    def get_name(self):
        '''Returns a string of the animal's name.'''
        return self.__name

    def get_age(self):
        '''Returns the animal's age, or "Age not specified" if age is None.'''
        return self.__age if self.__age is not None else "Age not specified"

    def get_species(self):
        '''Returns the animal's species (eg. Lion) as a string.'''
        return self.__species

    def get_under_treatment(self):
        '''Returns boolean value indicating if the animal is currently undergoing treatment.'''
        return self.__under_treatment

    def set_under_treatment(self, under_treatment:bool):
        '''
        Takes a boolean parameter indicating if the animal is currently undergoing treatment.
        If the given argument is a valid boolean value, it is set as the under_treatment attribute.
        This method returns nothing.
        '''
        if type(under_treatment) == bool:
            self.__under_treatment = under_treatment

        if self.under_treatment and self.enclosure is not None:
            self.__enclosure.remove_animal(self)

    def get_dietary_needs(self):
        '''
        Returns a string of the animal's dietary needs in the following format:

        ---Dietary Needs for <name>---

        1. first

        2. second

        If the animal has no dietary needs listed, will return "<name> has no specific dietary needs."
        '''
        if self.__dietary_needs == []:
            result = f"{self.__name} has no specific dietary needs."
        else:
            result = f"\nDietary Needs for {self.__name}:\n"
            count = 1
            for item in self.__dietary_needs:
                result += f"{count}. {item}\n"
                count += 1
        return result

    def add_dietary_need(self, dietary_need:str):
        '''
        This method adds a dietary need for the animal. Users are prompted to enter the note via input.
        This method takes no parameters and returns nothing.
        '''
        if type(dietary_need) == str and dietary_need != "":
            self.__dietary_needs.append(dietary_need)
        else:
            print("Invalid entry. Not added to list.")

    def remove_dietary_need(self, index:int):
        '''
        This method removes a specified dietary need from the list.
        It displays the current dietary needs of the animal and prompts the user to enter the number (index) of the
        note to delete.
        If there are no dietary needs listed, the method will not work (it will just display a message).
        This method takes no parameters and returns nothing.
        '''
        try:
            if self.__dietary_needs == []:
                print("Nothing to remove.")
            elif index >= 0 and index < len(self.__dietary_needs):
                del self.__dietary_needs[index]
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid index.")

    def get_id(self):
        '''Returns an integer of the animal's ID number.'''
        return self.__id

    def __create_id(self):
        '''Returns an integer for the object's id number.'''
        temp = Animal.__next_id
        Animal.__next_id += 1
        return temp

    def get_environment_types(self):
        '''Returns a list of what environments the animal can live in.'''
        return self.__environment_types

    def __add_object_to_notes(self):
        '''A private method that adds a blank entry to the global notes attribute.'''
        value = {"name": self.__name, "injuries": [], "illnesses": [], "behavioural_concerns": []}
        key = f"{self.__species}-{self.__id}"
        Animal.__notes.update({key: value})

    def __validate_date(self, date):
        valid = True
        if (type(date) != str or len(date) != 10 or not (date[:2]+date[3:5]+date[6:]).isdigit() or
               (date[2]+date[5]) != "//" or date[:2].lstrip("0") == "" or
               date[3:5].lstrip("0") == "" or date[6:].lstrip("0") == "" or
               int(date[:2].lstrip("0")) < 1 or int(date[3:5].lstrip("0")) < 1
               or int(date[6:].lstrip("0")) < 1 or int(date[3:5].lstrip("0")) > 12 or
               (int(date[3:5].lstrip("0")) in [4, 6, 9, 11] and int(date[:2].lstrip("0")) > 30) or
               (int(date[3:5].lstrip("0")) in [1, 3, 5, 7, 8, 10, 12] and int(date[:2].lstrip("0")) > 31) or
               (int(date[3:5].lstrip("0")) == 2 and int(date[:2].lstrip("0")) not in [28, 29])):
            valid = False
        return valid

    def add_note(self, category, description, date_reported, severity, notes="none", treatment=False):
        '''
        This method prompts the user to add a new note to the animal object's file.
        It takes no parameters and gathers information through input statements.
        The user needs to choose the note category (injury, illness, or behavioural concern).
        Then, the user must enter a description, the date it was reported, the severity, and any additional notes.
        The user is also asked if the animal is undergoing treatment for this issue. If yes, the animal's under
        treatment attribute is set to True.
        This note is then added to the animal's record in the global notes variable.
        If added successfully, a message will be displayed.
        '''
        if category not in ["injuries", "illnesses", 'behavioural_concerns']:
            print("Invalid category. Must be 'injuries', 'illnesses', or 'behavioural_concerns'.")
        elif type(description) != str or description == "":
            print("Invalid description.")
        elif not self.__validate_date(date_reported):
            print("Invalid date.")
        elif severity not in ["high", "med", "low"]:
            print("Invalid severity. Must be either high, med, or low.")
        elif type(notes) != str:
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

            # Print confirmation message
            print("Note successfully added.\n")

    def remove_note(self, category, index, treatment=False):
        '''
        This method deletes a specified note from the animal's individual record.
        The animal's report is displayed and the user is prompted to enter which note they want to remove. It must be in
        the format "category-index". For example, "injuries-2" or "behavioural concerns-4".
        The user can enter "e" to exit the method and no changes will be made to the animal's record.
        If a valid note is selected, the note is permanently removed from the animal's record.
        The user is also asked if the animal is still undergoing treatment for another issue. If yes, the animal's under
        treatment attribute is set to True. If no, the animal's under treatment attribute is set to False.
        This method takes no parameters and returns nothing.
        '''
        if category not in ["injuries", "illnesses", 'behavioural_concerns']:
            print("Invalid category. Must be 'injuries', 'illnesses', or 'behavioural_concerns'.")
        else:
            try:
                animal_record = Animal.__notes.get(f"{self.__species}-{self.__id}")
                category_record = animal_record.get(category)
                if category_record == []:
                    print("There are no notes in that category.")
                elif 0 > index >= len(category_record):
                    print(f"Invalid index. Must be between 0 and {len(category_record) - 1}, inclusive.")
                elif type(treatment) != bool:
                    print("Invalid treatment indication. Must be a boolean value.")
                else:
                    self.under_treatment = treatment
                    del category_record[index]
                    animal_record.update({category: category_record})
                    Animal.__notes.update({f"{self.__species}-{self.__id}": animal_record})
                    print("Note removed successfully.")
            except TypeError:
                print("Invalid index.")

    def report(self):
        '''
        This method prints the individual animal's current record.
        It takes no parameters and returns nothing.
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
        print(f"---Report for: {self.__name} (ID-{self.__id})---\n\n"
              f"INJURIES\n{injuries}ILLNESSES\n{illnesses}BEHAVIOURAL CONCERNS\n{behavioural_concerns}")

    def species_report(self):
        '''
        This method prints the records for all animal objects of the same species.
        It takes no parameters and returns nothing.
        '''
        print(f"------Species Report: {self.__species}------\n")
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

    def animals_report(self):
        '''
        This method prints the records of all instantiated animal objects, grouping by species.
        It takes no parameters and returns nothing.
        '''
        print(f"------Report for all Animals------\n")
        for species in Animal.__species:
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

    def get_enclosure(self):
        '''
        Returns either None, meaning the animal is current not in an enclosure, or an integer, indicating the id
        number of the enclosure the animal is in.
        '''
        return self.__enclosure

    def add_to_enclosure(self, enclosure):
        try:
            if enclosure.id == "":
                pass
            elif self.__enclosure == enclosure:
                print("Animal is already in this enclosure.")
            elif self.__enclosure is not None:
                print("Animal is already in an another enclosure.")
            elif self not in enclosure.animals:
                print("Animal is not in this enclosure. Must first add animal using enclosure object.")
            else:
                self.__enclosure = enclosure
        except AttributeError:
            print("Invalid enclosure.")

    def remove_from_enclosure(self, enclosure):
        try:
            if enclosure.id == "":
                pass
            elif self.enclosure is None:
                print("Animal is not in any enclosure.")
            elif self.enclosure != enclosure:
                print("Animal is in another enclosure.")
            else:
                self.__enclosure = None
        except AttributeError:
            print("Invalid enclosure.")

    @abstractmethod
    def cry(self):
        '''Displays the animal's sound.'''
        pass

    @abstractmethod
    def sleep(self):
        '''Displays how the animal sleeps.'''
        pass

    @abstractmethod
    def eat(self):
        '''Displays how/what the animal eats.'''
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

    def __eq__(self, other):
        '''Checks if two objects of Animal class are equal (checks id number).'''
        return isinstance(other, Animal) and self.id == other.id

    def __str__(self):
        treatment_statement = f"{self.name} is undergoing treatment.\n" if self.under_treatment else ""

        environment_statement = f"Environment types: "
        if self.environment_types == []:
            environment_statement += f"none specified"
        else:
            for item in self.environment_types:
                environment_statement += f"{item}, "

        return (f"\n---ANIMAL DETAILS---\nID: {self.id}\nName: {self.name}\nAge: {self.age} years\n"
                f"Species: {self.species}\n{environment_statement.strip(", ")}\n{self.dietary_needs}\n{treatment_statement}---------")