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

    def write_workout_to_csv(self):
            # TODO Save workout to CSV file
    # for key in todays_workout_dict:
    #     # open csv file
    #     # get column headers
    #     # write reps to appropriate columns
    #     pass
        pass