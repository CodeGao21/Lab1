def menu():
    menu_string = "1. Show Menu\n"
    menu_string += "2. Add Numbers\n"
    menu_string += "3. Subtract Numbers\n"
    menu_string += "4. Quit\n"
    return menu_string

# Main Program Starts

import os
os.system('clear')  # Clear the screen
choice = 0

while choice < 4:
    print(menu())
    choice = int(input())

    if choice == 1:
        os.system('clear')
    elif choice == 2:
        print("\n\nAdd Some Numbers\n\n")
    elif choice == 3:
        print("\n\nSubtract some Numbers\n\n")
    else:
        pass
