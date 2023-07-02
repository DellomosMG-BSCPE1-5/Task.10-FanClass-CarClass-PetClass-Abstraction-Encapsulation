from FanClass import Fan

fan_1 = Fan(Fan.fast, 10, "yellow", False)
fan_2 = Fan(Fan.medium, 5, "blue", True)

#for fan number 1
print("SPEED: ", fan_1.get_speed(), "[fast]")   #speed
print("RADIUS:", fan_1.get_radius())            #radius
print("COLOR: ", fan_1.get_color())             #color
fan_1.set_on(False)                             #on

#for fan number 2
print("\nSPEED: ", fan_2.get_speed(), "[medium]") #speed
print("RADIUS:", fan_2.get_radius())            #radius
print("COLOR: ", fan_2.get_color())             #color
fan_2.set_on(True)                              #on
