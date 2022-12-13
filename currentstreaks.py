import csv
from datetime import datetime, date
import pandas
import constants

class CurrentStreaksAlert:
    def __init__(self) -> None:
        # TODO Takes a list of exercises and generates CurrentStreak objects for them
        pass

class CurrentStreak:
    def __init__(self, exercise, rule) -> None:
        self.exercise = exercise
        self.rule = rule

    def set_exercise(self):
        while True:
            exercise_name = input("Enter exercise type: ")
            if exercise_name.lower() == "q":
                break
            elif exercise_name not in constants.EXERCISE_LIST:
                print("Error: Exercise type not recognized.")
            else:
                self.exercise = exercise_name
                break

    def set_streak_rule(self):
        if self.exercise in constants.STREAK_CONDITIONS:
            self.rule = int(constants.STREAK_CONDITIONS[self.exercise])
        else:
            self.rule = 0

    def test_week(self, history, cursor2, cursor1):
        # Extracts one week from the history based on the cursor position and tests it against the streak rule
        zero_counter = 0
        for i in range(cursor2, cursor1 + 1):
            if history[i] == 0:
                zero_counter += 1
        if zero_counter > self.rule:
            return False # Streak terminates at current week
        else:
            return True # Streak continues through current week

    def find_current_streak_length(self):
        log = pandas.read_csv(constants.DEFAULT_CSV)
        # Check most recent date in log against current date and compare against streak rule
        log_dates = log["DATE"].tolist()
        most_recent_date = datetime.strptime(log_dates[-1], "%Y-%m-%d")
        today = datetime.today()
        log_age = (most_recent_date - today).days
        if log_age > self.rule:
            return 0 # No current streak
        # Get all history for selected exercise, adding zeros to account for log age, then reverse it
        exercise_history = log[self.exercise].tolist()
        for i in range(log_age):
            exercise_history.append(0)
        exercise_history.reverse()
        # Set two cursors, one to the start of current week and the other to the most recent day in the log
        day_of_week = most_recent_date.weekday()
        cursor1 = day_of_week
        cursor2 = 0
        # Check that there is at least one week of history
        if len(exercise_history) > 6:
            # Test each week until one is found that violates the rule
            for i in range((len(exercise_history)//7)):
                if self.test_week(exercise_history, cursor2, cursor1):
                    cursor2 = cursor1 + 1
                    cursor1 += 7
                else:
                    break
        # Continue moving cursor2 forward until the break is found
        for i in range(6):
            zero_counter = 0
            for i in range(self.rule):
                if exercise_history[(cursor2 + i)] == 0:
                    zero_counter += 1
            if zero_counter == self.rule:
                break
            cursor2 += 1
        # cursor2 now contains the length of the streak in days
        return cursor2

    def current_streak(self):
        self.set_exercise()
        self.set_streak_rule()
        current_streak = self.find_current_streak_length()
        if current_streak:
            print("Your current streak for " + self.exercise + " is " + str(current_streak) + " days.")
        else:
            print("No current streak for " + self.exercise + ".")