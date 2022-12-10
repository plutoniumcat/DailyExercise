import csv
import constants

class Workout:
    def __init__(self, date, workout_dict):
        self.workout_dict = workout_dict
        self.date = date

    def get_workout_from_user(self):
        user_input = ""
        while True:
            user_input = input("Enter an exercise followed by a number (reps or duration) "
                "e.g. 'push-up 20'. Type 'f' when finished:")
            if user_input.lower() == "f":
                break
            else:
                try:
                    # Separate number from exercise name
                    number = user_input.split()[-1]
                    # Remove number and extra space from end of exercise name
                    exercise_name = user_input[:-(len(number) + 1)]
                    if exercise_name not in constants.EXERCISE_LIST:
                        print("Error: Exercise type not recognized.")
                    elif not number.isnumeric():
                        print("Error: Exercise reps or duration must be numeric.")
                    else:
                        self.workout_dict[exercise_name] = number
                except Exception as e:
                    # TODO create specific exception handling
                    print(e)

    def confirm_workout(self):
        # TODO Display workout information to user and ask them to confirm
        pass

    def write_workout_to_csv(self):
        # create dictionary with every exercise in exercise list
        write_to_csv_dict = {"date": self.date}
        for exercise in constants.EXERCISE_LIST:
            write_to_csv_dict[exercise] = 0
        for key in self.workout_dict:
            write_to_csv_dict[key] = self.workout_dict[key]
        with open(constants.DEFAULT_CSV, "a") as log:
            writer = csv.writer(log)
            writer.writerow(write_to_csv_dict.values())