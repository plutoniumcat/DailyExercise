import pandas
import constants
from getsaveddata import get_longest_streak_dict
from menufunctions import input_exercise_type

class History:
    def __init__(self, exercise, history) -> None:
        self.exercise = exercise
        self.history = history

    def set_exercise(self):
        while True:
            user_input = input_exercise_type()
            if user_input.lower == "c":
                break
            else:
                try:
                    if user_input not in constants.EXERCISE_LIST:
                        print("Error: Exercise type not recognized.")
                    else:
                        self.exercise = user_input
                        break
                except Exception as e:
                    # TODO create specific exception handling
                    print(e)

    def set_history(self):
        log = pandas.read_csv(constants.DEFAULT_CSV)
        self.history = log[self.exercise].tolist()

    def retrieve_measurement(self):
        return constants.EXERCISE_DICT[self.exercise]

    def retrieve_total_days(self):
        total = 0
        for day in self.history:
            if day > 0:
                total += 1
        return total

    def retrieve_total_reps(self):
        total = 0
        for day in self.history:
            total += day
        return total

    def retrieve_longest_streak(self):
        streak_dict = get_longest_streak_dict()
        return streak_dict[self.exercise]

    def retrieve_increase(self):
        initial = 0
        for day in self.history:
            if day > 0:
                initial = day
                break
        highest = 0
        for day in self.history:
            if day > highest:
                highest = day
        return [initial, highest]

    def retrieve_graph(self):
        pass

    def view_history(self):
        self.set_exercise()
        if self.exercise == "":
            return
        self.set_history()
        exercise = self.exercise
        measurement = self.retrieve_measurement()
        if measurement == "reps":
            exercise = exercise + "s"
        total_reps = self.retrieve_total_reps()
        if measurement == "minutes" and total_reps > 59:
            total_reps = str(total_reps//60) + " hours and " + str(total_reps % 60)
        total_days = self.retrieve_total_days()
        increase = self.retrieve_increase()
        streak = self.retrieve_longest_streak()
        print("You have done " + str(total_reps) + " " + measurement + " of " + exercise + 
        " over " + str(total_days) + " days. " "You have increased by " + str(increase[1] - increase[0]) 
        + " " + measurement + ", from " + str(increase[0]) + " " + measurement + " to "
        + str(increase[1]) + " " + measurement + ". Your longest streak is " + str(streak) + " days.")