# This Module has some Other Commonly used Functions

# Importing Required Modules

import os #when we open-close files we use os module or for file handling operations 
import time


# Functions

def About():
    """
    About() -> Prints the About Information on the Terminal

    Parameters -> None
    """
    # Change the path given here to the absolute path of the README file
    with open(FULL_PATH_TO_THE_README_FILE) as file:
        data = file.read()
        print(data)


def ClearScreen():
    """
    ClearScreen() -> Clears the Terminal Screen

    Parameters -> None
    """

    print("Clearing..")
    time.sleep(2)
    os.system("cls")


def Menu(answer="Yes"):
    """
    Menu() -> Displays the Menu

    Parameters -> Answer (User's Choice on Displaying the Menu, by default it is set to True)
    """

    if answer in ["Yes", "Y"]:
        print("  WELCOME TO LIBRARY MANAGEMENT SYSTEM")
        print("1. Issue_a_book")
        print("2. Checkissuebook")
        print("3. display")
        print("4. ShowallBooks")
        print("5. AvailableBooks")
        print("6. Clear Screen")
        print("7. Menu")
        print("8. About")
        print("9. Exit")
    else:
        pass
