import os
import csv
import constants
from getsaveddata import get_last_log_date
from menufunctions import quit_function
from currentstreaks import CurrentStreaksAlert


class Workout:
    def __init__(self, log, date, workout_dict, confirmation):
        self.log = log
        self.workout_dict = workout_dict
        self.date = date
        self.confirmation = confirmation

    def check_for_todays_workout(self):
        # Open log file and check if there is an existing workout for today
        last_log = get_last_log_date()
        if self.date == last_log:
            return True
        else:
            return False

    def get_workout_from_user(self):
        if not self.check_for_todays_workout():
            while True:
                user_input = input("Now editing today's workout.\nEnter an exercise followed by a number "
                "(reps or duration) e.g. 'push-up 20'. Type 'f' when finished: ")
                if user_input.lower() == "q":
                    quit_function()                
                elif user_input.lower() == "f":
                    break
                else:
                    # Separate number from exercise name
                    number = user_input.split()[-1]
                    # Remove number and extra space from end of exercise name
                    exercise_name = user_input[:-(len(number) + 1)]
                    if exercise_name not in constants.EXERCISE_LIST:
                        print("Error: Enter a valid exercise type and a number.")
                    elif not number.isnumeric():
                        print("Error: Exercise reps or duration must be numeric.")
                    else:
                        self.workout_dict[exercise_name] = number

        else:
            print("Error: You have already logged a workout for today.")
            # "To edit previous workouts, use the History menu.")
            return

    def show_workout(self):
        os.system('clear')
        for key, value in self.workout_dict.items():
            print(key, value)

    def edit_workout(self):
        self.show_workout()
        self.get_workout_from_user()

    def confirm_workout(self):
        if self.workout_dict == {}:
            return
        else:
            while True:
                self.show_workout()
                user_input = input("Log this workout? 'Y' for 'yes', 'e' for 'edit' or 'q' for quit. ")
                if user_input.lower() == "q":
                    return
                elif user_input.lower() == "y":
                    self.confirmation = True
                    return
                elif user_input.lower() == "e":
                    self.edit_workout()
                else:
                    continue

    def write_workout_to_csv(self):
        if self.confirmation == True:
            write_to_csv_dict = {"date": self.date}
            # Create comprehensive dictionary with every exercise in exercise list
            for exercise in constants.EXERCISE_LIST:
                write_to_csv_dict[exercise] = 0
            # Copy today's workout into comprehensive dictionary
            for key in self.workout_dict:
                write_to_csv_dict[key] = self.workout_dict[key]
            with open(self.log, "a") as log:
                writer = csv.writer(log)
                writer.writerow(write_to_csv_dict.values())

    def streak_alert(self):
        if self.confirmation == True:
            streak_alert = CurrentStreaksAlert(list(self.workout_dict.keys()))
            streak_alert.current_streaks_alert()

    def get(self):
        self.get_workout_from_user()
        self.confirm_workout()
        self.write_workout_to_csv()
        self.streak_alert()