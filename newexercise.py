import constants
import pandas
from getsaveddata import get_log_dates
from menufunctions import quit_function

class NewExercise:
    def __init__(self, exercise_name, measurement):
        self.exercise_name = exercise_name
        self.measurement = measurement

    def save_to_list(self):
        string = "\n" + self.exercise_name + ", " + self.measurement
        with open(constants.EXERCISE_FILE, "a") as file:
            file.write(string)

    def populate_log(self):
        # Fill log history with zeros for new exercise
        log_dates = get_log_dates()
        zeroes = []
        for i in range(len(log_dates)):
            zeroes.append(0)
        log = pandas.read_csv(constants.DEFAULT_CSV)
        log[self.exercise_name] = zeroes
        log.to_csv(constants.DEFAULT_CSV)

    def save_to_longest_streak(self):
        string = "\n" + self.exercise_name + ",0"
        with open(constants.LONGEST_STREAK_FILE, "a") as file:
            file.write(string)

    def get_new_exercise_from_user(self):
        exercise_name = ""
        exercise_measurement = ""
        while True:
            exercise_name = input("Enter the name of the new exercise to be tracked, or 'c' to cancel: ")
            if exercise_name.lower() == "q":
                quit_function()
            elif exercise_name.lower() == "c":
                return
            elif not exercise_name.isalnum() or len(exercise_name) > 50:
                print("Error: Exercise names must be alphanumeric and less than 50 characters.")
            elif exercise_name.lower() in constants.EXERCISE_LIST:
                print("Error: Exercise already exists.")
            else:
                self.exercise_name = exercise_name.lower()
                break
        while True:
            exercise_measurement = input("Enter the measurement for this exercise (reps or minutes): ")
            if exercise_measurement.lower() == "q":
                quit_function()
            elif not exercise_measurement.lower() in ["reps", "minutes"]:
                print("Error: Please enter either 'reps' or 'minutes'.")
            else:
                self.measurement = exercise_measurement.lower()
                break

    def confirm_new_exercise(self):
        if self.exercise_name == "":
            return
        else:
            print("The new exercise is " + self.exercise_name + " measured in " + self.measurement + ".")
            user_input = input("Confirm new exercise? Y/N ")
            if user_input.lower() == "y":
                self.save_to_list()
                self.populate_log()
                self.save_to_longest_streak()
            else:
                return

    def get(self):
        self.get_new_exercise_from_user()
        self.confirm_new_exercise()