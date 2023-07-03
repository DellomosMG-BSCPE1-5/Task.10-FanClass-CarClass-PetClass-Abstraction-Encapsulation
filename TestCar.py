from CarClass import Car
from colorama import Fore, Style
from Headers import Header

#objects
car_header = Header()
car_header.car()

car_1 = Car("Model 2000", "Test Drive...")
print(Fore.WHITE + Style.NORMAL + "\n", car_1.get_year_model(), car_1.get_make())

print(Fore.WHITE + Style.NORMAL + "\n[Accelerating...]", "=" * 86)
for i in range (5): #call the accelerate method 5 times. Assume that the unit of the speed of the car is meters per second (m/s)
    car_1.accelerate()
    print(Fore.RED + Style.NORMAL + "current speed:  " + Fore.WHITE + Style.NORMAL + str( car_1.get_speed()) + " m/s")     #get and display the current speed of the car 

print( Fore.WHITE + Style.NORMAL + "\n[Deccelerating...]", "=" * 86)
for i in range (5):     #call the brake method 5 times. Assume that the unit of the speed of the car is meters per second (m/s)
    car_1.brake()
    print(Fore.RED + Style.NORMAL + "current speed:  " + Fore.WHITE + Style.NORMAL + str(car_1.get_speed()) , " m/s")      #get and display the current speed of the car 

print( Fore.WHITE + Style.NORMAL + "\n[Stop]")


