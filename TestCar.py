from CarClass import Car

car_1 = Car(1997, "make a car")

#calling the accelerate method 5 times. Assume that the unit of the speed of the car is meters per second (m/s)
for i in range (5):
    car_1.accelerate()
    print("The current speed of the car is:", car_1.get_speed(), "m/s")

#calling the accelerate method 5 times. Assume that the unit of the speed of the car is meters per second (m/s)
for i in range (5):
    car_1.brake()
    print("The current speed of the car is:", car_1.get_speed(), "m/s")

