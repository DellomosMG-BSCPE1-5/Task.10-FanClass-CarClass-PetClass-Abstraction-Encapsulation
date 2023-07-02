from colorama import Fore, Style
from Headers import Header
from FanClass import Fan

fan_header = Header()
fan_header.fan()

fan_1 = Fan(Fan.fast, 10, "yellow", False)
fan_2 = Fan(Fan.medium, 5, "blue", True)

#for Fan number 1
print(Fore.CYAN + Style.NORMAL + "\nFAN #1:", Fore.WHITE + Style.NORMAL + "=" * 86)
print(Fore.CYAN + Style.DIM + "SPEED: ", Fore.WHITE + Style.NORMAL + str(fan_1.get_speed()), "[fast]")    #speed
print(Fore.CYAN+ Style.DIM + "RADIUS:", Fore.WHITE + Style.NORMAL + str(fan_1.get_radius()))             #radius
print(Fore.CYAN + Style.DIM + "COLOR: ", Fore.WHITE + Style.NORMAL + str(fan_1.get_color()))              #color
fan_1.set_on(False)     #on
print(Fore.WHITE + Style.NORMAL + "=" * 94)

#for Fan number 2
print(Fore.CYAN + Style.NORMAL + "\nFAN #2:", Fore.WHITE + Style.NORMAL + "=" * 86)
print(Fore.CYAN + Style.DIM + "SPEED: ", Fore.WHITE + Style.NORMAL + str(fan_2.get_speed()), "[medium]")    #speed
print(Fore.CYAN + Style.DIM + "RADIUS:", Fore.WHITE + Style.NORMAL + str(fan_2.get_radius()))               #radius
print(Fore.CYAN + Style.DIM + "COLOR: ", Fore.WHITE + Style.NORMAL + str(fan_2.get_color()))                #color
fan_2.set_on(True)     #on
print(Fore.WHITE + Style.NORMAL + "=" * 94)