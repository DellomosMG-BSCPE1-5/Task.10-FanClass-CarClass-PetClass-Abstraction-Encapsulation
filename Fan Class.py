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