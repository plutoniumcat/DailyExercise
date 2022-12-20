import csv
from datetime import datetime, date
import pandas
import constants
from getsaveddata import last_log_date_datetime, get_longest_streak_dict
from menufunctions import input_exercise_type


class CurrentStreaksAlert:
    def __init__(self, exercise_list) -> None:
        self.exercise_list = exercise_list
    
    def current_streaks_alert(self):
        streaks_list = []
        for exercise in self.exercise_list:
            streak = CurrentStreak(constants.DEFAULT_CSV, constants.STREAK_CONDITIONS, exercise, "")
            if streak.current_streak():
                streaks_list.append(streak.current_streak())
        if streaks_list == []:
            print("No current streaks")
        else:
            for item in streaks_list:
                print(item)


class CurrentStreak:
    def __init__(self, log, conditions, exercise, rule) -> None:
        self.log = log
        self.conditions = conditions
        self.exercise = exercise
        self.rule = rule

    def set_exercise(self):
        while True:
            exercise_name = input_exercise_type()
            if exercise_name.lower() == "c":
                break
            elif exercise_name not in constants.EXERCISE_LIST:
                print("Error: Exercise type not recognized.")
            else:
                self.exercise = exercise_name
                break

    def set_streak_rule(self):
        if self.exercise in self.conditions:
            self.rule = int(self.conditions[self.exercise])
        else:
            self.rule = 0

    def test_week(self, history, cursor2, cursor1):
        # Extracts one week from the history based on the cursor position and tests it against the streak rule
        for i in range(cursor2, cursor1 + 1):
            zero_counter = 0
            if history[i] == 0:
                zero_counter += 1
            if zero_counter > self.rule:
                return False # Streak terminates at current week
        else:
            return True # Streak continues through current week

    def evaluate_history(self, history):
        # Determines streak length if rule is 'every second day'
        for i in range(len(history) - 1):
            if history[i] == 0 and history[i + 1] == 0:
                return (i - 1)
            else:
                pass
        return len(history)

    def find_current_streak_length(self):
        last_log_date = last_log_date_datetime()
        # If there are no previous logs return 0
        if last_log_date == 0:
            return 0
        # Get all history for selected exercise then reverse it
        log = pandas.read_csv(self.log)
        exercise_history = log[self.exercise].tolist()
        # Remove empty list item that causes pytest tests to fail
        if not exercise_history[-1] and exercise_history[-1] != 0:
            del exercise_history[-1]
        exercise_history.reverse()
        # If streak rule is "every second day", evaluate the log against that rule
        if self.rule == 8:
            streak_length = self.evaluate_history(exercise_history)
            if streak_length != None:
                return streak_length
            else:
                print("Error: Streak length was None")
                return 0
        # Set two cursors, one to the start of current week and one to most recent day in log
        day_of_week = last_log_date.weekday()
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
        try:
            for i in range(6):
                zero_counter = 0
                for i in range(self.rule + 1):
                    if exercise_history[(cursor2 + i)] == 0:
                        zero_counter += 1
                if zero_counter == (self.rule + 1):
                    break
                cursor2 += 1
        except IndexError:
            pass
        # Fix off by one error
        if self.rule > 0 and self.rule < 8:
            cursor2 += 1
        # cursor2 now contains the length of the streak in days
        return cursor2

    def update_longest_streak(self, streak):
        # Updates longest streak file if current streak is longer than saved streak
        streak_dict = get_longest_streak_dict()
        if streak > streak_dict[self.exercise]:
            streak_dict[self.exercise] = streak
            with open(constants.LONGEST_STREAK_FILE, "w") as outfile:
                writer = csv.writer(outfile)
                for row in streak_dict.items():
                    writer.writerow(row)

    def current_streak(self):
        self.set_streak_rule()
        current_streak = self.find_current_streak_length()
        self.update_longest_streak(current_streak)
        if current_streak:
            return "Your current streak for " + self.exercise + " is " + str(current_streak) + " days."
        else:
            return False

    def check_for_streak(self):
        self.set_exercise()
        if self.current_streak():
            print(self.current_streak())
        else:
            print("No current streak for " + self.exercise + ".")