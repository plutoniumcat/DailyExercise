import csv
import pandas
import constants

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

def get_last_log_date():
    log = pandas.read_csv(constants.DEFAULT_CSV)
    log_dates = log["DATE"].tolist()
    if len(log_dates) == 0:
        return 0
    last_log_date = log_dates[-1]
    return last_log_date