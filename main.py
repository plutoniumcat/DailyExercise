import os
import constants

def main():
    # Main Menu loop
    while True:
        try:
            if not os.path.isfile(constants.DEFAULT_CSV):
                log = open(constants.DEFAULT_CSV, "w")
            else:
                log = open(constants.DEFAULT_CSV, "a")
            display_main_menu()
        except FloatingPointError:
            log.close()
            print("Thank you for using DailyExercise.")
            exit()

def quit_function():
    # TODO Save file before exiting
    raise FloatingPointError

def get_menu_selection(number_of_menu_items):
    while True:
        menu_selection = input("Enter your selection, or 'q' to quit: ")
        if menu_selection.lower() == "q":
            quit_function()
        elif not menu_selection.isnumeric():
            print("Invalid menu selection. Enter a number, or 'q' to quit: ")
            continue
        elif int(menu_selection) > number_of_menu_items or int(menu_selection) == 0:
            print("Invalid menu selection. Enter a number, or 'q' to quit: ")
            continue
        else:
            return int(menu_selection)

def press_enter_to_continue():
    user_input = input("Press enter to continue")
    if user_input == "q":
        quit_function()

def display_main_menu():
            os.system('clear')
            print("Main Menu\n1. Log today's workout\n2. Add new exercise type\n3. Streaks\n4. History\nEnter a number, or 'q' to quit: ")
            main_menu_selection = get_menu_selection(constants.MAIN_MENU_ITEMS)
            if main_menu_selection == 1:
                todays_workout_menu()
            elif main_menu_selection == 2:
                add_new_exercise_menu()
            elif main_menu_selection == 3:
                streaks_menu()
            elif main_menu_selection == 4:
                history_menu()

def todays_workout_menu():
    os.system('clear')
    print("TODO: Add today's workout submenu")
    press_enter_to_continue()
    display_main_menu()

def add_new_exercise_menu():
    os.system('clear')
    print("TODO: Add new exercise submenu")
    press_enter_to_continue()
    display_main_menu()

def streaks_menu():
    os.system('clear')
    print("TODO: Add streaks submenu")
    press_enter_to_continue()
    display_main_menu()

def history_menu():
    os.system('clear')
    print("TODO: Add history submenu")
    press_enter_to_continue()
    display_main_menu()


main()