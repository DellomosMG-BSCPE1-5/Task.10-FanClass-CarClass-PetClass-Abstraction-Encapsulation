#create a class named "Fan"
class Fan:
#declare constants to denote the fan speed
    slow = 1
    medium = 2
    fast = 3
#create a parameterized constructor
    def __init__(self, speed = slow, radius = 5, color = "blue", on = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
#create the methods
#the accessor methods for all four data fields
    def get_speed(self):
        return self.__speed
    
    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color
    
    def get_on(self):
        return self.__on