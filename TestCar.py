from pyboxen import boxen
from CarClass import Car
from colorama import Fore, Style
from Headers import Header

car_header = Header()
car_header.car()

car_1 = Car("Model 2000", "Test Drive...")
print(Fore.WHITE + Style.NORMAL + "\n", car_1.get_year_model(), car_1.get_make())

print(Fore.WHITE + Style.NORMAL + "\n[Accelerating...]", "=" * 86)
#calling the accelerate method 5 times. Assume that the unit of the speed of the car is meters per second (m/s)
for i in range (5):
    car_1.accelerate()
    #get the current speed of the car and display it
    print(Fore.RED + Style.NORMAL + "current speed:  " + Fore.WHITE + Style.NORMAL + str( car_1.get_speed()) + " m/s")

print( Fore.WHITE + Style.NORMAL + "\n[Deccelerating...]", "=" * 86)
#calling the brake method 5 times. Assume that the unit of the speed of the car is meters per second (m/s)
for i in range (5):
    car_1.brake()
    #get the current speed of the car and display it
    print(Fore.RED + Style.NORMAL + "current speed:  " + Fore.WHITE + Style.NORMAL + str(car_1.get_speed()) , " m/s")
print( Fore.WHITE + Style.NORMAL + "\n[Stop]")


