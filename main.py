import os
import csv
from datetime import date
import constants
from menufunctions import *
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

def display_main_menu():
            os.system('clear')
            print("Main Menu\n1. Log today's workout\n2. Add new exercise type\n3. Streaks"
            "\n4. History")
            main_menu_selection = get_menu_selection(constants.MAIN_MENU_ITEMS)
            if main_menu_selection == 1:
                todays_workout()
            elif main_menu_selection == 2:
                add_new_exercise()
            elif main_menu_selection == 3:
                streaks_menu()
            elif main_menu_selection == 4:
                history_menu()

def todays_workout():
    os.system('clear')
    # TODO check if today's workout already recorded
    todays_workout = Workout(date.today(), {}, False)
    todays_workout.get()
    press_enter_to_continue()
    display_main_menu()

def add_new_exercise():
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