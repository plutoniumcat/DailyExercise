import os
import csv
from datetime import date, datetime, timedelta
import constants
from menufunctions import *
from getsaveddata import get_last_log_date, determine_log_age
from workout import Workout
from newexercise import NewExercise
from streakconditions import StreakConditions
from currentstreaks import CurrentStreak, CurrentStreaksAlert
from history import History

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
    else:
        # Check if last workout was earlier than yesterday
        last_log_date = get_last_log_date()
        today = date.today()
        yesterday = str(datetime.today() - timedelta(days=1))
        if last_log_date in [today, yesterday, 0]:
            return
        else:
            # Determine how many days ago the last log was
            log_age = determine_log_age(last_log_date)
            # Save a row of zeros for every missed day
            for i in reversed(range(1, log_age - 1)):
                # Find the date
                workout_date = (datetime.today() - timedelta(days=i)).date()
                # Generate blank workout for that date
                blank_workout = Workout(workout_date, {"aerobics":0}, True)
                blank_workout.write_workout_to_csv()

def display_main_menu():
            clear_screen()
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
    clear_screen()
    todays_workout = Workout(str(date.today()), {}, False)
    todays_workout.get()
    press_enter_to_continue()
    display_main_menu()

def add_new_exercise():
    clear_screen()
    new_exercise = NewExercise("", "")
    new_exercise.get()
    press_enter_to_continue()
    display_main_menu()

def streaks_menu():
    clear_screen()
    print("Streaks\n1. View all current streaks\n2. Search for current streak\n3. Define streak conditions"
    "\n4. Return to main menu")
    streak_menu_selection = get_menu_selection(constants.STREAK_MENU_ITEMS)
    if streak_menu_selection == 1:
        view_streak = CurrentStreaksAlert(constants.EXERCISE_LIST)
        view_streak.current_streaks_alert()
    elif streak_menu_selection == 2:
        view_streak = CurrentStreak("", "")
        view_streak.check_for_streak()
    elif streak_menu_selection == 3:
        new_streak_condition = StreakConditions("", "", False)
        new_streak_condition.define_streak_conditions()
    elif streak_menu_selection == 4:
        pass
    press_enter_to_continue()
    display_main_menu()

def history_menu():
    clear_screen()
    history = History("", [])
    history.view_history()
    press_enter_to_continue()
    display_main_menu()

main()