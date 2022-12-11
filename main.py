import os
import csv
from datetime import date
import constants
from workout import Workout
from newexercise import NewExercise

def main():
    # Main Menu loop
    while True:
        try:
            initialize_log()
            display_main_menu()
        except FloatingPointError:
            print("Thank you for using DailyExercise.")
            exit()

def initialize_log():
    # Create log and input column headers if log does not already exist
    if not os.path.isfile(constants.DEFAULT_CSV):
        header_list = ["DATE"] + constants.EXERCISE_LIST
        with open(constants.DEFAULT_CSV, "w") as log:
            writer = csv.writer(log, delimiter=",")
            writer.writerow(header_list)

def quit_function():
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
            print("Main Menu\n1. Log today's workout\n2. Add new exercise type\n3. Streaks"
            "\n4. History")
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
    get_todays_workout()
    press_enter_to_continue()
    display_main_menu()

def get_todays_workout():
    # TODO check if today's workout already recorded
    todays_workout = Workout(date.today(), {}, False)
    todays_workout.get()

def add_new_exercise_menu():
    os.system('clear')
    new_exercise = NewExercise("", "")
    new_exercise.get()
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