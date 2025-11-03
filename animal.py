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

        self.__add_object_to_notes()
        self.set_name(name)
        self.set_age(age)
        Animal.__species.add(self.__species)

    def set_name(self, name):
        '''
        Takes a string as a parameter.
        If the name is valid (letters only), sets the name attribute to the given string.
        If the name is invalid, prints an error message.
        '''
        if type(name) == str and name.isalpha():
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

    def __create_id(self):
        '''Returns an integer for the object's id number.'''
        temp = Animal.__next_id
        Animal.__next_id += 1
        return temp

    def __add_object_to_notes(self):
        '''A private method that adds a blank entry to the global notes attribute.'''
        value = {"name": self.__name, "injuries": [], "illnesses": [], "behavioural_concerns": []}
        key = f"{self.__species}-{self.__id}"
        Animal.__notes.update({key: value})

    def add_note(self):
        '''
        This method prompts the user to add a new note to the animal object's file.
        It takes no parameters and gathers information through input statements.
        The user needs to choose the note category (injury, illness, or behavioural concern).
        Then, the user must enter a description, the date it was reported, the severity, and any additional notes.
        This note is then added to the animal's record in the global notes variable.
        If added successfully, a message will be displayed.
        '''
        # Get category of note to add.
        print(f"---Add note for: {self.__name}---\n"
              f"Categories:\n1. Injuries\n2. Illnesses\n3. Behavioural concerns\n")
        category = input("Select category: ")
        while category not in ["1", "2", "3"]:
            print("Invalid category.")
            category = input("Select category: ")

        # Translate category into key.
        if category == "1":
            type = "injuries"
        elif category == "2":
            type = "illnesses"
        else:
            type = "behavioural_concerns"

        # Get specific records.
        animal_record = Animal.__notes.get(f"{self.__species}-{self.__id}")
        category_record = animal_record.get(type)

        # Get description.
        desc = input(f"Enter description: ")
        while desc == "":
            desc = input(f"Enter description: ")

        # Get and validate reported date.
        reported = input("Enter the date it was reported (dd/mm/yyyy): ")
        while (len(reported) != 10 or not (reported[:2]+reported[3:5]+reported[6:]).isdigit() or
               (reported[2]+reported[5]) != "//" or reported[:2].lstrip("0") == "" or
               reported[3:5].lstrip("0") == "" or reported[6:].lstrip("0") == "" or
               int(reported[:2].lstrip("0")) < 1 or int(reported[3:5].lstrip("0")) < 1
               or int(reported[6:].lstrip("0")) < 1 or int(reported[3:5].lstrip("0")) > 12 or
               (int(reported[3:5].lstrip("0")) in [4, 6, 9, 11] and int(reported[:2].lstrip("0")) > 30) or
               (int(reported[3:5].lstrip("0")) in [1, 3, 5, 7, 8, 10, 12] and int(reported[:2].lstrip("0")) > 31) or
               (int(reported[3:5].lstrip("0")) == 2 and int(reported[:2].lstrip("0")) not in [28, 29])):
            print("Invalid date.")
            reported = input("Enter the date it was reported (dd/mm/yyyy): ")

        # Get and validate severity.
        severity = input("Enter severity (high, med, low): ")
        while severity not in ["high", "med", "low"]:
            print("Invalid input.")
            severity = input("Enter severity (high, med, low): ")

        # Get additional notes.
        notes = input("Enter any additional notes: ")
        if notes == "":
            notes = "none"

        # Add note to record and global variable.
        category_record.append([desc, reported, severity, notes])
        animal_record.update({type: category_record})
        Animal.__notes.update({f"{self.__species}-{self.__id}": animal_record})

        # Print confirmation message
        print("Note successfully added.\n")

    def remove_note(self):
        '''
        This method deletes a specified note from the animal's individual record.
        The animal's report is displayed and the user is prompted to enter which note they want to remove. It must be in
        the format "category-index". For example, "injuries-2" or "behavioural concerns-4".
        The user can enter "e" to exit the method and no changes will be made to the animal's record.
        If a valid note is selected, the note is permanently removed from the animal's record.
        This method takes no parameters and returns nothing.
        '''
        # Show report for animal.
        self.report()

        # Get animal's record.
        animal_record = Animal.__notes.get(f"{self.__species}-{self.__id}")

        # Get note to delete (category-index).
        delete_note = input("Enter note to delete (eg injuries-1, e to exit): ")
        delete_note_split = delete_note.split("-")
        if len(delete_note_split) == 2 and delete_note_split[0] == "behavioural concerns":
            delete_note_split[0] = "behavioural_concerns"

        # Validate input.
        while (delete_note != "e" and (len(delete_note_split) != 2 or delete_note_split[0] not in ["injuries", "illnesses", "behavioural_concerns"]
                or not delete_note_split[1].isdigit() or int(delete_note_split[1]) == 0 or
                int(delete_note_split[1]) > len(animal_record.get(delete_note_split[0])))):

            if (len(delete_note_split) == 2 and delete_note_split[0] in ["injuries", "illnesses", "behavioural_concerns"]
                and delete_note_split[1].isdigit() and len(animal_record.get(delete_note_split[0])) == 0):
                print("There are no notes for that category. Please choose another category or enter e to exit.")
            elif (len(delete_note_split) == 2 and delete_note_split[0] in ["injuries", "illnesses", "behavioural_concerns"]
                and delete_note_split[1].isdigit() and int(delete_note_split[1]) > len(animal_record.get(delete_note_split[0]))):
                print(f"That category only has {len(animal_record.get(delete_note_split[0]))} note(s). Please enter a valid index.")
            else:
                print("Invalid entry. Please use the example format.")

            delete_note = input("Enter note to delete (eg injuries-1, e to exit): ")
            delete_note_split = delete_note.split("-")
            if len(delete_note_split) == 2 and delete_note_split[0] == "behavioural concerns":
                delete_note_split[0] = "behavioural_concerns"

        # If valid note selected (ie if user didn't exit), delete note.
        if delete_note != "e":
            key = delete_note_split[0]
            value = animal_record.get(key)
            del value[int(delete_note_split[1]) - 1]
            animal_record.update({key: value})
            Animal.__notes.update({f"{self.__species}-{self.__id}": animal_record})
            print("Note removed successfully.")
        print()

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
                    for note in animal_record.get("injuries"):
                        injuries += f"Description: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"

                illnesses = ""
                if animal_record.get("illnesses") == []:
                    illnesses += "None\n\n"
                else:
                    for note in animal_record.get("illnesses"):
                        illnesses += f"Description: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"

                behavioural_concerns = ""
                if animal_record.get("behavioural_concerns") == []:
                    behavioural_concerns += "None\n\n"
                else:
                    for note in animal_record.get("behavioural_concerns"):
                        behavioural_concerns += f"Description: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"

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
                        for note in animal_record.get("injuries"):
                            injuries += f"Description: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"

                    illnesses = ""
                    if animal_record.get("illnesses") == []:
                        illnesses += "None\n\n"
                    else:
                        for note in animal_record.get("illnesses"):
                            illnesses += f"Description: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"

                    behavioural_concerns = ""
                    if animal_record.get("behavioural_concerns") == []:
                        behavioural_concerns += "None\n\n"
                    else:
                        for note in animal_record.get("behavioural_concerns"):
                            behavioural_concerns += f"Description: {note[0]}\nDate reported: {note[1]}\nSeverity: {note[2]}\nNotes: {note[3]}\n\n"

                    # Print results.
                    print(f"---{animal_record.get("name")} (ID-{key.split("-")[1]})---\n\n"
                          f"INJURIES\n{injuries}ILLNESSES\n{illnesses}BEHAVIOURAL CONCERNS\n{behavioural_concerns}")

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
    name = property(get_name, set_name)
    age = property(get_age, set_age)
    species = property(get_species)