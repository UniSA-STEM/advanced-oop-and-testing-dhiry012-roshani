'''
File: enclosure.py
Description: A module defining a class that represents a zoo enclosure.
Author: Roshani Dhillon
ID: 110459484
Username: dhiry012
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Enclosure:
    '''
    A class which represents a zoo enclosure.

    Parameters:
        area : An integer or float of the area (meters squared) of the enclosure.
        environmental_type : A string indicating the type of enclosure (must be one of "tropical", "grassland", "desert",
            "forest", "freshwater aquatic", "saltwater aquatic", "mountainous", "wetland", or "arctic").

    Attributes:
        id : An integer unique to this enclosure object (no other enclosure objects will have the same number).
        size : An integer or float representing the area (meters squared) of the enclosure.
        environmental_type : A string representing the environmental type of the enclosure.
        cleanliness_level : A number from 0 to 10 indicating how clean the enclosure is.
        MAX_CLEANLINESS_LEVEL : The max cleanliness level. Set to 10.
        staff : A dictionary of which staff members are allocated to this enclosure and what duties they are assigned.
        animals : A list of the animals in the enclosure.
        species : A string indicating which species of animal is housed in this enclosure.

    Methods:
        get_valid_environmental_types() : Returns a list of the valid environmental types for an enclosure.

        get_id() : Returns the enclosure's id number.

        get_size() : Returns the enclosure's area (meters squared).

        set_size(area) : Updates the enclosure's size.

        get_environmental_type() : Returns the enclosure's environmental type.

        set_environmental_type : Changes the enclosure's environmental type.

        get_cleanliness_level() : Returns the cleanliness level of the enclosure (0-10).

        get_staff() : Returns a dictionary of the staff assigned to the enclosure.

        get_animals() : Returns a list of the animals currently in the enclosure.

        get_species() : Returns the species of animal currently being housed in the enclosure.

        add_animal(animal) : Adds an animal to the enclosure.

        remove_animal(animal) : Removes an animal from the enclosure.

        add_staff(staff, duty) : Assigned a staff member to the enclosure.

        remove_staff(staff, duty) : Removes a staff member from the enclosure.

        reduce_cleanliness(amount) : Reduces the enclosure's cleanliness level.

        clean(staff) : A Zookeeper cleans the enclosure.

        __eq__(other) : Determines if the enclosure is equal to another.

        __str__() : Returns a string of the enclosure's details.

    Properties:
        id : get_id()
        size : get_size(), set_size()
        environmental_type : get_environmental_type(), set_environmental_type()
        cleanliness_level : get_cleanliness_level()
        staff : get_staff()
        animals : get_animals()
        species : get_species()
        valid_environmental_types : get_valid_environmental_types()
    '''

    # Global attributes.
    __next_id = 1
    __valid_environmental_types = ["tropical", "grassland", "desert", "forest", "freshwater aquatic", "saltwater aquatic",
                                   "mountainous", "wetland", "arctic"]

    def __init__(self, area:int|float, environmental_type:str) -> None:
        self.__id = self.__create_id()
        self.__size = None
        self.__environmental_type = None
        self.__cleanliness_level = 10
        self.__MAX_CLEANLINESS_LEVEL = 10
        self.__staff = {"feeding": [], "cleaning": [], "health": [], "research": [], "general": []}
        self.__animals = []
        self.__species = None

        # Validate.
        self.set_size(area)
        self.set_environmental_type(environmental_type)

    def get_valid_environmental_types(self) -> list:
        '''
        Returns:
             list

        Returns a list of the valid environmental types for an enclosure.
        '''
        return self.__valid_environmental_types

    def get_id(self) -> int:
        '''
        Returns:
            integer

        Returns the enclosure's id number.
        '''
        return self.__id

    def __create_id(self) -> int:
        '''
        Returns:
            integer

        A private method used when the object is created, which returns the next id number.
        '''
        temp = Enclosure.__next_id
        Enclosure.__next_id += 1
        return temp

    def get_size(self) -> int|float|None:
        '''
        Returns:
            integer, float, or None

        Returns the enclosure's area (meters squared).
        If no area is specified, will return None.
        '''
        return self.__size

    def set_size(self, area:int|float) -> None:
        '''
        Parameters:
            area : An integer or float of the enclosure's area (meters squared).

        Returns:
            None

        Updates the size of the enclosure, if the provided value is valid.
        If not valid, displays an error message.
        '''
        if type(area) == int or type(area) == float:
            self.__size = area
        else:
            print("Invalid area for enclosure.")

    def get_environmental_type(self) -> str|None:
        '''
        Returns:
            string or None

        Returns the enclosure's environmental type.
        If no environmental type has been specified, will return None.
        '''
        return self.__environmental_type

    def set_environmental_type(self, environment:str) -> None:
        '''
        Parameters:
            environment : A string describing the environment of the enclosure.

        Returns:
            None

        Updates the environment type of the enclosure, if a valid type is provided.
        If there are animals in the enclosure, displays error message.
        If the environment is invalid, displays error message.
        '''
        if self.animals != []:
            print("There are animals in this enclosure. Cannot change environment.")
        elif environment in self.__valid_environmental_types:
            self.__environmental_type = environment
        else:
            print("Invalid environmental type.")

    def get_cleanliness_level(self) -> int|float:
        '''
        Returns:
            integer or float

        Returns the cleanliness level of the enclosure (0-10).
        '''
        return self.__cleanliness_level

    def get_staff(self) -> dict:
        '''
        Returns:
            dictionary

        Returns a dictionary of the staff assigned to the enclosure by duties.
        '''
        return self.__staff

    def get_animals(self) -> list:
        '''
        Returns:
            list

        Returns the animals currently in the enclosure.
        '''
        return self.__animals

    def get_species(self) -> str|None:
        '''
        Returns:
            string or None

        Returns the species of animal currently being housed in the enclosure.
        If there are no animals in the enclosure (and therefore no species), will return None.
        '''
        return self.__species

    def add_animal(self, animal) -> None:
        '''
        Parameters:
             animal : An Animal class object to add to the enclosure.

        Returns:
            None

        Adds an animal to the enclosure. This reduces the enclosure's cleanliness by 1.
        If the enclosure has no specified environment type, the species in incompatible, the animal is under treatment,
        environmental type of enclosure is incompatible with animal's needs, or the animal is already in an
        enclosure, displays error message.
        If the provided animal is invalid, displays error message.
        '''
        try:
            if self.environmental_type is None:
                print("Environment type not set. Cannot add animal.")
            elif self.species is not None and self.species != animal.species:
                print(f"{animal.name} is not {self.species}. Cannot add to enclosure.")
            elif animal.under_treatment:
                print(f"Cannot add {animal.name} to enclosure while under treatment.")
            elif self.environmental_type not in animal.environment_types:
                print(f"Enclosure type ({self.environmental_type}) incompatible with {animal.name}'s requirements.")
            elif animal in self.animals:
                print(f"{animal.name} already in this enclosure.")
            elif animal.enclosure is not None:
                print(f"{animal.name} is already in another enclosure.")
            else:
                if self.species is None:
                    self.__species = animal.species  # If first animal, set enclosure species to animal species.
                self.__animals.append(animal)        # Add animal to list.
                animal.add_to_enclosure(self)        # Add enclosure to animal.
                self.reduce_cleanliness(1)           # Reduce cleanliness.
                print(f"{animal.name} added to enclosure {self.id}.")
        except AttributeError:
            print("Invalid animal.")

    def remove_animal(self, animal) -> None:
        '''
        Parameters:
             animal : An Animal class object to remove from the enclosure.

        Returns:
            None

        Removes an animal from the enclosure.
        If the animal is not in the enclosure, displays error message.
        If the provided animal is invalid, displays error message.
        '''
        try:
            check = animal.under_treatment  # Throw Exception if invalid animal object.

            if animal not in self.animals:
                print("Animal is not in this enclosure.")
            else:
                self.__animals.remove(animal)          # Remove animal from enclosure.
                animal.remove_from_enclosure(self)     # Remove enclosure from animal.
                print(f"{animal.name} removed from enclosure.")
        except AttributeError:
            print("Invalid animal.")

    def add_staff(self, staff, duty="general") -> None:
        '''
        Parameters:
             staff : A Staff class object to assign to the enclosure.
             duty : A string defining what duty to assign the staff. Defaults to 'general'.

        Returns:
            None

        Adds a staff member to the enclosure based on their role. If successfully added, prints a confirmation message.
        If the duty provided is invalid, the staff member is already assigned this duty, or the duty is not one of the
        staff's responsibilities, displays error message.
        If the provided staff is invalid, displays error message.
        '''
        try:
            check = staff.role  # Throw an Exception if not Staff object.

            if duty not in ["feeding", "cleaning", "health", "research", "general"]:
                print("Invalid duty. Must be 'feeding', 'cleaning', 'health', 'research', or 'general'.")
            elif staff in self.staff.get(duty):
                print(f"{staff.name} is already assigned this duty.")
            elif duty not in staff.duties:
                print(f"{duty.capitalize()} is not one of {staff.name}'s duties.")
            else:
                duty_list = self.staff.get(duty)        # Add staff to enclosure.
                duty_list.append(staff)
                self.__staff.update({duty: duty_list})
                staff.add_to_enclosure(self)            # Add enclosure to staff.
                print(f"{staff.name} assigned to {duty} duties in enclosure {self.id}.")
        except AttributeError:
            print("Invalid staff.")

    def remove_staff(self, staff, duty="general") -> None:
        '''
        Parameters:
             staff : A Staff class object to remove from the enclosure.
             duty : A string defining what duty from which to remove the staff. Defaults to 'general'.

        Returns:
            None

        Removes a staff member from specific duties.
        If the staff member is not assigned to that duty or the duty provided is invalid, displays error message.
        If the provided staff is invalid, displays error message.
        '''
        try:
            check = staff.role  # Throw an Exception if not Staff object.

            if duty not in ["feeding", "cleaning", "health", "research", "general"]:
                print("Invalid duty. Must be 'feeding', 'cleaning', 'health', 'research', or 'general'.")
            elif staff not in self.staff.get(duty):
                print(f"{staff.name} has not been assigned this duty.")
            else:
                duty_list = self.staff.get(duty)
                duty_list.remove(staff)
                self.__staff.update({duty: duty_list})
                staff.remove_from_enclosure(self)
                print(f"{staff.name} removed from {duty} duties in enclosure {self.id}.")
        except AttributeError:
            print("Invalid staff.")

    def reduce_cleanliness(self, amount:int|float) -> None:
        '''
        Parameters:
             amount : An integer or float by which to reduce the enclosure's cleanliness level.

        Returns:
            None

        Reduces the enclosure's cleanliness level by a specified amount.
        Note that the lowest the level can go is 0.
        If the given amount is invalid (not a positive number), displays error message.
        '''
        try:
            # Ensure amount is a positive number.
            if amount < 0:
                raise TypeError

            self.__cleanliness_level -= amount
            if self.__cleanliness_level < 0:
                self.__cleanliness_level = 0
        except TypeError:
            print("Invalid amount.")

    def clean(self, staff) -> None:
        '''
        Parameters:
             staff : A Zookeeper object who will clean the enclosure.

        Returns:
            None

        Cleans the enclosure, resetting cleanliness level to max and displaying "<name> is cleaning the enclosure...".
        If the staff member is not a Zookeeper or not assigned to the enclosure, displays error message.
        If staff is not a valid Staff/Zookeeper object, displays error message.
        '''
        try:
            # Check if staff is Zookeeper.
            if staff.role != "Zookeeper":
                print(f"{self.name} is not a Zookeeper.")
            else:  # If staff is Zookeeper...
                # Check if Zookeeper assigned to enclosure.
                zookeepers = []
                for key in self.staff.keys():
                    if "Zookeeper" in key:
                        zookeepers.append(self.staff.get(key))

                if staff not in zookeepers:
                    print(f"{staff.name} is not assigned to this enclosure.")
                else:
                    print(f"{staff.name} is cleaning the enclosure...")
                    self.__cleanliness_level = self.__MAX_CLEANLINESS_LEVEL
        except AttributeError:
            print("Invalid staff.")

    id = property(get_id)
    size = property(get_size, set_size)
    environmental_type = property(get_environmental_type, set_environmental_type)
    cleanliness_level = property(get_cleanliness_level)
    staff = property(get_staff)
    animals = property(get_animals)
    species = property(get_species)
    valid_environmental_types = property(get_valid_environmental_types)

    def __eq__(self, other:Enclosure) -> bool:
        '''
        Parameters:
            other : Another Enclosure object to which this object is compared.

        Returns:
            boolean

        Compares two Enclosure objects and returns True of the objects are equal or False if not.
        The objects are equal if they are both of the Enclosure class and have the same id number.
        '''
        return isinstance(other, Enclosure) and self.id == other.id

    def __str__(self) -> str:
        '''
        Returns:
             string

        Returns a string of the enclosure's details in the following format:

        ---ENCLOSURE REPORT---

        ID: <id>

        Type: <environmental_type>

        Size: <size>m\u00b2

        Cleanliness level: <cleanliness_level>/10

        Animals:

        <animal name> (ID-<animal id>, species <species>)

        <animal name> (ID-<animal id>, species <species>)

        Staff:

        <staff name> (ID-<staff id>, <role>)

        <staff name> (ID-<staff id>, <role>)
        '''
        size_statement = f"{self.size}m\u00b2" if self.size is not None else "None"

        animal_statement = ""
        if self.animals == []:
            animal_statement += "None"
        else:
            for animal in self.animals:
                animal_statement += f"\n> {animal.name} (ID-{animal.id}, species {animal.species})"

        staff_statement = ""
        for duty in self.staff.keys():
            staff_statement += f"\n> {duty.capitalize()}: "
            if self.staff.get(duty) == []:
                staff_statement += "None"
            for staff in self.staff.get(duty):
                staff_statement += f"{staff.name} (ID-{staff.id}), "

            staff_statement = staff_statement.strip(", ")

        return (f"\n---ENCLOSURE REPORT---\nID: {self.id}\nType: {self.environmental_type}\nSize: {size_statement}\n"
                f"Cleanliness level: {self.cleanliness_level}/10\n\nAnimals: {animal_statement}\n\nStaff:{staff_statement}"
                f"\n--------------------")
