import core.User_Functions as User
import core.Other as Other
import core.Checks as Check
from time import sleep

# Initial Checks

# Checking the Connection to the MySQL Server
connection_status = Check.CheckConnection()
if connection_status is False:
    quit()
else:
    Check.CheckDatabase()  # Checking for the Requirements of the Project

Other.ClearScreen()  # Clear the Terminal Window
Other.Menu()

while True:
    ans = input("Choose an Option Number: ")
    if ans == "1":
        User.Issue_a_book()
    elif ans == "2":
        User.Checkissuebook()
    elif ans == "3":
        User.display()
    elif ans == "4":
        User.ShowallBooks()
    elif ans == "5":
        User.AvailableBooks()
    elif ans == "6":
        Other.ClearScreen()
        Other.Menu()
    elif ans == "7":
        Other.Menu()
    elif ans == "8":
        Other.ClearScreen()
        Other.About()
        while True:
            ask = input("Do you want to Display Menu(Y/N): ")
            if ask in ["Y", "y"]:
                Other.Menu()
                break
            elif ask in ["N", "n"]:
                break
            else:
                print("Please Enter either Y (Yes) or N (No)!")
    elif ans == "9":
        print("Closing all Connections..")
        sleep(0.5)
        print("Thank You!")
        quit()
    else:
        print("Please Enter a Valid Option Number!")
