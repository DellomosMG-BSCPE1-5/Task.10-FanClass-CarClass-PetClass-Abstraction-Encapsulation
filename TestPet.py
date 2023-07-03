from colorama import Fore, Style
from Headers import Header
from PetClass import Pet

#objects
pet_header = Header()
pet_data = Pet()

while True:
    #header
    pet_header.pet()

    #pet's data
    print(Fore.WHITE + Style.NORMAL + "\n")
    pet_data.set_name()
    pet_data.set_animal_type()
    pet_data.set_age()

    #displaying pet's data
    print(Fore.YELLOW + Style.NORMAL + "\nYOUR PET'S DATA:", Fore.WHITE + Style.NORMAL + "=" * 69)
    print(Fore.YELLOW + Style.DIM + "NAME:       ", Fore.WHITE + Style.NORMAL + str(pet_data.get_name()))        #name
    print(Fore.YELLOW+ Style.DIM + "ANIMAL TYPE:", Fore.WHITE + Style.NORMAL + str(pet_data.get_animal_type()))  #animal type
    print(Fore.YELLOW + Style.DIM + "AGE:        ", Fore.WHITE + Style.NORMAL + str(pet_data.get_age()), "years old")         #age
    print(Fore.WHITE + Style.NORMAL + "=" * 86)

    again = input("\nDo you want to input data again? Type Y to restart or press another key to quit: ")  # Asking the user if he/she wants to try/start again.
    #if user typed "y", go back to the top.
    if again.upper() == "Y":  
        continue
    break
