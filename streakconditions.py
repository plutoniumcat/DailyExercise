import csv
import constants
from menufunctions import get_menu_selection, clear_screen, input_exercise_type

class StreakConditions:
    def __init__(self, exercise, rule, overwrite):
        self.exercise = exercise
        self.rule = rule
        self.overwrite = overwrite

    def set_exercise(self):
        clear_screen()
        while True:
            exercise_name = exercise_name = input_exercise_type()
            if exercise_name.lower() == 'c':
                break
            elif exercise_name not in constants.EXERCISE_LIST:
                print("Error: Exercise type not recognized.")
                continue
            elif exercise_name in constants.STREAK_CONDITIONS:
                user_input = input("There is an existing streak condition for this exercise."
                " Do you wish to update it? Y/N ")
                if user_input.lower() == "y":
                    self.exercise = exercise_name
                    self.overwrite = True
                    return
                else:
                    return 
            else:
                self.exercise = exercise_name
            return

    def set_rule(self):
        clear_screen()
        print("Choose a rule\n1. Every day\n2. Every second day\n3."
        " Once a week\n4. Twice a week\n5. Three times a week\n6. "
        "Four times a week\n7. Five times a week\n8. Six times a week")
        selection = get_menu_selection(8)
        if selection == 1:
            rule = 0
        elif selection == 2:
            rule = 8
        elif selection == 3:
            rule = 6
        elif selection == 4:
            rule = 5
        elif selection == 5:
            rule = 4
        elif selection == 6:
            rule = 3
        elif selection == 7:
            rule = 2
        elif selection == 8:
            rule = 1
        self.rule = rule
        return

    def save_streak_conditions(self):
        streak_conditions = self.exercise + "," + self.rule + "\n"
        rule_list = ["every day", "six times a week", "five times a week", "four times a week", 
        "three times a week", "twice a week", "once a week", "every second day"]
        print(self.exercise + ", " + rule_list[self.rule])
        user_input = input("Confirm new streak conditions? Y/N ")
        if user_input.lower() == "y":
            if self.overwrite == False:
                with open("streakconditions.csv", "a") as file:
                    file.write(streak_conditions)
            else:
                constants.STREAK_CONDITIONS[self.exercise] = self.rule
                with open("streakconditions.csv", "w") as file:
                    for key in constants.STREAK_CONDITIONS:
                        file.write(key + "," + constants.STREAK_CONDITIONS[key] + "\n")
                return
        else:
            return

    def define_streak_conditions(self):
        self.set_exercise()
        self.set_rule()
        if self.exercise == "":
            return
        else:
            self.save_streak_conditions()