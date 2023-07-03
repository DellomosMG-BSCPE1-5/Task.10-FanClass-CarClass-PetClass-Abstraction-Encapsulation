#create a class named Car
class Car:
    #create the constructor
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    #create the necessary methods
    #the mutator methods for the two data fields
    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make    
        
    #the accessor methods for the two data fields
    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
       
    #accelerate()
    def accelerate(self):
        #the speed data attribute will increase by 5 
        self.__speed += 5

    #brake()
    def brake(self):
        #if the speed data attribute is equal or less than to zero, then it will be equal to zero.
        if self.__speed <= 0:
            self.__speed = 0
        #else, the speed data attribute will decrease by 5
        else:
            self.__speed -= 5
            
    #get_speed()
    def get_speed(self):
        #return the current speed
        return self.__speed
