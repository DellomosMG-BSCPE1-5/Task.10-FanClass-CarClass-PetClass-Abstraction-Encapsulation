#create class named Pet
class Pet:
    #constructor
    def __init__(self, name = " ", animal_type = " ", age = 0):
        #attributes
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    #methods
    #mutator method for all data attributes
    def set_name(self):
        self.__name = str(input("Enter the name of your pet: "))
    
    def set_animal_type(self):
        self.__animal_type = str(input("Enter your pet's animal type: "))
    
    def set_age(self):
        while True:
            try:
                self.__age = int(input("Enter the age of you pet: "))
            except (ValueError):
                print("Invalid input. Please enter a valid whole number for the pet's age.")
            else:
                break   

    #accessor methods for all data attributes
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
