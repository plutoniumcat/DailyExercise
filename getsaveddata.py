import csv

def get_exercise_dict():
    with open("exerciselist.csv", "r") as file:
        reader = csv.reader(file)
        exercise_dict = dict(reader)
        return exercise_dict

def get_streak_conditions():
    with open("streakconditions.csv", "r") as file:
        reader = csv.reader(file)
        streak_conditions = dict(reader)
        return streak_conditions