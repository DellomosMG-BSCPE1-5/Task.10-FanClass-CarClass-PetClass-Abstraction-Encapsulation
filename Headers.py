from art import *
from colorama import Fore, Style

class Header:
    def fan(self):
        program_title = text2art("  Fan  ", font='tarty1', chr_ignore=True)
        print(Fore.CYAN + program_title)    

    def car(self):
        program_title = text2art("  Car  ", font='tarty1', chr_ignore=True)
        print(Fore.RED + program_title)

    def pet(self):
        program_title = text2art("  Pet  ", font='tarty1', chr_ignore=True)
        print(Fore.WHITE + program_title)