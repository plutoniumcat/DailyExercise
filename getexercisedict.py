import csv

def get_exercise_dict():
    with open("exerciselist.csv", "r") as file:
        reader = csv.reader(file)
        exercise_dict = dict(reader)
        return exercise_dict