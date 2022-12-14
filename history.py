import pandas
import constants

class History:
    def __init__(self, exercise, history) -> None:
        self.exercise = exercise
        self.history = history

    def set_exercise(self):
        while True:
            user_input = input("Enter exercise type: ")
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
        history = log[self.exercise].tolist()

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
        pass

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
        self.set_history()
        measurement = self.retrieve_measurement()
        total_days = str(self.retrieve_total_days())
        total_reps = str(self.retrieve_total_reps())
        increase = self.retrieve_increase()
        print("You have done " + total_reps + " " + measurement + " of " + self.exercise + 
        " over " + total_days + " days. " "You have increased by " + str(increase[1] - increase[0]) 
        + " " + measurement + ", from " + str(increase[0]) + " " + measurement + " to "
        + str(increase[1]) + " " + measurement + ".")